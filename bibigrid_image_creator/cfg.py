#!/usr/bin/env python
CFG_APACHE_GANGLIA_CONF='''Alias /ganglia /usr/share/ganglia-webfrontend
'''

CFG_APACHE_SPARK_CONF='''<Location /spark>
        ProxyHTMLLinks a href
        ProxyHTMLLinks area href
        ProxyHTMLLinks link href
        ProxyHTMLLinks img src longdesc usemap
        ProxyHTMLLinks object classid codebase data usemap
        ProxyHTMLLinks q cite
        ProxyHTMLLinks blockquote cite
        ProxyHTMLLinks ins cite
        ProxyHTMLLinks del cite
        ProxyHTMLLinks form action
        ProxyHTMLLinks input src usemap
        ProxyHTMLLinks head profile
        ProxyHTMLLinks base href
        ProxyHTMLLinks script src for
        ProxyHTMLLinks meta content
        
        ProxyHTMLEvents onclick ondblclick onmousedown onmouseup \
            onmouseover onmousemove onmouseout onkeypress \
            onkeydown onkeyup onfocus onblur onload \
            onunload onsubmit onreset onselect onchange
        
        ProxyPass http://localhost:8080
        ProxyPassReverse http://localhost:8080
        ProxyHTMLEnable On
        ProxyHTMLExtended On
        SetOutputFilter INFLATE;proxy-html;DEFLATE;     
        ProxyHTMLURLMap http://localhost:8080 /spark
</Location>
'''
CFG_APACHE_HDFS_CONF='''<Location /hdfs>
        ProxyHTMLLinks a href
        ProxyHTMLLinks area href
        ProxyHTMLLinks link href
        ProxyHTMLLinks img src longdesc usemap
        ProxyHTMLLinks object classid codebase data usemap
        ProxyHTMLLinks q cite
        ProxyHTMLLinks blockquote cite
        ProxyHTMLLinks ins cite
        ProxyHTMLLinks del cite
        ProxyHTMLLinks form action
        ProxyHTMLLinks input src usemap
        ProxyHTMLLinks head profile
        ProxyHTMLLinks base href
        ProxyHTMLLinks script src for
        ProxyHTMLLinks meta content
        
        ProxyHTMLEvents onclick ondblclick onmousedown onmouseup \
            onmouseover onmousemove onmouseout onkeypress \
            onkeydown onkeyup onfocus onblur onload \
            onunload onsubmit onreset onselect onchange
        
        ProxyPass http://localhost:50070
        ProxyPassReverse http://localhost:50070
        ProxyHTMLEnable On
        ProxyHTMLExtended On
        SetOutputFilter INFLATE;proxy-html;DEFLATE;     
        ProxyHTMLURLMap http://localhost:50070 /hdfs
</Location>
'''

CFG_APACHE_MESOS_CONF='''<Location /mesos>
        ProxyHTMLLinks a href
        ProxyHTMLLinks area href
        ProxyHTMLLinks link href
        ProxyHTMLLinks img src longdesc usemap
        ProxyHTMLLinks object classid codebase data usemap
        ProxyHTMLLinks q cite
        ProxyHTMLLinks blockquote cite
        ProxyHTMLLinks ins cite
        ProxyHTMLLinks del cite
        ProxyHTMLLinks form action
        ProxyHTMLLinks input src usemap
        ProxyHTMLLinks head profile
        ProxyHTMLLinks base href
        ProxyHTMLLinks script src for
        ProxyHTMLLinks meta content
        
        ProxyHTMLEvents onclick ondblclick onmousedown onmouseup \
            onmouseover onmousemove onmouseout onkeypress \
            onkeydown onkeyup onfocus onblur onload \
            onunload onsubmit onreset onselect onchange
        
        ProxyPass http://localhost:5050
        ProxyPassReverse http://localhost:5050
        ProxyHTMLEnable On
        ProxyHTMLExtended On
        SetOutputFilter INFLATE;proxy-html;DEFLATE;     
        ProxyHTMLURLMap http://localhost:5050 /mesos
</Location>
'''

CFG_APACHE_RESULT_CONF='''
<Directory /vol/spool/www>
        Options Indexes FollowSymLinks
        AllowOverride None
        Require all granted
</Directory>

Alias /result /vol/spool/www
'''


CFG_DEFAULT_LOCALE='''LANG="en_US.utf8"
'''


CFG_HOSTS_ALLOW='''rpcbind mountd nfsd statd lockd rquotad : ALL
'''

CFG_SCHEDULE_CONF='''algorithm                         default
schedule_interval                 0:0:15
maxujobs                          0
queue_sort_method                 load
job_load_adjustments              NONE
load_adjustment_decay_time        0
load_formula                      slots
schedd_job_info                   false
flush_submit_sec                  1
flush_finish_sec                  1
params                            none
reprioritize_interval             0:0:0
halftime                          168
usage_weight_list                 cpu=1.000000,mem=0.000000,io=0.000000
compensation_factor               5.000000
weight_user                       0.250000
weight_project                    0.250000
weight_department                 0.250000
weight_job                        0.250000
weight_tickets_functional         0
weight_tickets_share              0
share_override_tickets            TRUE
share_functional_shares           TRUE
max_functional_jobs_to_schedule   200
report_pjob_tickets               FALSE
max_pending_tasks_per_job         50
halflife_decay_list               none
policy_hierarchy                  OFS
weight_ticket                     0.000000
weight_waiting_time               0.000000
weight_deadline                   0.000000
weight_urgency                    0.000000
weight_priority                   0.000000
max_reservation                   0
default_duration                  INFINITY
'''

CFG_SGE_CONF='''#global:
execd_spool_dir              /var/spool/gridengine/execd
mailer                       /usr/bin/mail
xterm                        /usr/bin/xterm
load_sensor                  none
prolog                       none
epilog                       none
shell_start_mode             posix_compliant
login_shells                 bash,sh,ksh,csh,tcsh
min_uid                      0
min_gid                      0
user_lists                   none
xuser_lists                  none
projects                     none
xprojects                    none
enforce_project              false
enforce_user                 auto
load_report_time             00:00:40
max_unheard                  00:05:00
reschedule_unknown           00:00:00
loglevel                     log_warning
administrator_mail           root
set_token_cmd                none
pag_cmd                      none
token_extend_time            none
shepherd_cmd                 none
qmaster_params               none
execd_params                 none
reporting_params             accounting=true reporting=false \
                             flush_time=00:00:15 joblog=false sharelog=00:00:00
finished_jobs                0
gid_range                    65400-65500
max_aj_instances             2000
max_aj_tasks                 75000
max_u_jobs                   0
max_jobs                     0
auto_user_oticket            0
auto_user_fshare             0
auto_user_default_project    none
auto_user_delete_time        86400
delegated_file_staging       false
reprioritize                 0
rlogin_daemon                /usr/sbin/sshd -i
rlogin_command               /usr/bin/ssh
qlogin_daemon                /usr/sbin/sshd -i
qlogin_command               /usr/share/gridengine/qlogin-wrapper
rsh_daemon                   /usr/sbin/sshd -i
rsh_command                  /usr/bin/ssh
jsv_url                      none
jsv_allowed_mod              ac,h,i,e,o,j,M,N,p,w
'''

