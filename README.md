# Arm Software Developers (prototype project)

This prototype site uses a custom Arm theme for [Hugo](https://gohugo.io/) to create a static website with easy navigation and structure for learning-based technical content for Arm software developers. The content is created in markdown and stored on GitHub. GitHub Actions are used to update the website automatically when changes are made.

The project is open to anyone who wishes to improve or create content for other Arm software developers.

## Getting started

There are two ways to create new content or make changes to the existing content.
- Run hugo on your local computer (or a remote server you control via ssh)
- Use Gitpod for cloud development

For local operation, make sure you have [git installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and start by cloning the project.

If you are planning to make a contribution you should fork the repository first to your GitHub account and then clone your fork. 

After the changes are completed use a pull request to submit the proposed changes.

Substitute your GitHub account name if you are cloning a fork.

```bash
git clone https://github.com/zachlas/arm-software-developers-ads
```

You can now edit and create new content.

To see how your changes look, run the website locally.

## Running the website locally

Building and running the site locally requires [Hugo](https://gohugo.io). Download and install Hugo from the Hugo releases page [here](https://github.com/gohugoio/hugo/releases). Any recent version of Hugo will work. The **extended version of Hugo is not needed**. Hugo works on all major operating systems and architectures.

You can also install Hugo on Linux using a package manager. 

For Debian/Ubuntu use:

```bash
sudo apt install hugo
```

For even more ways to install Hugo [check the documentation](https://gohugo.io/getting-started/installing).

To see the version of Hugo:

```bash
hugo version
```

If Hugo is installed on a remote Linux machine and you are using ssh to connect, forward port 1313.

```bash
ssh -L 1313:localhost:1313 user@ip-address
```

With the pre-requisites installed, you can now run hugo to launch the website on your machine.

```bash
hugo server
```

Hugo server will print a message to connect to port 1313

```console
Web Server is available at //localhost:1313/ (bind address 127.0.0.1)
```

Open a browser and go to http://localhost:1313 


## Develop using [Gitpod](https://www.gitpod.io/)

Instead of installing tools on your local machine, you can create and modify content directly in Gitpod.

Install the [Gitpod Chrome Extension](https://chrome.google.com/webstore/detail/gitpod-always-ready-to-co/dodmmooeoklaejobgleioelladacbeki) which installs a Gitpod button in the GitHub project. You can also prefix the URL for the GitHub project (or your fork of the project) with gitpod.io/#

[Open this repository in Gitpod](https://gitpod.io/#github.com/zachlas/arm-software-developers-ads)

You can use your GitHub credentials to login to Gitpod and use the Free plan which offers up to 50 hours per month.

## Adding new learning-paths to the website

Start by forking and cloning the repository. 

To add new learning paths, navigate to the appropriate directory under content/learning-paths in your fork.

There are 5 different areas into which you can contribute content

* cloud
* desktop_and_laptop
* embedded
* microcontroller
* mobile

Create a directory for your new learning path in the appropriate area.

For example to create a new cloud based learning path

```
cd content/learning-paths/cloud
mkdir <new-learning-path>
```

You will then add the following markdown files in the <new-learning-path> directory

* _index.md - This file contains information like the title, target audience for the new learning path. There are comments in the file to help you fill in the content apropriately. You will also need to follow the guidance in the comments to add the appropriate tags for your learning path.
* <how-to-1>.md - This markdown file contains the how-to content for the learning-path. You can have multiple how-to guides in a learning path. Name this file to reflect the content you are adding.
* _review.md - This file contains simple question/answers to check the knowledge take away from the learning path. 
* _next_steps.md - This file contains the next recommended steps for the reader to follow on completion of this learning path.

To make this easier, there is a template provided for all these files. You can copy the files from the template into your <new-learning-path> directory and modify.

For example:

```bash
cd <new-learning-path>
cp -r cp -r ../../../../learning-path_templates/* .
```

## Adding images 

To add images to your content use markdown syntax.

```console
![alt tex](image-name)
```

For learning paths put the images in the same directory as your learning path. 

For tool installs, put the images in the _images/ directory. For example, 
```console
![my image](/install-tools/_images/my-image.png)
```

## Adding YouTube videos

To add YouTube videos use the following shortcode.

Find the YouTube ID in the URL for by clicking Share in YouTube and copying the ID.

```console
{{< youtube-nocookie _PKNbBeAB2M>}}
```

## Submit your changes to the website

After adding a new learning path and completing your changes, you can run the website locally by running `hugo server` and check that everything looks good.

Commit your changes using git.

To submit your changes for review, follow the GitHub Fork-and-Pull approach and submit the Pull request with your changes to be reviewed and merged.
