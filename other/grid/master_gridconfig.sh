sudo -u sgeadmin qconf -am ubuntu
echo "export SGE_ROOT=/var/lib/gridengine" >> ~/.bashrc
source ~/.bashrc
qconf -au ubuntu users
qconf -Ahgrp hostgroup.conf
qconf -Ap pe.conf
qconf -Aq queue.conf
sudo cp userdata /etc/init.d/
cp add_exec ~/