CFG_ADD_EXEC='''#!/bin/bash

if [ $# -ne 2 ] ; then 
    echo "usage:: $0 <hostname> $1 <cores>"; 
    exit; 
fi;

echo "add '$1' as exec host"

# create simple configuration file
echo -e "hostname              $1 
load_scaling          NONE
complex_values        NONE
user_lists            NONE
xuser_lists           NONE
projects              NONE
xprojects             NONE
usage_scaling         NONE
report_variables      NONE" > /tmp/$1.cfg

# add $1 as execution host using previous configuration
qconf -Ae /tmp/$1.cfg

# add $1 to hostgroup @allhosts
qconf -aattr hostgroup hostlist $1 @allhosts
qconf -aattr queue slots '['$1'='$2']' main.q
'''


CFG_HOSTGROUP_CONF='''group_name @allhosts
hostlist NONE
'''


CFG_PE_CONF='''pe_name            multislot
slots              100000
user_lists         NONE
xuser_lists        NONE
start_proc_args    /bin/true
stop_proc_args     /bin/true
allocation_rule    $pe_slots
control_slaves     TRUE
job_is_first_task  FALSE
urgency_slots      max
accounting_summary TRUE
'''


CFG_QUEUE_CONF='''qname                 main.q
hostlist              @allhosts
seq_no                0
load_thresholds       NONE
suspend_thresholds    NONE
nsuspend              1
suspend_interval      00:05:00
priority              0
min_cpu_interval      00:05:00
processors            UNDEFINED
qtype                 BATCH INTERACTIVE
ckpt_list             NONE
pe_list               multislot make
rerun                 FALSE
slots                 1
tmpdir                /tmp
shell                 /bin/sh
prolog                NONE
epilog                NONE
shell_start_mode      posix_compliant
starter_method        NONE
suspend_method        NONE
resume_method         NONE
terminate_method      NONE
notify                00:00:60
owner_list            NONE
user_lists            NONE
xuser_lists           NONE
subordinate_list      NONE
complex_values        NONE
projects              NONE
xprojects             NONE
calendar              NONE
initial_state         default
s_rt                  INFINITY
h_rt                  INFINITY
s_cpu                 INFINITY
h_cpu                 INFINITY
s_fsize               INFINITY
h_fsize               INFINITY
s_data                INFINITY
h_data                INFINITY
s_stack               INFINITY
h_stack               INFINITY
s_core                INFINITY
h_core                INFINITY
s_rss                 INFINITY
h_rss                 INFINITY
s_vmem                INFINITY
h_vmem                INFINITY
'''


CFG_USERDATA='''
#!/bin/sh
case "$1" in
start)  date >> /var/log/userdata.log 
    (/usr/bin/curl http://169.254.169.254/latest/user-data | /bin/bash - ) 2>\&1 >> /var/log/userdata.log
    ;;
*)  echo "Usage: $0 {start}"
    exit 1 ;;
esac
'''


CFG_GMETAD_CONF='''data_source "BiBiGrid" localhost
gridname "BiBiGrid"
setuid_username "ganglia"
case_sensitive_hostnames 1
'''


