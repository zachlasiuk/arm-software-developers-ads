---
# User change
title: "2a) Contribute: Directory creation"

weight: 4 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
![alt-text #center](2-contribution-process.PNG "Contribution process")


# Adding a new Learning Path to the website

To add new learning paths, navigate to the appropriate directory under content/learning-paths in your fork.

There are 5 different categories into which you can contribute content:
* server-and-cloud
* desktop-and-laptop
* embedded
* microcontroller
* mobile

{{% notice Note%}}
Your Learning Path should live in the category it is targeting software development for. For example, say you are writing a Learning Path about streamlining Embedded software development by using cloud-based Cortex-M virtualizing tools (like Arm Virtual Hardware). That Learning Path belongs under the 'Embedded' category as it is using cloud tools but is **targeting** embedded devices.
{{% /notice %}}


Create a directory for your new learning path in the appropriate category. For example to create a new **server-and-cloud** based learning path:

```
cd content/learning-paths/cloud
mkdir <new-learning-path>
```

Next, copy the files from the provided learning path template to modify with your metadata and content. The command is:
```bash
cd <new-learning-path>
cp -r cp -r ../../../../learning-path_templates/* .
```

This will then add the following markdown files in the **new-learning-path** directory:


| Files                 | Details |
|---------------        |----------|
| _index.md             | This file contains information like the title, target audience, and tagging metadata for your new Learning Path. The next step of this Learning Path explains these metadata elements and how to fill them out properly. |
| _review.md            | This file contains simple questions and answers to reinforce knowledge gained from your Learning Path.    |
| _next_steps.md        | This file contains the next recommended steps and related resources for the reader to follow on completion of this Learning Path.   |
| **how-to-1.md**       | This file contains the how-to content for the Learning Path. You can have multiple how-to guides in your Learning Path, with each **how-to-N.md** file representing another distinct step in your tutorial. Name this file to reflect the content you are adding. |
| **any-pictures.png**  | (optional) Pictures and screenshots can be included in this directory to appear in your Learning Path (images can also be referenced as web links if desired). |
