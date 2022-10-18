---
title: "Arm User-Based Licenses"

additional_search_terms:
  - compiler

tool_install: true              # DO NOT MODIFY. Always true for tool installs
layout: "installtoolsall"       # DO NOT MODIFY. Always true for the main page of tool installs
---
All Arm tools are license managed. Arm is migrating to a user-based licensing (UBL) system which greatly simplifies license configuration. It is available for [Arm Success Kits](../successkits/).

With a UBL license you have unlimited access to all components within the success kit you have enabled. The license is cached locally for up to 7 days, enabling remote or traveling users to have access to tools without connecting to their license server.

Using any UBL enabled tool when the server is available will renew the 7 days of license. This renewal attempt is performed once per 24 hours.

If the license is not renewed within 7 days, it is automatically returned to the pool of available licenses. When you next use a UBL licensed tool, it will automatically attempt to check out a new license..

The licenses can be set up as:
* [Local license server](#local), an internally managed license server, likely only accessible from internal network/VPN.
* [Cloud license server](#cloud), a license server managed by Arm, accessible from anywhere.

Legacy products do not support UBL licensing. For those products, use [FlexLM licensing](#legacy).

# Local license server {#local}

If your local license server is already running, jump to [End-user license setup](#user).

## License server setup {#admin}

To generate your licenses you need access to the Arm user-based licensing portal, with the account that the licenses were assigned to.
```url
https://developer.arm.com/support/licensing/user-based
```
### License server set up

UBL license server software is supported on the following host [operating systems](https://developer.arm.com/documentation/107573/latest/Getting-started-with-user-based-licensing/Hardware-and-software-requirements):
* Red Hat Enterprise Linux / CentOS 7 and 8
* Ubuntu 20.04 LTS

### Download and install server software

The local license server (LLS) software can be downloaded from:
```url
https://lm.arm.com/downloads
```
The license server uses a number of standard Linux [utilities](https://developer.arm.com/documentation/107573/latest/Getting-started-with-user-based-licensing/Hardware-and-software-requirements), including Python and Java.

Expand the tarball, and install the license server software.
```console
tar -xf flexnetls-armlmd-<version>.tar.gz
sudo flexnetls-armlmd-<version>/install_license_server
```
The installer will automatically start the license server software. You will see the following output:
```
Waiting for license server... (up to 120 seconds)
License server ready.
```
To check the status of the server application, use:
```console
sudo systemctl status flexnetls-armlmd
```
### Set environment variables

It is recommended to add the install directory to the `PATH`, and to set the `FLEXNETLS_BASEURL` environment variable. For example:
```console
export PATH=/opt/flexnetls-armlmd/bin:$PATH
export FLEXNETLS_BASEURL=http://localhost:7070/api/1.0/instances/~
```
### Set administrator password

The first time you install the LLS server, you must set an appropriate password so as to be able to configure it. Use the following command:
```console
armlm_change_admin_password
```
### Verify server hostid (optional)

The default `hostid` was selected by the license server installer. To view the selected hostid use:
```console
armlm_show_hostid
```
which will output (in JSON format) a list of the selected and all available hostids.

If you wish to change the selected hostid, edit the `/server/local-configuration.yaml` file. See the [documentation](https://developer.arm.com/documentation/107573/latest/Getting-started-with-user-based-licensing/Register-your-license-server) for full details.

### Register license server with Arm

Create a license server identity file (`identity.bin`) using:
```console
armlm_generate_server_identity --identity-file identity.bin
```
Access the Arm user-based licensing portal.
```url
https://developer.arm.com/support/licensing/user-based
```
Navigate to `Manage License Servers`, and click on `Register Local License Server`. Upload the identity file.

### Add licenses to server

Click on `Add Products` and select the quantity of the available licenses to assign to that server. When satisfied, click on `Add Products` and a license file will be generated.

If not automatically downloaded or if to consolidate with existing licenses, click on `Download all licenses allocated to this server`.

Install the license file on the license server with:
```console
armlm_update_licenses --data-file <license_file>
```
You will see the following output when successful.
```
Licenses have been successfully updated. No confirmation is required.
```
The licenses are now ready to use by the [end-users](#user).

### Monitor license server usage

To list the number of licenses (total and used) use:
```console
armlm_list_products
```
To list the current active users of the licenses use:
```console
armlm_list_users
```
## End-user license setup {#user}

Arm UBL licenses enable Hardware (HSK) and Software (SSK) [Success Kits](https://www.arm.com/products/development-tools/success-kits).

HSKs are a super-set of SSKs. If you only require access to the components of an SSK, it is strongly recommended that you only use an SSK license.

### Set up by environment variable

Create `ARMLM_ONDEMAND_ACTIVATION` environment variable referencing the success kit product code and your [internal server](#admin).

{{< tabpane code=true >}}
  {{< tab header="HSK" >}}
export ARMLM_ONDEMAND_ACTIVATION=HWSKT-STD0@https://internal.ubl.server
{{< /tab >}}
  {{< tab header="SSK" >}}
export ARMLM_ONDEMAND_ACTIVATION=SWSKT-STD0@https://internal.ubl.server
{{< /tab >}}
{{< /tabpane >}}

A license will be checked out whenever a UBL enabled tool is used.

To see if you have a license checked-out, enter the command:
```console
armlm inspect
```
If a license is checked out, you have access to all components within the success kit you have enabled.

### Manually set up

Open a command prompt, and navigate to the bin directory of any UBL enabled product. Activate an appropriate success kit license:

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

# Cloud license server {#cloud}

If you already have an activation code, go to [activate license](#activate).

### Generate activation code

Arm UBL licenses enable Hardware (HSK) and Software (SSK) [Success Kits](https://www.arm.com/products/development-tools/success-kits).

HSKs are a super-set of SSKs. If you only require access to the components of an SSK, it is strongly recommended that you only use an SSK license.

To generate an activation code you need access to the Arm user-based licensing portal with the account that the licenses were assigned to. This is likely to be an assigned license administrator rather than the end-user.
```url
https://developer.arm.com/support/licensing/user-based
```
Click on `View Details` of the product of interest, and then navigate to `Cloud Server` > `Generate Activation Code`. This code can be shared with the end-user to [activate](#activate).

Once activated, the user information will be shown along side the activation code.

### Activate license {#activate}

Open a command prompt, and navigate to the bin directory of any UBL enabled product.

Use the following command with your assigned activation code.
```console
armlm activate --code xxxxxxxx-xxxx-xxxx-xxxxxxxx
```
To confirm you have enabled the license, enter the command:
```console
armlm inspect
```
The license can also be activated in the [Arm Development Studio](https://developer.arm.com/Tools%20and%20Software/Arm%20Development%20Studio) IDE, via `Help` > `Arm License Manager` > `Manage Arm User-Based Licenses`.

You now have access to all components within the success kit you have enabled.

# Legacy FlexLM license setup {#legacy}

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
