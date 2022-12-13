# Arm Learning Paths (prototype project)

GitHub source for the Arm Learning Paths static website, serving learning-based technical content for Arm software developers. 
This README contains two things:
1. 'How To Contribute' step-by-step guide
2. Documentation on the website's architecture

# How To Contribute, a step-by-step guide

All contributions are welcome from individuals passionate about developing technology on Arm. 
This is the 3-step process to contribute:

### Verify if your idea is appropriate for a learning path, and how to add a new directory for your learning path.
  - Explained in the ['how to contribute' learning path](http://www.armswdev.tk/learning-paths/cross-platform/_example-learning-path/)
### Fork the GitHub repository and add your learning path, checking how your content looks by running the website locally.
  - You can add content locally or via Gitpod (recommended); both methods are explained in this document.
  - View tips for formatting content, adding metadata, and writing style guidelines also in the ['how to contribute' learning path](http://www.armswdev.tk/learning-paths/cross-platform/_example-learning-path/)
### Submit a pull request
  - Your content will be reviewed and published shortly!


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
 