CFG_GMOND_CONF_MASTER='''/* This configuration is as close to 2.5.x default behavior as possible 
   The values closely match ./gmond/metric.h definitions in 2.5.x */ 
globals {                    
  daemonize = yes              
  setuid = yes             
  user = ganglia              
  debug_level = 0               
  max_udp_msg_len = 1472        
  mute = no             
  deaf = no             
  host_dmax = 0 /*secs */ 
  cleanup_threshold = 300 /*secs */ 
  gexec = no             
  send_metadata_interval = 30     
} 

/* If a cluster attribute is specified, then all gmond hosts are wrapped inside 
 * of a <CLUSTER> tag.  If you do not specify a cluster tag, then all <HOSTS> will 
 * NOT be wrapped inside of a <CLUSTER> tag. */ 
cluster { 
  name = "BiBiGrid" 
  owner = "BiBiCloud" 
  latlong = "unspecified" 
  url = "unspecified" 
} 

/* The host section describes attributes of the host, like the location */ 
host { 
  location = "unspecified" 
} 

/* Feel free to specify as many udp_send_channels as you like.  Gmond 
   used to only support having a single channel */ 
udp_send_channel { 
  #mcast_join = 239.2.11.71 
  host = MASTER_IP
  port = 8649 
  ttl = 1 
} 

/* You can specify as many udp_recv_channels as you like as well. */ 
udp_recv_channel { 
  #mcast_join = 239.2.11.71 
  port = 8649 
  #bind = 239.2.11.71 
} 

/* You can specify as many tcp_accept_channels as you like to share 
   an xml description of the state of the cluster */ 
tcp_accept_channel { 
  port = 8649 
} 

/* Each metrics module that is referenced by gmond must be specified and 
   loaded. If the module has been statically linked with gmond, it does not 
   require a load path. However all dynamically loadable modules must include 
   a load path. */ 
modules { 
  module { 
    name = "core_metrics" 
  } 
  module { 
    name = "cpu_module" 
    path = "/usr/lib/ganglia/modcpu.so" 
  } 
  module { 
    name = "disk_module" 
    path = "/usr/lib/ganglia/moddisk.so" 
  } 
  module { 
    name = "load_module" 
    path = "/usr/lib/ganglia/modload.so" 
  } 
  module { 
    name = "mem_module" 
    path = "/usr/lib/ganglia/modmem.so" 
  } 
  module { 
    name = "net_module" 
    path = "/usr/lib/ganglia/modnet.so" 
  } 
  module { 
    name = "proc_module" 
    path = "/usr/lib/ganglia/modproc.so" 
  } 
  module { 
    name = "sys_module" 
    path = "/usr/lib/ganglia/modsys.so" 
  } 
} 

include ('/etc/ganglia/conf.d/*.conf') 


/* The old internal 2.5.x metric array has been replaced by the following 
   collection_group directives.  What follows is the default behavior for 
   collecting and sending metrics that is as close to 2.5.x behavior as 
   possible. */

/* This collection group will cause a heartbeat (or beacon) to be sent every 
   20 seconds.  In the heartbeat is the GMOND_STARTED data which expresses 
   the age of the running gmond. */ 
collection_group { 
  collect_once = yes 
  time_threshold = 20 
  metric { 
    name = "heartbeat" 
  } 
} 

/* This collection group will send general info about this host every 1200 secs. 
   This information doesn't change between reboots and is only collected once. */ 
collection_group { 
  collect_once = yes 
  time_threshold = 1200 
  metric { 
    name = "cpu_num" 
    title = "CPU Count" 
  } 
  metric { 
    name = "cpu_speed" 
    title = "CPU Speed" 
  } 
  metric { 
    name = "mem_total" 
    title = "Memory Total" 
  } 
  /* Should this be here? Swap can be added/removed between reboots. */ 
  metric { 
    name = "swap_total" 
    title = "Swap Space Total" 
  } 
  metric { 
    name = "boottime" 
    title = "Last Boot Time" 
  } 
  metric { 
    name = "machine_type" 
    title = "Machine Type" 
  } 
  metric { 
    name = "os_name" 
    title = "Operating System" 
  } 
  metric { 
    name = "os_release" 
    title = "Operating System Release" 
  } 
  metric { 
    name = "location" 
    title = "Location" 
  } 
} 

/* This collection group will send the status of gexecd for this host every 300 secs */
/* Unlike 2.5.x the default behavior is to report gexecd OFF.  */ 
collection_group { 
  collect_once = yes 
  time_threshold = 300 
  metric { 
    name = "gexec" 
    title = "Gexec Status" 
  } 
} 

/* This collection group will collect the CPU status info every 20 secs. 
   The time threshold is set to 90 seconds.  In honesty, this time_threshold could be 
   set significantly higher to reduce unneccessary network chatter. */ 
collection_group { 
  collect_every = 20 
  time_threshold = 90 
  /* CPU status */ 
  metric { 
    name = "cpu_user"  
    value_threshold = "1.0" 
    title = "CPU User" 
  } 
  metric { 
    name = "cpu_system"   
    value_threshold = "1.0" 
    title = "CPU System" 
  } 
  metric { 
    name = "cpu_idle"  
    value_threshold = "5.0" 
    title = "CPU Idle" 
  } 
  metric { 
    name = "cpu_nice"  
    value_threshold = "1.0" 
    title = "CPU Nice" 
  } 
  metric { 
    name = "cpu_aidle" 
    value_threshold = "5.0" 
    title = "CPU aidle" 
  } 
  metric { 
    name = "cpu_wio" 
    value_threshold = "1.0" 
    title = "CPU wio" 
  } 
  /* The next two metrics are optional if you want more detail... 
     ... since they are accounted for in cpu_system.  
  metric { 
    name = "cpu_intr" 
    value_threshold = "1.0" 
    title = "CPU intr" 
  } 
  metric { 
    name = "cpu_sintr" 
    value_threshold = "1.0" 
    title = "CPU sintr" 
  } 
  */ 
} 

collection_group { 
  collect_every = 20 
  time_threshold = 90 
  /* Load Averages */ 
  metric { 
    name = "load_one" 
    value_threshold = "1.0" 
    title = "One Minute Load Average" 
  } 
  metric { 
    name = "load_five" 
    value_threshold = "1.0" 
    title = "Five Minute Load Average" 
  } 
  metric { 
    name = "load_fifteen" 
    value_threshold = "1.0" 
    title = "Fifteen Minute Load Average" 
  }
} 

/* This group collects the number of running and total processes */ 
collection_group { 
  collect_every = 80 
  time_threshold = 950 
  metric { 
    name = "proc_run" 
    value_threshold = "1.0" 
    title = "Total Running Processes" 
  } 
  metric { 
    name = "proc_total" 
    value_threshold = "1.0" 
    title = "Total Processes" 
  } 
}

/* This collection group grabs the volatile memory metrics every 40 secs and 
   sends them at least every 180 secs.  This time_threshold can be increased 
   significantly to reduce unneeded network traffic. */ 
collection_group { 
  collect_every = 40 
  time_threshold = 180 
  metric { 
    name = "mem_free" 
    value_threshold = "1024.0" 
    title = "Free Memory" 
  } 
  metric { 
    name = "mem_shared" 
    value_threshold = "1024.0" 
    title = "Shared Memory" 
  } 
  metric { 
    name = "mem_buffers" 
    value_threshold = "1024.0" 
    title = "Memory Buffers" 
  } 
  metric { 
    name = "mem_cached" 
    value_threshold = "1024.0" 
    title = "Cached Memory" 
  } 
  metric { 
    name = "swap_free" 
    value_threshold = "1024.0" 
    title = "Free Swap Space" 
  } 
} 

collection_group { 
  collect_every = 40 
  time_threshold = 300 
  metric { 
    name = "bytes_out" 
    value_threshold = 4096 
    title = "Bytes Sent" 
  } 
  metric { 
    name = "bytes_in" 
    value_threshold = 4096 
    title = "Bytes Received" 
  } 
  metric { 
    name = "pkts_in" 
    value_threshold = 256 
    title = "Packets Received" 
  } 
  metric { 
    name = "pkts_out" 
    value_threshold = 256 
    title = "Packets Sent" 
  } 
}

/* Different than 2.5.x default since the old config made no sense */ 
collection_group { 
  collect_every = 1800 
  time_threshold = 3600 
  metric { 
    name = "disk_total" 
    value_threshold = 1.0 
    title = "Total Disk Space" 
  } 
}

collection_group { 
  collect_every = 40 
  time_threshold = 180 
  metric { 
    name = "disk_free" 
    value_threshold = 1.0 
    title = "Disk Space Available" 
  } 
  metric { 
    name = "part_max_used" 
    value_threshold = 1.0 
    title = "Maximum Disk Space Used" 
  } 
}
'''









