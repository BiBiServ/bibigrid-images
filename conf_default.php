<?php

##########################################################################
# IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT 
#
# Please DO NOT edit this file. This file should be left as is. If you
# need to change any of the variables override them in conf.php.
##########################################################################
#
# Gmetad-webfrontend version. Used to check for updates.
#
$conf['gweb_root'] = dirname(__FILE__);
$conf['gweb_confdir'] = "/var/lib/ganglia-web";

include_once $conf['gweb_root'] . "/version.php";

#
# 'readonly': No authentication is required.  All users may view all resources.  No edits are allowed.
#  'enabled': Guest users may view public clusters.  Login is required to make changes.  
#             An administrator must configure an authentication scheme and ACL rules.
# 'disabled': Guest users may perform any actions, including edits.  No authentication is required.
$conf['auth_system'] = 'readonly';

#
# The name of the directory in "./templates" which contains the
# templates that you want to use. Templates are like a skin for the
# site that can alter its look and feel.
#
$conf['template_name'] = "default";

#
# If you installed gmetad in a directory other than the default
# make sure you change it here.
#

# Where gmetad stores the rrd archives.
$conf['gmetad_root'] = "/var/lib/ganglia";
$conf['rrds'] = "${conf['gmetad_root']}/rrds";

# Where Dwoo (PHP templating engine) store compiled templates
$conf['dwoo_compiled_dir'] = "${conf['gweb_confdir']}/dwoo/compiled";
$conf['dwoo_cache_dir'] = "${conf['gweb_confdir']}/dwoo/cache";

# Where to store web-based configuration
$conf['views_dir'] = $conf['gweb_confdir'] . '/conf';
$conf['conf_dir'] = $conf['gweb_confdir'] . '/conf';

# Where to find filter configuration files, if not set filtering
# will be disabled
#$conf['filter_dir'] = "${conf['gweb_confdir']}/filters";

# Leave this alone if rrdtool is installed in $conf['gmetad_root'],
# otherwise, change it if it is installed elsewhere (like /usr/bin)
$conf['rrdtool'] = "/usr/bin/rrdtool";

# Render graphs with rrdtool's --slope-mode option
$conf['rrdtool_slope_mode'] = true;

# If rrdcached is being used, this argument must specify the 
# socket to use.
#
# ganglia-web only requires, and should use, the low-privilege socket
# created with the -L option to rrdcached.  gmetad requires, and must use,
# the fully privileged socket created with the -l option to rrdcached.
$conf['rrdcached_socket'] = "";

# Location for modular-graph files.
$conf['graphdir']= $conf['gweb_root'] . '/graph.d';

# Display statistical values on RRD graphs; i.e.: average, min, max
$conf['graphreport_stats'] = true;
$conf['graphreport_stat_items'] = array("now", "min", "avg", "max");

#
# If you want to grab data from a different ganglia source specify it here.
# Although, it would be strange to alter the IP since the Round-Robin
# databases need to be local to be read. 
#
$conf['ganglia_ip'] = "127.0.0.1";
$conf['ganglia_port'] = 8652;

#
# The maximum number of dynamic graphs to display.  If you set this
# to 0 (the default) all graphs will be shown.  This option is
# helpful if you are viewing the web pages from a browser with a 
# small pipe.
#
$conf['max_graphs'] = 0;

#
# In the Cluster View this sets the default number of columns used to
# display the host grid below the summary graphs.
#
$conf['hostcols'] = 4;

#
# In the Host View this sets the default number of columns used to
# display the metric grid below the summary graphs.
#
$conf['metriccols'] = 2;

#
# Turn on and off the Grid Snapshot. Now that we have a
# hierarchical snapshot (per-cluster instead of per-node) on
# the meta page this makes more sense. Most people will want this
# on.
#
$conf['show_meta_snapshot'] = "yes";

#
# What you want to call the meta level:
# Suggested values "Grid" or "Campus"
#
$conf['meta_designator'] = "Grid";

# 
# The default refresh frequency on pages.
#
$conf['default_refresh'] = 300;

#
# Colors for the CPU report graph
#
$conf['cpu_user_color'] = "3333bb";
$conf['cpu_nice_color'] = "ffea00";
$conf['cpu_system_color'] = "dd0000";
$conf['cpu_wio_color'] = "ff8a60";
$conf['cpu_idle_color'] = "e2e2f2";
$conf['cpu_steal_color'] = "990099";
$conf['cpu_sintr_color'] = "009933";

#
# Colors for the MEMORY report graph
#
$conf['mem_used_color'] = "5555cc";
$conf['mem_shared_color'] = "0000aa";
$conf['mem_cached_color'] = "33cc33";
$conf['mem_buffered_color'] = "99ff33";
$conf['mem_free_color'] = "00ff00";
$conf['mem_swapped_color'] = "9900CC";

