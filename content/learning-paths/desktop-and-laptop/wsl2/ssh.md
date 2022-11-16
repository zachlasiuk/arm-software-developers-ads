---
title: SSH to WSL

weight: 4
layout: learningpathall
---


## Run SSH on WSL 

SSH can be used to connect to WSL and to copy files from Windows.

If you only want to copy files between Windows and WSL on the current machine, SSH is not needed. 

WSL automatically mounts the Windows C:\ drive on /mnt/c 

For example, if a file was downloaded using a browser in the Windows Downloads directory and you want to bring it into Linux use the cp command.

Substitute your username and the filename to be copied.

```bash
cp /mnt/c/Users/<username>/Downloads/<filename> .
```

If SSH is needed to access WSL from a different machine continue with the instructions below. 

## Install SSH server

Install the SSH server inside the Linux distribution. 

```bash
sudo apt install openssh-server -y
```

Start the SSH server.

```bash
sudo /etc/init.d/ssh start
```

The SSH server can also be started automatically using systemd. Refer to the [systemd](/learning-paths/desktop-and-laptop/wsl2/systemd/) information in the next section.

Once the SSH server is started, it's possible to ssh from the Windows Command Prompt to WSL. 

Make sure to add the Linux username to the ssh command if the Windows username is different from the Linux username.

```cmd
ssh.exe user@localhost
```

## Change the SSH server port

Sometimes, a higher port is used for the SSH server. 

Modify the SSH config file to change the port number for the SSH server. 

Use port 2022 for SSH instead of the default port 22.

Edit the file /etc/ssh/sshd_config and uncomment the #Port 22 to be just Port 2022

Do the editing from the command line:
```
sudo sed -i -E 's,^#?Port.*$,Port 2022,' /etc/ssh/sshd_config
```

```cmd
ssh user@localhost -p 2022
```

There are two options to SSH from another machine on the local network.

Both of these options need more information. 

# Bridged networking

WSL uses NAT by default. This means the Linux distribution running in WSL will get an IP address starting with 172.X.X.X and not an IP address on the local network. This makes it impossible to SSH to WSL.

One way to get an IP on the local network is to use a bridged network. 

For more information refer to the [short WSL bridging and networking reference](https://github.com/luxzg/WSL2-fixes/blob/master/networkingMode%3Dbridged%20-%20quick%20setup.md)

# Port forwarding

Another way to connect to WSL via SSH is to forward or proxy the Windows port for SSH, such as 2022, to the WSL instance. 

```console
netsh interface portproxy add v4tov4 listenport=$port listenaddress=$addr connectport=$port connectaddress=$remoteport
```



