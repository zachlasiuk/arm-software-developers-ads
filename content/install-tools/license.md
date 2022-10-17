---
title: "Arm license setup"

additional_search_terms:
  - compiler

tool_install: true              # DO NOT MODIFY. Always true for tool installs
layout: "installtoolsall"       # DO NOT MODIFY. Always true for the main page of tool installs
---
All Arm tools are license managed. Arm is migrating to a user-based licensing (UBL) system which greatly simplifies license configuration. It is available for [Arm Success Kits](../successkits/).

With a UBL license you have unlimited access to all components within the success kit you have enabled. The license is cached locally for up to 7 days, enabling remote or traveling users to have access to tools without connecting to their internal network.

Using any component whilst connected to the network will renew the 7 days of license. This renewal is performed once per 24 hours.

If the license is not renewed within 7 days, it is automatically returned to the pool of available licenses. When you next use a UBL licensed tool, it will automatically attempt to check out a new license, which will require network connectivity to the UBL server.

## License server setup (for server administrators) {#admin}

If the license server has been set up by others, jump to [User-based license setup](#user).

### License server set up

UBL license server software is supported on the following host [operating systems](https://developer.arm.com/documentation/107573/latest/Getting-started-with-user-based-licensing/Hardware-and-software-requirements):
* Red Hat Enterprise Linux / CentOS 7 and 8
* Ubuntu 20.04 LTS

### Install required utilites

The license server uses a number of standard 

{{< tabpane code=true >}}
  {{< tab header="Ubuntu" >}}
sudo apt-get install -y openjdk-8-jre python3 python3-pip bash tar sed libgetopt-argvfile-perl
pip install pyYAML
{{< /tab >}}
{{< tab header="RHE/CentOS" >}}
su -c "yum install -y java-1.8.0-openjdk python3 python3-pip bash tar sed libgetopt-argvfile-perl"
{{< /tab >}}
{{< /tabpane >}}

Full documentation is in the [User-based Licensing License Server Administration Guide](https://developer.arm.com/documentation/107573).

### Download and install server software
The local license server (LLS) software can be downloaded from:
```url
https://lm.arm.com/downloads
```
Expand the tarball
```console
tar -xf flexnetls-armlmd-<version>.tar.gz
```
Install (and start) the license server software:
```console
sudo flexnetls-armlmd-<version>/install_license_server
```
See the documentation for advanced options.

### Set environment variables

The following environment variables must be set as follows (assuming default install locations):
```console
export PATH=/opt/flexnetls-armlmd/bin:$PATH
export FLEXNETLS_BASEURL=http://localhost:7070/api/1.0/instances/~
```
### Set administrator password

The first time you use start the LLS server, you must set an appropriate password so as to be able to configure it.
```console
cd /opt/flexnetls-armlmd/bin
./armlm_change_admin_password
```
### TO DO Register license server and generate licenses

TO DO

## User-based license setup {#user}

HSK is a super-set of SSK. If you only require access to the components of SSK, it is strongly recommended that you only use an SSK license.

### Automatically check out a license

Set the `ARMLM_ONDEMAND_ACTIVATION` environment variable to point to your [internal server](#admin):
{{< tabpane code=true >}}
  {{< tab header="HSK" >}}
export ARMLM_ONDEMAND_ACTIVATION=HWSKT-STD0@https://internal.ubl.server
{{< /tab >}}
  {{< tab header="SSK" >}}
export ARMLM_ONDEMAND_ACTIVATION=SWSKT-STD0@https://internal.ubl.server
{{< /tab >}}
{{< /tabpane >}}
A license will be checked out whenever a UBL based tool is run, for example:
```console
armclang --version
```
To confirm you have checked-out a license, enter the command:
```console
armlm inspect
```
You now have access to all components within the success kit you have enabled.

### Manually check out a license

Go to the bin directory of any success kit component you have installed, and enter a command of the form:

{{< tabpane code=true >}}
  {{< tab header="HSK" >}}
armlm activate --server https://internal.ubl.server --product HWSKT-STD0
{{< /tab >}}
  {{< tab header="SSK" >}}
armlm activate --server https://internal.ubl.server --product SWSKT-STD0
{{< /tab >}}
{{< /tabpane >}}

To confirm you have checked-out a license, enter the command:
```console
armlm inspect
```
The license can also be activated in the [Arm Development Studio](https://developer.arm.com/Tools%20and%20Software/Arm%20Development%20Studio) IDE, via `Help` > `Arm License Manager` > `Manage Arm User-Based Licenses`.

You now have access to all components within the success kit you have enabled.

### Cloud UBL server setup

In some cases you may have access to a cloud UBL server, which you can enable with a supplied code. Contact your license adminstration team or Arm account manager if you are unsure what your code is.
```console
armlm activate --code xxxxxxxx-xxxx-xxxx-xxxxxxxx
```
To confirm you have enabled the license, enter the command:
```console
armlm inspect
```
## Legacy FlexLM license setup

Users who do not yet have access to UBL licenses will have FlexLM licenses. You should set the environment variable `ARMLMD_LICENSE_FILE` to map to the location of your license server. Contact your license adminstration team for information on your internal license server.

{{< tabpane code=true >}}
  {{< tab header="Windows" >}}
set ARMLMD_LICENSE_FILE=port@server
{{< /tab >}}
  {{< tab header="Linux" >}}
export ARMLMD_LICENSE_FILE=port@server
{{< /tab >}}
{{< /tabpane >}}

The license can also be configured in the [Arm Development Studio](https://developer.arm.com/Tools%20and%20Software/Arm%20Development%20Studio) IDE, via `Help` > `Arm License Manager`.

## Documentation

 - [User-based Licensing License Server Administration Guide](https://developer.arm.com/documentation/107573)
 - [User-based Licensing User Guide](https://developer.arm.com/documentation/102516)
