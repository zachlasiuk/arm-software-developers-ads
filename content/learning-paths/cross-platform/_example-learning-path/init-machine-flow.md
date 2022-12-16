---
# User change
title: "1) Machine Initalization"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
![alt-text #center](1-machine-init-process.PNG "Machine init process")

There are three ways to be set up to create new content or make changes to the existing content.
1. A Gitpod instance with tools pre-installed (recommended)
2. A local computer (Linux, Mac, or Windows)
3. A remote server via SSH (such as AWS EC2)

# 1) [Gitpod](https://www.gitpod.io/) setup

Instead of installing tools on your local machine, you can create and modify content directly in Gitpod. This repository is configured to initalize a Gitpod instance with all tools/software you need to start contributing right away like Hugo.

First, fork the repository to your GitHub account to work with it there.

Next, install the [Gitpod Chrome Extension](https://chrome.google.com/webstore/detail/gitpod-always-ready-to-co/dodmmooeoklaejobgleioelladacbeki) which installs a Gitpod button in the GitHub project. You can also prefix the URL for the GitHub project (or your fork of the project) with gitpod.io/#

Finally, [open this repository in Gitpod](https://gitpod.io/#github.com/zachlas/arm-software-developers-ads). You can use your GitHub credentials to login to Gitpod and use the Free plan which offers up to 50 hours per month (the Free plan should be sufficient to add your content).


# 2)  Local computer setup

Make sure you have [git installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

Then fork the repository first to your GitHub account, and then clone your fork to your local machine (substitute your github account name in the command below):
```bash
git clone https://github.com/<your-github-account-name>/arm-software-developers-ads
```

Next, install Hugo to review how your changes look before submitting. The easiest way to download Hugo on Linux (Debian/Ubuntu) is through the package manager:
```bash
sudo apt install hugo
```
You can also download and install Hugo from the Hugo releases page [here](https://github.com/gohugoio/hugo/releases). Any recent version of Hugo will work. The **extended version of Hugo is not needed**. Hugo works on all major operating systems and architectures. For even more ways to install Hugo [check the documentation](https://gohugo.io/getting-started/installing).

Check Hugo is installed correctly and check the version by running this command:
```bash
hugo version
```

# 3)  Remove server setup 

To use a remote machine like an AWS EC2 instance, first start up a custom EC2 instance and log into it over ssh. To access the Hugo server on your remote machine, make sure to connect over ssh using port forwarding (use port 1313):
```bash
ssh -L 1313:localhost:1313 user@ip-address
```

Next, install Hugo to review how your changes look before submitting. See the '2) Local computer setup' section above for instructions on how to download and install Hugo.




# Contribution process

Regardless of what computer you are using, with all the pre-requisites installed you are new ready to start contributing content. The content contribution flow will look like this:

With the pre-requisites installed, you can now run hugo to launch the website on your machine.

```bash
hugo server
```

Hugo server will print a message to connect to port 1313

```console
Web Server is available at //localhost:1313/ (bind address 127.0.0.1)
```

Open a browser and go to http://localhost:1313 
