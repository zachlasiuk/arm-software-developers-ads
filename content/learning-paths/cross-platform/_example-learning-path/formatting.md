---
# User change
title: "Content formatting - code, images, videos"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Code Snippets
xyz

## Images

You can add images in the standard markdown format. Provide alternative text (displayed if the image cannot load) in brackets followed by the image source and subtitle in parenthesis. Simple example:

![example image alt-text#center](arm-pic.png "Figure 1. Example image caption")

These are the range of options to add an image:
- Hosting
    - Local
    - External
- Alignment
    - Left-aligned (default)
    - Center-aligned

### Image Hosting (internal or external)
Internal hosting is straightfoward. Add the picture (.png or .jpeg format) into the learning path directory alongside the *.md files, and refer to it by name. This example is using 'arm-pic.png' which you can find in this directory:

![Arm sample pic](arm-pic.png "Figure 2. Local hosting example")

External image referencing is also simple. Obtain the picture link and place that as the source. Example:

![Arm sample pic](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSuMSonKjWrTHvrR00sIUfPtOAxJ-RjUKmWUqCai5hMWC6MiHq8ZsUYBDWYDQ1WsjTb2e4&usqp=CAU "Figure 4. External hosting example")

### Image Alignment (center or left) 

Left-alignment is the default image behavior. 
To center an image, add '#center' at the end of the alt-text and the image + subtitle will center on the page.

Center aligned:
![alt-text #center](arm-pic.png "Figure 5. Centered example")

### Image Sizing
Images are displayed in their specified size. To shrink an image, download the image, modify the size, and host the image locally.

