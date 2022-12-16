---
# User change
title: "3) Publish request"

weight: 8 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
![alt-text #center](3-publishing-process.PNG "Publishing process")

# Submit your changes to the website

After adding a new learning path and completing your changes, you can run the website locally by running `hugo server` and check that everything looks good.

Commit your changes using git.

Before submitting changes make sure `hugo` runs without errors on the command line. 

```console
hugo
```

To submit your changes for review, follow the GitHub Fork-and-Pull approach and submit the Pull request with your changes to be reviewed and merged.



# Publishing - What to Expect

After submitting a PR (Pull Request), automated checks will run to validate your metadata format and the Arm team will start reviewing your content, mostly for technical accuracy and a lookover of writing style/mistakes. You should expect to recieve a notification that (1) you need to tweak some information, or (2) your content has been accepted and published within a week.

{{% notice Note 1 %}}
If there are small typos or formatting issues, we will fix them before publishing. This is done to reduce the amount of back-and-forth overhead on small issues; you will always be able to view all changes through GitHub and let us know if you object to any changes.
{{% /notice %}}

{{% notice Note 2 %}}
If there are large factual / reproducibility errors in your contribution, we will contact you to resolve them before publishing.
{{% /notice %}}
