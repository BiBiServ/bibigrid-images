#!/bin/bash

function usage {
cat << "USAGE"
usage : ${0} (14.04|16.04) - creates a Ubuntu 14.04/16.04 base image"
        ${0} 14.04 master  - creates a BiBiGrid Master image on top of Ubuntu 14.04"
        ${0} 14.04 slave   - creates a BiBiGrid Slave image on top of Ubuntu 14.04" 

Requirements: 
- installed openstacke cmdline tools (pip install --user openstack)
- sourced OpenStack RC File v3
- present configurations file (~/.${0}), e.g.

export PROXYSERVER=proxy.cebitec.uni-bielefeld.de
export PROXYPORT=3128
export HTTP_PROXY="http://$(PROXYSERVER):$(PROXYPORT)"
export HTTPS_PROXY="https://$(PROXYSERVER):$(PROXYPORT)"
export FTP_PROXY="ftp://$(PROXYSERVER):$(PROXYPORT)"
export NO_PROXY=localhost,127.0.0.1,169.254.169.254,swift,openstack.cebitec.uni-bielefeld.de

export OS_KEY=os-bibi
export OS_NET=b9f8e25f-98ca-4e22-9c1e-152d9aca5aa5
export OS_EXTERN=cebitec
export OS_FLAVOR=de.NBI.default

All PROXY variables are optional.
USAGE
	exit
}

function log { date +\(%H:%M:%S\)\ "$1"; }
function check_service {
  /bin/nc ${1} ${2} </dev/null 2>/dev/null
  while test $? -eq 1; do
    log "wait 10s for service available at ${1}:${2}"
    sleep 10
    /bin/nc ${1} ${2} </dev/null 2>/dev/null
  done
}



# Check for configuration file


if [ -f ~/.$(basename ${0}) ]; then 
	source ~/.$(basename ${0})
else
	echo "Configuration file ~/.${0} not found!"
	usage
fi;


# only 14.04 and 16.04 LTS are supported
if [  \( x = x${1} -o  \( x14.04 != x${1} -a x16.04 != x${1} \) \) ]; then
	echo 1
	usage
fi

# bibigrid images only supported for 14.04
if [ x14.04 = x${1} ]; then 
	if  [  \( x != x${2} -a \( xmaster != x${2} -a xslave != x${2} \) \) ]; then
		echo 2
		usage
	fi
fi

if [ x14.04 = x${1} ]; then
	URL=https://cloud-images.ubuntu.com/trusty/current/trusty-server-cloudimg-amd64-disk1.img

else
	URL=https://cloud-images.ubuntu.com/xenial/current/xenial-server-cloudimg-amd64-disk1.img
fi

BIBIGRID=${2}

IMAGEID=`uuidgen`
DATE=`date +%D`
if [ ${BIBIGRID} ]; then 
	if [ ! -e bibigrid-image ]; then
		echo bibigrid-image not found in cwd. Copy or link bibigrid-image to  \"$(pwd)\".
		exit
	fi
	IMAGE=bibigrid-${1}-${IMAGEID}.img
	RIMAGE="BiBiGrid ${BIBIGRID} ${1} (${DATE})"
else
	IMAGE=ubuntu-${1}-${IMAGEID}.img
	RIMAGE="Ubuntu ${1} LTS (${DATE})"
fi



TMPDIR=/tmp/${USER}/${IMAGEID}
mkdir -p ${TMPDIR} 

log "download cloud image"
wget -O ${TMPDIR}/${IMAGE} ${URL}  

log "image create"
openstack image create --min-disk 5 --min-ram 1024 --disk-format qcow2 --file ${TMPDIR}/${IMAGE} "ib-${IMAGEID}"

log "server create"
ID=$(openstack server create -f value -c id --flavor ${OS_FLAVOR}  --image "ib-${IMAGEID}" --nic net-id=${OS_NET} --key-name ${OS_KEY} --wait "ib-${IMAGEID}")
if [ x = x${IP} ]; then
	log "floating ip create"
	IP=$(openstack floating ip create -f value -c floating_ip_address ${OS_EXTERN})
	IP_DEL=1
else
	log "use env setting for floating ip : ${IP}"
fi
log "floating ip add"
openstack server add floating ip ${ID} ${IP} 
log "configure instance"
check_service ${IP} 22
scp files/dhclient-script-${1}.patch ${IP}:/tmp
ssh ${IP} "sudo patch -p1 /sbin/dhclient-script < /tmp/dhclient-script-${1}.patch"
if [ x16.04 = x${1} ]; then
	scp files/snapd.service.path ${IP}:/tmp
	ssh ${IP} "sudo patch -p1 /lib/systemd/system/snapd.service < /tmp/snapd.service.patch"
fi
if [ x != x${PROXYSERVER} ]; then
	cp files/proxy ${TMPDIR}/proxy
	sed -i s\!\$\{PROXYSERVER\}\!${PROXYSERVER}\! ${TMPDIR}/proxy
	sed -i s\!\$\{PROXYPORT\}\!${PROXYPORT}\! ${TMPDIR}/proxy
	sed -i s\!\$\{HTTP_PROXY\}\!${HTTP_PROXY}\! ${TMPDIR}/proxy
	sed -i s\!\$\{HTTPS_PROXY\}\!${HTTPS_PROXY}\! ${TMPDIR}/proxy
	sed -i s\!\$\{FTP_PROXY\}\!${FTP_PROXY}\! ${TMPDIR}/proxy
	sed -i s\!\$\{NO_PROXY\}\!${NO_PROXY}\! ${TMPDIR}/proxy

	scp ${TMPDIR}/proxy ${IP}:/tmp
	ssh ${IP} "sudo cp /tmp/proxy /etc/dhcp/dhclient-exit-hooks.d/"
fi
if [ ${BIBIGRID} ]; then
	scp bibigrid-image ${IP}:
	ssh ${IP} "sudo /sbin/dhclient -r; sudo /sbin/dhclient"
	sleep 5
	ssh ${IP} "sudo -E ./bibigrid-image --for ${BIBIGRID}"
fi

log "clean up"
ssh ${IP} "rm .ssh/*"
log "server stop"
openstack server stop ${ID}
# wait for server state "SHUTOFF"
state=ACTIVE
while test x${state} != xSHUTOFF; do
	sleep 10
	state=$(openstack server show -f value -c status ${ID})
done
log "server image create (snapshot)"
openstack server image create --name "ib-${IMAGEID}-snapshot" --wait ${ID}
log "server terminate "
openstack server delete ${ID}
if [ x != x${IP_DEL} ]; then
	log "floating ip delete"
	openstack floating ip delete ${IP}
fi
log "download snapshot ..."
openstack image save --file ${TMPDIR}/${IMAGE}.snapshot ib-${IMAGEID}-snapshot
log "... and upload as image"
openstack image create  --min-disk 20 --min-ram 1024 --disk-format qcow2  --file ${TMPDIR}/${IMAGE}.snapshot "${RIMAGE}"
log "image delete (cloud/local)"
openstack image delete "ib-${IMAGEID}"
openstack image delete "ib-${IMAGEID}-snapshot"
rm -r ${TMPDIR}
