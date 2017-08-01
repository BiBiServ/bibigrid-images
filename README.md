# BiBiGrid-Images

BiBiGrid-Images is small tool written in Python that creates images used by [BiBiGrid](https://github.com/bibiserv/bibigrid) on top of a base Ubuntu 14.04 (cloud-)images for virtual environments (AWS, Openstack, ...). The tool creates different images for the master and slave instances. BiBiGrid-Images make use of possible proxy settings.


## Build

```
> make

```

## Usage
Typically, the BiBiGrid-Image tool is run on a clean base Ubuntu 14.04 installation.


```
> ./bibigrid-help
usage: bibigrid-image [-h] [--version] --for {master,slave}
                      [--username USERNAME] [--skip-apt] [--step-by-step-apt]
                      [--en]

Create a BiBiGrid Master/Slave Image. Use proxy properties from environment

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  --for {master,slave}  The type of the image to be created.
  --username USERNAME   The username of the current user (default: ubuntu).
  --skip-apt            Skip package installation entirely.
  --step-by-step-apt    Invoke apt separately for every package.
  --en                  Enhanced Networking for C3,R3 and I2 instances.
```


## Known Issues
- BiBiGrid-Images currently only run on Ubuntu 14.04. Other versions are currently not supported.
- DNS should work properly, otherwise the GridEngine initial configuration creates an error. 
- **DNS / Openstack :** The default DNS entry (following the Openstack installation guide) for every instance has the pattern *host-$ip(1st octet)-$ip(2nd octet)-$ip(3rd octect)-$ip(4th octet)* independend of the given instance name. The cloud-init software, which typically configures an instance using the metadata service during boot time, hardcode the hostname to instance name (setting `/etc/hosts`). A bug  (which only occurs in this context) in the dhcp-client software (since Ubuntu 14.04) prevents that DNS informations distributed by DHCP are updated, when the instance has network connection. However, this problem can be solved. You can configure Openstack to use the instance-name as hostname (instead of above mentioned pattern) or patch the DHCP-client.

- The **username** argument should be set to the user account later used by the BiBiGrid tool. In case of Ubuntu cloudimages this is always **ubuntu**.
- Enable **Enhanced Networking** makes only sense when preparing images for Amazon AWS using instance types with very fast network connections. Enable this feature for images running on other cloud framework (e.g. Openstack) can lead to corrupt images.