# Arm Learning Paths (prototype project)

GitHub source for the Arm Learning Paths static website, serving learning-based technical content for Arm software developers. 
This README contains two things:
1. 'How To Contribute' step-by-step guide
2. Documentation on the website's architecture

<br/>

# How To Contribute, a step-by-step guide

All contributions are welcome from individuals passionate about developing technology on Arm. 
This is the 3-step process to contribute:

### 1) Check if your content is appropriate for a Learning Path
  - Explained in the ['how to contribute' learning path](http://www.armswdev.tk/learning-paths/cross-platform/_example-learning-path/)

### 2) Fork the GitHub repository, add your Learning Path
  - You can add content locally or via Gitpod (recommended); both methods are explained in this document.
  - View tips for creating your new learning path, formatting content, adding metadata, and writing style guidelines also in the ['how to contribute' learning path](http://www.armswdev.tk/learning-paths/cross-platform/_example-learning-path/)

### 3) Submit a pull request
  - Your content will be reviewed and published shortly!

If you have questions about this process please reach out to Arm-Tool-Solutions@arm.com

<br/>
<br/>
<br/>

# Website documentation

This site is built on the [Hugo](https://gohugo.io/) web framework, ideal for generating static websites. Below is a brief description of the key files/directories of this website:

/
  * /content
    * where all learning path content is located.
  * /themes
    * where the html elements are defined that renders /content files into stylized HTML.
  * /tools
    * python scripts that automatically check for website integrety.
  * LICENSE files
    * where the license information is contained.
  * config.toml
    * where the high-level website configuration settings are defined.
 