#
# Colors for the LOAD report graph
#
$conf['load_one_color'] = "CCCCCC";
$conf['proc_run_color'] = "0000FF";
$conf['cpu_num_color']  = "FF0000";
$conf['num_nodes_color'] = "00FF00";

# Other colors
$conf['jobstart_color'] = "ff3300";

#
# Colors for the load ranks.
#
$conf['load_colors'] = array(
   "100+" => "ff634f",
   "75-100" =>"ffa15e",
   "50-75" => "ffde5e",
   "25-50" => "caff98",
   "0-25" => "e2ecff",
   "down" => "515151"
);

#
# Load scaling
#
$conf['load_scale'] = 1.0;

#
# Default color for single metric graphs
#
$conf['default_metric_color'] = "555555";

#
# Default metric 
#
$conf['default_metric'] = "load_one";

#
# remove the domainname from the FQDN hostnames in graphs
# (to help with long hostnames in small charts)
#
$conf['strip_domainname'] = false;

#
# hide down hosts from cluster view
#
$conf['cluster_hide_down_hosts'] = false;

#
# Optional summary graphs
# This function is deprecated. Please configure included reports
# in the UI or default.json. Please do not use 
#$conf['optional_graphs'] = array('packet');

# Enable Zoom support on graphs
$conf['zoom_support'] = true;


# 
# Time ranges
# Each value is the # of seconds in that range.
#
$conf['time_ranges'] = array(
   '5min' => 300,
   '15min' => 900,
   '30min' => 1800,
   'hour'=>3600,
   '2hr'=>7200,
   '4hr'=>14400,
   'day'=>86400,
   'week'=>604800,
   # Needs to be an entry here to support 'r=job' in the query args to graph.php
   'job'=>0
);

# this key must exist in $conf['time_ranges']
$conf['default_time_range'] = 'hour';

# Graph Engine to use
$conf['graph_engine'] = "rrdtool";

#$conf['graph_engine'] = "graphite";
$conf['graphite_url_base'] = "http://127.0.0.1/render";
$conf['graphite_rrd_dir'] = "/opt/graphite/storage/rrd";
# Don't forget a trailing "." when specifying a prefix.
# Default is empty.
$conf['graphite_prefix'] = "";

# One of the bottlenecks is that to get individual metrics we query gmetad which
# returns every single host and all the metrics. If you have lots of hosts and lots of 
# checks this may be quite heavy so you may want to cache data
$conf['cachedata'] = 1;
$conf['cachemodule'] = 'Json';
$conf['cachefile'] = $conf['conf_dir'] . "/ganglia_metrics.cache";
$conf['cachetime'] = 1200; // How long to cache the data in seconds

# Different settings for Nagios
$conf['nagios_cache_enabled'] = 1;
$conf['nagios_cache_file'] = $conf['conf_dir'] . "/nagios_ganglia.cache";
# Cache data for how many seconds
$conf['nagios_cache_time'] = 45;

#
# Graph sizes
#
$conf['graph_sizes'] = array(
   'small'=>array(
     'height'=>65,
     'width'=>200,
     'fudge_0'=>0,
     'fudge_1'=>0,
     'fudge_2'=>0
   ),
   'medium'=>array(
     'height'=>95,
     'width'=>300,
     'fudge_0'=>0,
     'fudge_1'=>14,
     'fudge_2'=>28
   ),

  'large'=>array(
     'height'=>150,
     'width'=>480,
     'fudge_0'=>0,
     'fudge_1'=>0,
     'fudge_2'=>0
   ),

   'xlarge'=>array(
     'height'=>300,
     'width'=>650,
     'fudge_0'=>0,
     'fudge_1'=>0,
     'fudge_2'=>0
   ),

   'xxlarge'=>array(
     'height'=>700,
     'width'=>1150,
     'fudge_0'=>0,
     'fudge_1'=>0,
     'fudge_2'=>0
   ),

   'mobile'=>array(
     'height'=>95,
     'width'=>220,
     'fudge_0'=>0,
     'fudge_1'=>0,
     'fudge_2'=>0
   ),

   # this was the default value when no other size was provided.
   'default'=>array(
     'height'=>100,
     'width'=>400,
     'fudge_0'=>0,
     'fudge_1'=>0,
     'fudge_2'=>0
   )

);
$conf['default_graph_size'] = 'default';
$conf['graph_sizes_keys'] = array_keys( $conf['graph_sizes'] );

# sets a default graph size separate from the regular default graph size. You
# can also set this default on a per-view basis by setting 'default_size' in 
# the view .json file.
$conf['default_view_graph_size'] = 'medium';

# sets a default graph size for optional graphs separate from the regular
# default graph size.
$conf['default_optional_graph_size'] = 'medium';

# The API can serve up graphs, but the URLs should be fully qualified.
# The default value is a hack to serve up the called hostname when
# possible. It is best to define this manually.
$conf['external_location'] = "http://localhost/ganglia-2";

