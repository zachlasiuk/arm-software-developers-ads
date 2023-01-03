---
# User change
title: "Contribute: Directory creation"

weight: 4 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
![alt-text #center](2-contribution-process.PNG "Contribution process")


# Adding a new Learning Path

To add a new Learning Path, navigate to the appropriate directory under content/learning-paths in your fork.

There are 5 categories into which you can contribute content:
* server-and-cloud
* desktop-and-laptop
* embedded
* microcontroller
* mobile

{{% notice Note%}}
Place your Learning Path in the category closest to the environment where the software runs. The tags on the [front page of the website](/) help explain the categories. Feel free to ask on GitHub if you are unsure which category best matches your Learning Path. 
{{% /notice %}}


Create a directory for your new Learning Path in the appropriate category. 

For example, to create a new **server-and-cloud** Learning Path:

```
cd content/learning-paths/cloud
mkdir <new-learning-path>
```

Next, copy the files from the provided Learning Path template to modify with your metadata and content. The command is:
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