CFG_GMOND_CONF_SLAVE='''/* This configuration is as close to 2.5.x default behavior as possible 
   The values closely match ./gmond/metric.h definitions in 2.5.x */ 
globals {                    
  daemonize = yes              
  setuid = yes             
  user = ganglia              
  debug_level = 0               
  max_udp_msg_len = 1472        
  mute = no             
  deaf = yes             
  host_dmax = 0 /*secs */ 
  cleanup_threshold = 300 /*secs */ 
  gexec = no             
  send_metadata_interval = 30     
} 

/* If a cluster attribute is specified, then all gmond hosts are wrapped inside 
 * of a <CLUSTER> tag.  If you do not specify a cluster tag, then all <HOSTS> will 
 * NOT be wrapped inside of a <CLUSTER> tag. */ 
cluster { 
  name = "BiBiGrid" 
  owner = "BiBiCloud" 
  latlong = "unspecified" 
  url = "unspecified" 
} 

/* The host section describes attributes of the host, like the location */ 
host { 
  location = "unspecified" 
} 

/* Feel free to specify as many udp_send_channels as you like.  Gmond 
   used to only support having a single channel */ 
udp_send_channel { 
  #mcast_join = 239.2.11.71 
  host = MASTER_IP
  port = 8649 
  ttl = 1 
} 

/* You can specify as many udp_recv_channels as you like as well. */ 
udp_recv_channel { 
  #mcast_join = 239.2.11.71 
  #port = 8649 
  #bind = 239.2.11.71 
} 

/* You can specify as many tcp_accept_channels as you like to share 
   an xml description of the state of the cluster */ 
tcp_accept_channel { 
  port = 8649 
} 

/* Each metrics module that is referenced by gmond must be specified and 
   loaded. If the module has been statically linked with gmond, it does not 
   require a load path. However all dynamically loadable modules must include 
   a load path. */ 
modules { 
  module { 
    name = "core_metrics" 
  } 
  module { 
    name = "cpu_module" 
    path = "/usr/lib/ganglia/modcpu.so" 
  } 
  module { 
    name = "disk_module" 
    path = "/usr/lib/ganglia/moddisk.so" 
  } 
  module { 
    name = "load_module" 
    path = "/usr/lib/ganglia/modload.so" 
  } 
  module { 
    name = "mem_module" 
    path = "/usr/lib/ganglia/modmem.so" 
  } 
  module { 
    name = "net_module" 
    path = "/usr/lib/ganglia/modnet.so" 
  } 
  module { 
    name = "proc_module" 
    path = "/usr/lib/ganglia/modproc.so" 
  } 
  module { 
    name = "sys_module" 
    path = "/usr/lib/ganglia/modsys.so" 
  } 
} 

include ('/etc/ganglia/conf.d/*.conf') 


/* The old internal 2.5.x metric array has been replaced by the following 
   collection_group directives.  What follows is the default behavior for 
   collecting and sending metrics that is as close to 2.5.x behavior as 
   possible. */

/* This collection group will cause a heartbeat (or beacon) to be sent every 
   20 seconds.  In the heartbeat is the GMOND_STARTED data which expresses 
   the age of the running gmond. */ 
collection_group { 
  collect_once = yes 
  time_threshold = 20 
  metric { 
    name = "heartbeat" 
  } 
} 

/* This collection group will send general info about this host every 1200 secs. 
   This information doesn't change between reboots and is only collected once. */ 
collection_group { 
  collect_once = yes 
  time_threshold = 1200 
  metric { 
    name = "cpu_num" 
    title = "CPU Count" 
  } 
  metric { 
    name = "cpu_speed" 
    title = "CPU Speed" 
  } 
  metric { 
    name = "mem_total" 
    title = "Memory Total" 
  } 
  /* Should this be here? Swap can be added/removed between reboots. */ 
  metric { 
    name = "swap_total" 
    title = "Swap Space Total" 
  } 
  metric { 
    name = "boottime" 
    title = "Last Boot Time" 
  } 
  metric { 
    name = "machine_type" 
    title = "Machine Type" 
  } 
  metric { 
    name = "os_name" 
    title = "Operating System" 
  } 
  metric { 
    name = "os_release" 
    title = "Operating System Release" 
  } 
  metric { 
    name = "location" 
    title = "Location" 
  } 
} 

/* This collection group will send the status of gexecd for this host every 300 secs */
/* Unlike 2.5.x the default behavior is to report gexecd OFF.  */ 
collection_group { 
  collect_once = yes 
  time_threshold = 300 
  metric { 
    name = "gexec" 
    title = "Gexec Status" 
  } 
} 

/* This collection group will collect the CPU status info every 20 secs. 
   The time threshold is set to 90 seconds.  In honesty, this time_threshold could be 
   set significantly higher to reduce unneccessary network chatter. */ 
collection_group { 
  collect_every = 20 
  time_threshold = 90 
  /* CPU status */ 
  metric { 
    name = "cpu_user"  
    value_threshold = "1.0" 
    title = "CPU User" 
  } 
  metric { 
    name = "cpu_system"   
    value_threshold = "1.0" 
    title = "CPU System" 
  } 
  metric { 
    name = "cpu_idle"  
    value_threshold = "5.0" 
    title = "CPU Idle" 
  } 
  metric { 
    name = "cpu_nice"  
    value_threshold = "1.0" 
    title = "CPU Nice" 
  } 
  metric { 
    name = "cpu_aidle" 
    value_threshold = "5.0" 
    title = "CPU aidle" 
  } 
  metric { 
    name = "cpu_wio" 
    value_threshold = "1.0" 
    title = "CPU wio" 
  } 
  /* The next two metrics are optional if you want more detail... 
     ... since they are accounted for in cpu_system.  
  metric { 
    name = "cpu_intr" 
    value_threshold = "1.0" 
    title = "CPU intr" 
  } 
  metric { 
    name = "cpu_sintr" 
    value_threshold = "1.0" 
    title = "CPU sintr" 
  } 
  */ 
} 

collection_group { 
  collect_every = 20 
  time_threshold = 90 
  /* Load Averages */ 
  metric { 
    name = "load_one" 
    value_threshold = "1.0" 
    title = "One Minute Load Average" 
  } 
  metric { 
    name = "load_five" 
    value_threshold = "1.0" 
    title = "Five Minute Load Average" 
  } 
  metric { 
    name = "load_fifteen" 
    value_threshold = "1.0" 
    title = "Fifteen Minute Load Average" 
  }
} 

/* This group collects the number of running and total processes */ 
collection_group { 
  collect_every = 80 
  time_threshold = 950 
  metric { 
    name = "proc_run" 
    value_threshold = "1.0" 
    title = "Total Running Processes" 
  } 
  metric { 
    name = "proc_total" 
    value_threshold = "1.0" 
    title = "Total Processes" 
  } 
}

/* This collection group grabs the volatile memory metrics every 40 secs and 
   sends them at least every 180 secs.  This time_threshold can be increased 
   significantly to reduce unneeded network traffic. */ 
collection_group { 
  collect_every = 40 
  time_threshold = 180 
  metric { 
    name = "mem_free" 
    value_threshold = "1024.0" 
    title = "Free Memory" 
  } 
  metric { 
    name = "mem_shared" 
    value_threshold = "1024.0" 
    title = "Shared Memory" 
  } 
  metric { 
    name = "mem_buffers" 
    value_threshold = "1024.0" 
    title = "Memory Buffers" 
  } 
  metric { 
    name = "mem_cached" 
    value_threshold = "1024.0" 
    title = "Cached Memory" 
  } 
  metric { 
    name = "swap_free" 
    value_threshold = "1024.0" 
    title = "Free Swap Space" 
  } 
} 

collection_group { 
  collect_every = 40 
  time_threshold = 300 
  metric { 
    name = "bytes_out" 
    value_threshold = 4096 
    title = "Bytes Sent" 
  } 
  metric { 
    name = "bytes_in" 
    value_threshold = 4096 
    title = "Bytes Received" 
  } 
  metric { 
    name = "pkts_in" 
    value_threshold = 256 
    title = "Packets Received" 
  } 
  metric { 
    name = "pkts_out" 
    value_threshold = 256 
    title = "Packets Sent" 
  } 
}

/* Different than 2.5.x default since the old config made no sense */ 
collection_group { 
  collect_every = 1800 
  time_threshold = 3600 
  metric { 
    name = "disk_total" 
    value_threshold = 1.0 
    title = "Total Disk Space" 
  } 
}

collection_group { 
  collect_every = 40 
  time_threshold = 180 
  metric { 
    name = "disk_free" 
    value_threshold = 1.0 
    title = "Disk Space Available" 
  } 
  metric { 
    name = "part_max_used" 
    value_threshold = 1.0 
    title = "Maximum Disk Space Used" 
  } 
}
'''
CFG_CASSANDRA='''# Cassandra storage config YAML 

# NOTE:
#   See http://wiki.apache.org/cassandra/StorageConfiguration for
#   full explanations of configuration directives
# /NOTE

# The name of the cluster. This is mainly used to prevent machines in
# one logical cluster from joining another.
cluster_name: 'my_cluster'

# This defines the number of tokens randomly assigned to this node on the ring
# The more tokens, relative to other nodes, the larger the proportion of data
# that this node will store. You probably want all nodes to have the same number
# of tokens assuming they have equal hardware capability.
#
# If you leave this unspecified, Cassandra will use the default of 1 token for legacy compatibility,
# and will use the initial_token as described below.
#
# Specifying initial_token will override this setting.
#
# If you already have a cluster with 1 token per node, and wish to migrate to 
# multiple tokens per node, see http://wiki.apache.org/cassandra/Operations
num_tokens: ##NUM_TOKEN##

# initial_token allows you to specify tokens manually.  While you can use # it with
# vnodes (num_tokens > 1, above) -- in which case you should provide a 
# comma-separated list -- it's primarily used when adding nodes # to legacy clusters 
# that do not have vnodes enabled.
# initial_token:

# See http://wiki.apache.org/cassandra/HintedHandoff
hinted_handoff_enabled: true
# this defines the maximum amount of time a dead host will have hints
# generated.  After it has been dead this long, new hints for it will not be
# created until it has been seen alive and gone down again.
max_hint_window_in_ms: 10800000 # 3 hours
# Maximum throttle in KBs per second, per delivery thread.  This will be
# reduced proportionally to the number of nodes in the cluster.  (If there
# are two nodes in the cluster, each delivery thread will use the maximum
# rate; if there are three, each will throttle to half of the maximum,
# since we expect two nodes to be delivering hints simultaneously.)
hinted_handoff_throttle_in_kb: 1024
# Number of threads with which to deliver hints;
# Consider increasing this number when you have multi-dc deployments, since
# cross-dc handoff tends to be slower
max_hints_delivery_threads: 2

# The following setting populates the page cache on memtable flush and compaction
# WARNING: Enable this setting only when the whole node's data fits in memory.
# Defaults to: false
# populate_io_cache_on_flush: false

# Authentication backend, implementing IAuthenticator; used to identify users
# Out of the box, Cassandra provides org.apache.cassandra.auth.{AllowAllAuthenticator,
# PasswordAuthenticator}.
#
# - AllowAllAuthenticator performs no checks - set it to disable authentication.
# - PasswordAuthenticator relies on username/password pairs to authenticate
#   users. It keeps usernames and hashed passwords in system_auth.credentials table.
#   Please increase system_auth keyspace replication factor if you use this authenticator.
authenticator: AllowAllAuthenticator

# Authorization backend, implementing IAuthorizer; used to limit access/provide permissions
# Out of the box, Cassandra provides org.apache.cassandra.auth.{AllowAllAuthorizer,
# CassandraAuthorizer}.
#
# - AllowAllAuthorizer allows any action to any user - set it to disable authorization.
# - CassandraAuthorizer stores permissions in system_auth.permissions table. Please
#   increase system_auth keyspace replication factor if you use this authorizer.
authorizer: AllowAllAuthorizer

# Validity period for permissions cache (fetching permissions can be an
# expensive operation depending on the authorizer, CassandraAuthorizer is
# one example). Defaults to 2000, set to 0 to disable.
# Will be disabled automatically for AllowAllAuthorizer.
permissions_validity_in_ms: 2000

# The partitioner is responsible for distributing rows (by key) across
# nodes in the cluster.  Any IPartitioner may be used, including your
# own as long as it is on the classpath.  Out of the box, Cassandra
# provides org.apache.cassandra.dht.{Murmur3Partitioner, RandomPartitioner
# ByteOrderedPartitioner, OrderPreservingPartitioner (deprecated)}.
# 
# - RandomPartitioner distributes rows across the cluster evenly by md5.
#   This is the default prior to 1.2 and is retained for compatibility.
# - Murmur3Partitioner is similar to RandomPartioner but uses Murmur3_128
#   Hash Function instead of md5.  When in doubt, this is the best option.
# - ByteOrderedPartitioner orders rows lexically by key bytes.  BOP allows
#   scanning rows in key order, but the ordering can generate hot spots
#   for sequential insertion workloads.
# - OrderPreservingPartitioner is an obsolete form of BOP, that stores
# - keys in a less-efficient format and only works with keys that are
#   UTF8-encoded Strings.
# - CollatingOPP collates according to EN,US rules rather than lexical byte
#   ordering.  Use this as an example if you need custom collation.
#
# See http://wiki.apache.org/cassandra/Operations for more on
# partitioners and token selection.
partitioner: org.apache.cassandra.dht.Murmur3Partitioner

# Directories where Cassandra should store data on disk.  Cassandra
# will spread data evenly across them, subject to the granularity of
# the configured compaction strategy.
data_file_directories:
    - /vol/scratch/cassandra/data

# commit log
commitlog_directory: /vol/scratch/cassandra/commitlog

# policy for data disk failures:
# stop: shut down gossip and Thrift, leaving the node effectively dead, but
#       can still be inspected via JMX.
# best_effort: stop using the failed disk and respond to requests based on
#              remaining available sstables.  This means you WILL see obsolete
#              data at CL.ONE!
# ignore: ignore fatal errors and let requests fail, as in pre-1.2 Cassandra
disk_failure_policy: stop

# Maximum size of the key cache in memory.
#
# Each key cache hit saves 1 seek and each row cache hit saves 2 seeks at the
# minimum, sometimes more. The key cache is fairly tiny for the amount of
# time it saves, so it's worthwhile to use it at large numbers.
# The row cache saves even more time, but must contain the entire row,
# so it is extremely space-intensive. It's best to only use the
# row cache if you have hot rows or static rows.
#
# NOTE: if you reduce the size, you may not get you hottest keys loaded on startup.
#
# Default value is empty to make it "auto" (min(5% of Heap (in MB), 100MB)). Set to 0 to disable key cache.
key_cache_size_in_mb:

# Duration in seconds after which Cassandra should
# save the key cache. Caches are saved to saved_caches_directory as
# specified in this configuration file.
#
# Saved caches greatly improve cold-start speeds, and is relatively cheap in
# terms of I/O for the key cache. Row cache saving is much more expensive and
# has limited use.
#
# Default is 14400 or 4 hours.
key_cache_save_period: 14400

# Number of keys from the key cache to save
# Disabled by default, meaning all keys are going to be saved
# key_cache_keys_to_save: 100

# Maximum size of the row cache in memory.
# NOTE: if you reduce the size, you may not get you hottest keys loaded on startup.
#
# Default value is 0, to disable row caching.
row_cache_size_in_mb: 0

# Duration in seconds after which Cassandra should
# safe the row cache. Caches are saved to saved_caches_directory as specified
# in this configuration file.
#
# Saved caches greatly improve cold-start speeds, and is relatively cheap in
# terms of I/O for the key cache. Row cache saving is much more expensive and
# has limited use.
#
# Default is 0 to disable saving the row cache.
row_cache_save_period: 0

# Number of keys from the row cache to save
# Disabled by default, meaning all keys are going to be saved
# row_cache_keys_to_save: 100

# The off-heap memory allocator.  Affects storage engine metadata as
# well as caches.  Experiments show that JEMAlloc saves some memory
# than the native GCC allocator (i.e., JEMalloc is more
# fragmentation-resistant).
# 
# Supported values are: NativeAllocator, JEMallocAllocator
#
# If you intend to use JEMallocAllocator you have to install JEMalloc as library and
# modify cassandra-env.sh as directed in the file.
#
# Defaults to NativeAllocator
# memory_allocator: NativeAllocator

# saved caches
saved_caches_directory: /vol/scratch/cassandra/saved_caches

# commitlog_sync may be either "periodic" or "batch." 
# When in batch mode, Cassandra won't ack writes until the commit log
# has been fsynced to disk.  It will wait up to
# commitlog_sync_batch_window_in_ms milliseconds for other writes, before
# performing the sync.
#
# commitlog_sync: batch
# commitlog_sync_batch_window_in_ms: 50
#
# the other option is "periodic" where writes may be acked immediately
# and the CommitLog is simply synced every commitlog_sync_period_in_ms
# milliseconds.  By default this allows 1024*(CPU cores) pending
# entries on the commitlog queue.  If you are writing very large blobs,
# you should reduce that; 16*cores works reasonably well for 1MB blobs.
# It should be at least as large as the concurrent_writes setting.
commitlog_sync: periodic
commitlog_sync_period_in_ms: 10000
# commitlog_periodic_queue_size:

# The size of the individual commitlog file segments.  A commitlog
# segment may be archived, deleted, or recycled once all the data
# in it (potentially from each columnfamily in the system) has been
# flushed to sstables.  
#
# The default size is 32, which is almost always fine, but if you are
# archiving commitlog segments (see commitlog_archiving.properties),
# then you probably want a finer granularity of archiving; 8 or 16 MB
# is reasonable.
commitlog_segment_size_in_mb: 32

# any class that implements the SeedProvider interface and has a
# constructor that takes a Map<String, String> of parameters will do.
seed_provider:
    # Addresses of hosts that are deemed contact points. 
    # Cassandra nodes use this list of hosts to find each other and learn
    # the topology of the ring.  You must change this if you are running
    # multiple nodes!
    - class_name: org.apache.cassandra.locator.SimpleSeedProvider
      parameters:
          # seeds is actually a comma-delimited list of addresses.
          # Ex: "<ip1>,<ip2>,<ip3>"
          - seeds: "##MASTER_IP##"

# For workloads with more data than can fit in memory, Cassandra's
# bottleneck will be reads that need to fetch data from
# disk. "concurrent_reads" should be set to (16 * number_of_drives) in
# order to allow the operations to enqueue low enough in the stack
# that the OS and drives can reorder them.
#
# On the other hand, since writes are almost never IO bound, the ideal
# number of "concurrent_writes" is dependent on the number of cores in
# your system; (8 * number_of_cores) is a good rule of thumb.
concurrent_reads: 32
concurrent_writes: 32

# Total memory to use for sstable-reading buffers.  Defaults to
# the smaller of 1/4 of heap or 512MB.
# file_cache_size_in_mb: 512

# Total memory to use for memtables.  Cassandra will flush the largest
# memtable when this much memory is used.
# If omitted, Cassandra will set it to 1/3 of the heap.
# memtable_total_space_in_mb: 2048

# Total space to use for commitlogs.  Since commitlog segments are
# mmapped, and hence use up address space, the default size is 32
# on 32-bit JVMs, and 1024 on 64-bit JVMs.
#
# If space gets above this value (it will round up to the next nearest
# segment multiple), Cassandra will flush every dirty CF in the oldest
# segment and remove it.  So a small total commitlog space will tend
# to cause more flush activity on less-active columnfamilies.
# commitlog_total_space_in_mb: 4096

# This sets the amount of memtable flush writer threads.  These will
# be blocked by disk io, and each one will hold a memtable in memory
# while blocked. If you have a large heap and many data directories,
# you can increase this value for better flush performance.
# By default this will be set to the amount of data directories defined.
#memtable_flush_writers: 1

# the number of full memtables to allow pending flush, that is,
# waiting for a writer thread.  At a minimum, this should be set to
# the maximum number of secondary indexes created on a single CF.
memtable_flush_queue_size: 4

# Whether to, when doing sequential writing, fsync() at intervals in
# order to force the operating system to flush the dirty
# buffers. Enable this to avoid sudden dirty buffer flushing from
# impacting read latencies. Almost always a good idea on SSDs; not
# necessarily on platters.
trickle_fsync: false
trickle_fsync_interval_in_kb: 10240

# TCP port, for commands and data
storage_port: 7000

# SSL port, for encrypted communication.  Unused unless enabled in
# encryption_options
ssl_storage_port: 7001

# Address to bind to and tell other Cassandra nodes to connect to. You
# _must_ change this if you want multiple nodes to be able to
# communicate!
# 
# Leaving it blank leaves it up to InetAddress.getLocalHost(). This
# will always do the Right Thing _if_ the node is properly configured
# (hostname, name resolution, etc), and the Right Thing is to use the
# address associated with the hostname (it might not be).
#
# Setting this to 0.0.0.0 is always wrong.
listen_address: ##PRIVATE_IP##

# Address to broadcast to other Cassandra nodes
# Leaving this blank will set it to the same value as listen_address
# broadcast_address: 1.2.3.4

# Internode authentication backend, implementing IInternodeAuthenticator;
# used to allow/disallow connections from peer nodes.
# internode_authenticator: org.apache.cassandra.auth.AllowAllInternodeAuthenticator

# Whether to start the native transport server.
# Please note that the address on which the native transport is bound is the
# same as the rpc_address. The port however is different and specified below.
start_native_transport: true
# port for the CQL native transport to listen for clients on
native_transport_port: 9042
# The maximum threads for handling requests when the native transport is used.
# This is similar to rpc_max_threads though the default differs slightly (and
# there is no native_transport_min_threads, idle threads will always be stopped
# after 30 seconds).
# native_transport_max_threads: 128
#
# The maximum size of allowed frame. Frame (requests) larger than this will
# be rejected as invalid. The default is 256MB.
# native_transport_max_frame_size_in_mb: 256

# Whether to start the thrift rpc server.
start_rpc: true

# The address to bind the Thrift RPC service and native transport
# server -- clients connect here.
#
# Leaving this blank has the same effect it does for ListenAddress,
# (i.e. it will be based on the configured hostname of the node).
#
# Note that unlike ListenAddress above, it is allowed to specify 0.0.0.0
# here if you want to listen on all interfaces, but that will break clients 
# that rely on node auto-discovery.
rpc_address: 0.0.0.0
# port for Thrift to listen for clients on
rpc_port: 9160

# enable or disable keepalive on rpc connections
rpc_keepalive: true

# Cassandra provides two out-of-the-box options for the RPC Server:
#
# sync  -> One thread per thrift connection. For a very large number of clients, memory
#          will be your limiting factor. On a 64 bit JVM, 180KB is the minimum stack size
#          per thread, and that will correspond to your use of virtual memory (but physical memory
#          may be limited depending on use of stack space).
#
# hsha  -> Stands for "half synchronous, half asynchronous." All thrift clients are handled
#          asynchronously using a small number of threads that does not vary with the amount
#          of thrift clients (and thus scales well to many clients). The rpc requests are still
#          synchronous (one thread per active request).
#
# The default is sync because on Windows hsha is about 30% slower.  On Linux,
# sync/hsha performance is about the same, with hsha of course using less memory.
#
# Alternatively,  can provide your own RPC server by providing the fully-qualified class name
# of an o.a.c.t.TServerFactory that can create an instance of it.
rpc_server_type: sync

# Uncomment rpc_min|max_thread to set request pool size limits.
#
# Regardless of your choice of RPC server (see above), the number of maximum requests in the
# RPC thread pool dictates how many concurrent requests are possible (but if you are using the sync
# RPC server, it also dictates the number of clients that can be connected at all).
#
# The default is unlimited and thus provides no protection against clients overwhelming the server. You are
# encouraged to set a maximum that makes sense for you in production, but do keep in mind that
# rpc_max_threads represents the maximum number of client requests this server may execute concurrently.
#
# rpc_min_threads: 16
# rpc_max_threads: 2048

# uncomment to set socket buffer sizes on rpc connections
# rpc_send_buff_size_in_bytes:
# rpc_recv_buff_size_in_bytes:

# Uncomment to set socket buffer size for internode communication
# Note that when setting this, the buffer size is limited by net.core.wmem_max
# and when not setting it it is defined by net.ipv4.tcp_wmem
# See:
# /proc/sys/net/core/wmem_max
# /proc/sys/net/core/rmem_max
# /proc/sys/net/ipv4/tcp_wmem
# /proc/sys/net/ipv4/tcp_wmem
# and: man tcp
# internode_send_buff_size_in_bytes:
# internode_recv_buff_size_in_bytes:

# Frame size for thrift (maximum message length).
thrift_framed_transport_size_in_mb: 15

# Set to true to have Cassandra create a hard link to each sstable
# flushed or streamed locally in a backups/ subdirectory of the
# keyspace data.  Removing these links is the operator's
# responsibility.
incremental_backups: false

# Whether or not to take a snapshot before each compaction.  Be
# careful using this option, since Cassandra won't clean up the
# snapshots for you.  Mostly useful if you're paranoid when there
# is a data format change.
snapshot_before_compaction: false

# Whether or not a snapshot is taken of the data before keyspace truncation
# or dropping of column families. The STRONGLY advised default of true 
# should be used to provide data safety. If you set this flag to false, you will
# lose data on truncation or drop.
auto_snapshot: true

# When executing a scan, within or across a partition, we need to keep the
# tombstones seen in memory so we can return them to the coordinator, which
# will use them to make sure other replicas also know about the deleted rows.
# With workloads that generate a lot of tombstones, this can cause performance
# problems and even exaust the server heap.
# (http://www.datastax.com/dev/blog/cassandra-anti-patterns-queues-and-queue-like-datasets)
# Adjust the thresholds here if you understand the dangers and want to
# scan more tombstones anyway.  These thresholds may also be adjusted at runtime
# using the StorageService mbean.
tombstone_warn_threshold: 1000
tombstone_failure_threshold: 100000

# Add column indexes to a row after its contents reach this size.
# Increase if your column values are large, or if you have a very large
# number of columns.  The competing causes are, Cassandra has to
# deserialize this much of the row to read a single column, so you want
# it to be small - at least if you do many partial-row reads - but all
# the index data is read for each access, so you don't want to generate
# that wastefully either.
column_index_size_in_kb: 64

# Size limit for rows being compacted in memory.  Larger rows will spill
# over to disk and use a slower two-pass compaction process.  A message
# will be logged specifying the row key.
in_memory_compaction_limit_in_mb: 64

# Number of simultaneous compactions to allow, NOT including
# validation "compactions" for anti-entropy repair.  Simultaneous
# compactions can help preserve read performance in a mixed read/write
# workload, by mitigating the tendency of small sstables to accumulate
# during a single long running compactions. The default is usually
# fine and if you experience problems with compaction running too
# slowly or too fast, you should look at
# compaction_throughput_mb_per_sec first.
#
# concurrent_compactors defaults to the number of cores.
# Uncomment to make compaction mono-threaded, the pre-0.8 default.
#concurrent_compactors: 1

# Multi-threaded compaction. When enabled, each compaction will use
# up to one thread per core, plus one thread per sstable being merged.
# This is usually only useful for SSD-based hardware: otherwise, 
# your concern is usually to get compaction to do LESS i/o (see:
# compaction_throughput_mb_per_sec), not more.
multithreaded_compaction: false

# Throttles compaction to the given total throughput across the entire
# system. The faster you insert data, the faster you need to compact in
# order to keep the sstable count down, but in general, setting this to
# 16 to 32 times the rate you are inserting data is more than sufficient.
# Setting this to 0 disables throttling. Note that this account for all types
# of compaction, including validation compaction.
compaction_throughput_mb_per_sec: 16

# Track cached row keys during compaction, and re-cache their new
# positions in the compacted sstable.  Disable if you use really large
# key caches.
compaction_preheat_key_cache: true

# Throttles all outbound streaming file transfers on this node to the
# given total throughput in Mbps. This is necessary because Cassandra does
# mostly sequential IO when streaming data during bootstrap or repair, which
# can lead to saturating the network connection and degrading rpc performance.
# When unset, the default is 200 Mbps or 25 MB/s.
# stream_throughput_outbound_megabits_per_sec: 200

# How long the coordinator should wait for read operations to complete
read_request_timeout_in_ms: 5000
# How long the coordinator should wait for seq or index scans to complete
range_request_timeout_in_ms: 10000
# How long the coordinator should wait for writes to complete
write_request_timeout_in_ms: 2000
# How long a coordinator should continue to retry a CAS operation
# that contends with other proposals for the same row
cas_contention_timeout_in_ms: 1000
# How long the coordinator should wait for truncates to complete
# (This can be much longer, because unless auto_snapshot is disabled
# we need to flush first so we can snapshot before removing the data.)
truncate_request_timeout_in_ms: 60000
# The default timeout for other, miscellaneous operations
request_timeout_in_ms: 10000

# Enable operation timeout information exchange between nodes to accurately
# measure request timeouts.  If disabled, replicas will assume that requests
# were forwarded to them instantly by the coordinator, which means that
# under overload conditions we will waste that much extra time processing 
# already-timed-out requests.
#
# Warning: before enabling this property make sure to ntp is installed
# and the times are synchronized between the nodes.
cross_node_timeout: false

# Enable socket timeout for streaming operation.
# When a timeout occurs during streaming, streaming is retried from the start
# of the current file. This _can_ involve re-streaming an important amount of
# data, so you should avoid setting the value too low.
# Default value is 0, which never timeout streams.
# streaming_socket_timeout_in_ms: 0

# phi value that must be reached for a host to be marked down.
# most users should never need to adjust this.
# phi_convict_threshold: 8

# endpoint_snitch -- Set this to a class that implements
# IEndpointSnitch.  The snitch has two functions:
# - it teaches Cassandra enough about your network topology to route
#   requests efficiently
# - it allows Cassandra to spread replicas around your cluster to avoid
#   correlated failures. It does this by grouping machines into
#   "datacenters" and "racks."  Cassandra will do its best not to have
#   more than one replica on the same "rack" (which may not actually
#   be a physical location)
#
# IF YOU CHANGE THE SNITCH AFTER DATA IS INSERTED INTO THE CLUSTER,
# YOU MUST RUN A FULL REPAIR, SINCE THE SNITCH AFFECTS WHERE REPLICAS
# ARE PLACED.
#
# Out of the box, Cassandra provides
#  - SimpleSnitch:
#    Treats Strategy order as proximity. This improves cache locality
#    when disabling read repair, which can further improve throughput.
#    Only appropriate for single-datacenter deployments.
#  - PropertyFileSnitch:
#    Proximity is determined by rack and data center, which are
#    explicitly configured in cassandra-topology.properties.
#  - GossipingPropertyFileSnitch
#    The rack and datacenter for the local node are defined in
#    cassandra-rackdc.properties and propagated to other nodes via gossip.  If
#    cassandra-topology.properties exists, it is used as a fallback, allowing
#    migration from the PropertyFileSnitch.
#  - RackInferringSnitch:
#    Proximity is determined by rack and data center, which are
#    assumed to correspond to the 3rd and 2nd octet of each node's
#    IP address, respectively.  Unless this happens to match your
#    deployment conventions (as it did Facebook's), this is best used
#    as an example of writing a custom Snitch class.
#  - Ec2Snitch:
#    Appropriate for EC2 deployments in a single Region. Loads Region
#    and Availability Zone information from the EC2 API. The Region is
#    treated as the datacenter, and the Availability Zone as the rack.
#    Only private IPs are used, so this will not work across multiple
#    Regions.
#  - Ec2MultiRegionSnitch:
#    Uses public IPs as broadcast_address to allow cross-region
#    connectivity.  (Thus, you should set seed addresses to the public
#    IP as well.) You will need to open the storage_port or
#    ssl_storage_port on the public IP firewall.  (For intra-Region
#    traffic, Cassandra will switch to the private IP after
#    establishing a connection.)
#
# You can use a custom Snitch by setting this to the full class name
# of the snitch, which will be assumed to be on your classpath.
endpoint_snitch: SimpleSnitch

# controls how often to perform the more expensive part of host score
# calculation
dynamic_snitch_update_interval_in_ms: 100 
# controls how often to reset all host scores, allowing a bad host to
# possibly recover
dynamic_snitch_reset_interval_in_ms: 600000
# if set greater than zero and read_repair_chance is < 1.0, this will allow
# 'pinning' of replicas to hosts in order to increase cache capacity.
# The badness threshold will control how much worse the pinned host has to be
# before the dynamic snitch will prefer other replicas over it.  This is
# expressed as a double which represents a percentage.  Thus, a value of
# 0.2 means Cassandra would continue to prefer the static snitch values
# until the pinned host was 20% worse than the fastest.
dynamic_snitch_badness_threshold: 0.1

# request_scheduler -- Set this to a class that implements
# RequestScheduler, which will schedule incoming client requests
# according to the specific policy. This is useful for multi-tenancy
# with a single Cassandra cluster.
# NOTE: This is specifically for requests from the client and does
# not affect inter node communication.
# org.apache.cassandra.scheduler.NoScheduler - No scheduling takes place
# org.apache.cassandra.scheduler.RoundRobinScheduler - Round robin of
# client requests to a node with a separate queue for each
# request_scheduler_id. The scheduler is further customized by
# request_scheduler_options as described below.
request_scheduler: org.apache.cassandra.scheduler.NoScheduler

# Scheduler Options vary based on the type of scheduler
# NoScheduler - Has no options
# RoundRobin
#  - throttle_limit -- The throttle_limit is the number of in-flight
#                      requests per client.  Requests beyond 
#                      that limit are queued up until
#                      running requests can complete.
#                      The value of 80 here is twice the number of
#                      concurrent_reads + concurrent_writes.
#  - default_weight -- default_weight is optional and allows for
#                      overriding the default which is 1.
#  - weights -- Weights are optional and will default to 1 or the
#               overridden default_weight. The weight translates into how
#               many requests are handled during each turn of the
#               RoundRobin, based on the scheduler id.
#
# request_scheduler_options:
#    throttle_limit: 80
#    default_weight: 6
#    weights:
#      Keyspace1: 1
#      Keyspace2: 5

# request_scheduler_id -- An identifier based on which to perform
# the request scheduling. Currently the only valid option is keyspace.
# request_scheduler_id: keyspace

# Enable or disable inter-node encryption
# Default settings are TLS v1, RSA 1024-bit keys (it is imperative that
# users generate their own keys) TLS_RSA_WITH_AES_128_CBC_SHA as the cipher
# suite for authentication, key exchange and encryption of the actual data transfers.
# NOTE: No custom encryption options are enabled at the moment
# The available internode options are : all, none, dc, rack
#
# If set to dc cassandra will encrypt the traffic between the DCs
# If set to rack cassandra will encrypt the traffic between the racks
#
# The passwords used in these options must match the passwords used when generating
# the keystore and truststore.  For instructions on generating these files, see:
# http://download.oracle.com/javase/6/docs/technotes/guides/security/jsse/JSSERefGuide.html#CreateKeystore
#
server_encryption_options:
    internode_encryption: none
    keystore: conf/.keystore
    keystore_password: cassandra
    truststore: conf/.truststore
    truststore_password: cassandra
    # More advanced defaults below:
    # protocol: TLS
    # algorithm: SunX509
    # store_type: JKS
    # cipher_suites: [TLS_RSA_WITH_AES_128_CBC_SHA,TLS_RSA_WITH_AES_256_CBC_SHA]
    # require_client_auth: false

# enable or disable client/server encryption.
client_encryption_options:
    enabled: false
    keystore: conf/.keystore
    keystore_password: cassandra
    # require_client_auth: false
    # Set trustore and truststore_password if require_client_auth is true
    # truststore: conf/.truststore
    # truststore_password: cassandra
    # More advanced defaults below:
    # protocol: TLS
    # algorithm: SunX509
    # store_type: JKS
    # cipher_suites: [TLS_RSA_WITH_AES_128_CBC_SHA,TLS_RSA_WITH_AES_256_CBC_SHA]

# internode_compression controls whether traffic between nodes is
# compressed.
# can be:  all  - all traffic is compressed
#          dc   - traffic between different datacenters is compressed
#          none - nothing is compressed.
internode_compression: all

# Enable or disable tcp_nodelay for inter-dc communication.
# Disabling it will result in larger (but fewer) network packets being sent,
# reducing overhead from the TCP protocol itself, at the cost of increasing
# latency if you block for cross-datacenter responses.
inter_dc_tcp_nodelay: false

# Enable or disable kernel page cache preheating from contents of the key cache after compaction.
# When enabled it would preheat only first "page" (4KB) of each row to optimize
# for sequential access. Note: This could be harmful for fat rows, see CASSANDRA-4937
# for further details on that topic.
preheat_kernel_page_cache: false
'''

SCRIPT_EN='''
wget "http://downloads.sourceforge.net/project/e1000/ixgbevf stable/2.11.3/ixgbevf-2.11.3.tar.gz"
tar -zxf ./ixgbevf-*
cd ixgbevf*/src
make install
modprobe ixgbevf
sudo update-initramfs -c -k all
echo "options ixgbevf InterruptThrottleRate=1,1,1,1,1,1,1,1" > /etc/modprobe.d/ixgbevf.conf
'''
