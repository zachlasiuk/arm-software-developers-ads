# Prototype site for Arm Software Developers

This prototype site uses a custom Arm Design System theme with [Hugo](https://gohugo.io/), providing easy site navigation and structure for learning-based technical content.


## Getting started

To work on the project start by cloning the project and run locally.

```bash
git clone --recurse-submodules https://github.com/zachlas/arm-software-developers-ads
```

```bash
npm install
```

You can now edit your own versions of the site’s source files. 

To see your changes, run the website locally.

## Running the website locally

Building and running the site locally requires the **extended version** of [Hugo](https://gohugo.io).

You will also need to install npm, golang, PostCSS and Node.js. Follow the installation instructions [here](https://www.docsy.dev/docs/get-started/docsy-as-module/installation-prerequisites/)

With all the pre-requisites installed, you can now run the command below to launch the website locally on your machine

```bash
hugo server
```

## Adding new learning-paths to the website

Start by forking the repository. To add new learning paths to the website, navigate to the appropriate directory under content/learning-paths in your fork

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

## Submit your changes to the website

After adding a new learning path and completing all your changes, you can run the website locally by running `hugo server` and check if everything looks good.
To submit your changes to the website, follow the GitHub Fork-and-Pull approach and submit the Pull request with your changes to be reviewed/merged by the Admin