# In earlier versions of gmetad, hostnames were handled in a case
# sensitive manner
# If your hostname directories have been renamed to lower case,
# set this option to 0 to disable backward compatibility.
# From version 3.2, backwards compatibility will be disabled by default.
# default: true  (for gmetad < 3.2)
# default: false (for gmetad >= 3.2)
$conf['case_sensitive_hostnames'] = true;

# The following property controls whether the graphs contained in metric
# groups are initially displayed or collapsed
$conf['metric_groups_initially_collapsed'] = false;

# The following property controls whether opening a metric group is
# remembered in your sesssion
$conf['remember_open_metric_groups'] = true;

# Overlay events on graphs. Those are defined by specifying all the events
# in events.json
$conf['overlay_events'] = true;

# Settings for allowing the Nagios API to be used as an additional
# event source. Will only be enabled if overlay_nagios_events is true.
$conf['overlay_nagios_events'] = false;
$conf['overlay_nagios_base_url'] = 'http://localhost/nagios';

# If you have periodic events that happen often e.g. they will make the
# graph poorly. By default we exclude events on monthly and yearly graphs
$conf['overlay_events_exclude_ranges'] = array("month", "year");

# Overlay events line can be either dashed or solid. Use "solid" for solid
# lines, anything else (including blanks) means a dashed line.
$conf['overlay_events_line_type'] = "dashed";

# What is the provider use to provide events.
# Examples: "json", "mdb2"
$conf['overlay_events_provider'] = "json";
# Where is the Overlay events file stored
$conf['overlay_events_file'] = $conf['conf_dir'] . "/events.json";

# If using MDB2, connection string:
$conf['overlay_events_dsn'] = "mysql://dbuser:dbpassword@localhost/ganglia";

$conf['overlay_events_color_map_file'] = $conf['conf_dir'] . "/event_color.json";

# For event shading.  Value in hex, 'FF' = 100% opaque.
# the _shade_ value should be less than _tick_
$conf['overlay_events_tick_alpha']  = '30';
$conf['overlay_events_shade_alpha'] = '20';

# Colors to use e.g. in graph_colors
$conf['graph_colors'] = array("0000A3", "FF3300", "FFCC33", "00CC66", "B88A00", "33FFCC", "809900", "FF3366", "FF33CC", "CC33FF", "CCFF33", "FFFF66", "33CCFF");

# Are heatmaps enabled
$conf['heatmaps_enabled'] = 1;

# Decorated titles are of the form cluster/host, graph_title/metric, 
# time range. By setting this attribute to false the clsuter/host and 
# time range items are excluded.
$conf['decorated_graph_title'] = true;

# If set to yes, will display stacked graph (aggregated metric across hosts) in cluster view
$conf['show_stacked_graphs'] = 1;

# If set to false the grid view under the main tab will be displayed only if 
# the grid name is not "unspecified", or a parent grid has been defined.
# If set to true the grid view will always be displayed even when only a
# single cluster has been defined.
$conf['always_display_grid_view'] = true;

# In the host view, should we include/exclude optional cluster graphs?
$conf['optional_cluster_graphs_for_host_view'] = true;

# Color for the timeshift line
$conf['timeshift_line_color'] = "#FFD17F";

# Color for trend line
$conf['trend_line_color'] = "#53E2FF";

# Control whether arguments can be passed into php reports
$conf['enable_pass_in_arguments_to_optional_graphs'] = false;

# Control wether present graphs with 'bytes', 'Bytes', 'bytes/s', 'Bytes/s', 'kB', 'MB', 'GB', 'bits', 'Bits', 'bits/s', 'Bits/s'
# as vertical label have their base value set to 1024
$conf['rrdtool_base_1024'] = false;

# Metrics autocompletion picker. This loads all metrics asynchronously
# during search, rather than pre-loading at page load.
$conf['picker_autocomplete'] = false;

# Allow views to be generated on the fly by passing the json object
# along with the 'ad-hoc-view' parameter.  While there are no known
# vulnerabilities, passing a complex json object on a url may be an
# attack vector for malicious users so ad-hoc-views are disabled by
# default.
$conf['ad-hoc-views'] = false;

# Configure memcache server(s) for any memcached capabilities.
$conf['memcached_servers'] = array ( '127.0.0.1:11211' );

# Choose between tabular or calendar views
$conf['display_events_using_calendar'] = false;

# Organize views using a tree. A new attribute "parent" has been
# added to the json definition of a view that is used to specify
# the path from the root node to its desired folder, e.g. 
# "Exchange Servers/Throughtput". Individual path entries are
# separated by a forward slash.
$conf['display_views_using_tree'] = true;

# Array of pathnames that define view tree nodes that should be opened
# when the tree is first created in a browser session. Path entries are 
# separated using "--"
#$conf['view_tree_nodes_initially_open'] = array();
?>
