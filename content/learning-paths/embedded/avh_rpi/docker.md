---
# User change
title: "Docker"

weight: 7 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Docker

Install Docker using the universal Linux instructions and check it works by running the hello-world image:

```console
curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh
sudo usermod -aG docker $USER
newgrp docker
docker run hello-world
```

Try out some Docker projects to confirm they build and run as expected. Some simple ones are in GitHub in a [project called hello-arm](https://github.com/jasonrandrews/hello-arm). 

Also try out official images from Docker Hub such as Ubuntu. None of the projects detect anything different about the virtual Raspberry Pi 4 and performance is better than the physical Raspberry Pi in all cases. 

It’s also possible to build and run 32-bit Arm containers on the virtual Raspberry Pi.


## Summary 

Docker works well on the virtual Raspberry Pi. No differences are detected, and performance is faster than the physical Raspberry Pi. 


