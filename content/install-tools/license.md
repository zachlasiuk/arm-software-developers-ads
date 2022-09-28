---
title: "Arm user license setup"

additional_search_terms:
  - compiler

tool_install: true              # DO NOT MODIFY. Always true for tool installs
layout: "installtoolsall"       # DO NOT MODIFY. Always true for the main page of tool installs
---
All Arm tools are license managed. Arm is migrating to a user-based licensing (UBL) system which greatly simplifies license configuration. It is available for [Arm Success Kits](../successkits/).

With a UBL license you have unlimited access to all components within the success kit you have enabled. The license is cached locally for up to 7 days, enabling remote or traveling users to have access to tools without connecting to their internal network.

Using any component whilst connected to the network will renew the 7 days of license (this check is performed once per day upon the first use of the tools that day).

## User-based license setup

The most common deployment method is via a UBL server within your organization. To enable usage of the tools, go to the bin directory of any success kit component you have installed, and enter a command of the form:

{{< tabpane code=true >}}
  {{< tab header="HSK" >}}
armlm activate --server https://internal.ubl.server --product HWSKT-STD0
{{< /tab >}}
  {{< tab header="SSK" >}}
armlm activate --server https://internal.ubl.server --product SWSKT-STD0
{{< /tab >}}
{{< /tabpane >}}

To confirm you have enabled the license, enter the command:
```console
armlm inspect
```
The license can also be activated in the [Arm Development Studio](https://developer.arm.com/Tools%20and%20Software/Arm%20Development%20Studio) IDE, via `Help` > `Arm License Manager` > `Manage Arm User-Based Licenses`

You now have access to all components within the success kit you have enabled. Note that HSK is a super-set of SSK. If you only require access to the components of SSK, it is strongly recommended that you only use an SSK license.

## Cloud UBL server setup

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
