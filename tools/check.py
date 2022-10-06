#/usr/bin/env python3

import argparse
import logging
import os
import subprocess
import json


'''
Read json file and run commands in Docker
'''
def check(json_file):
    with open(json_file) as jf:
        data = json.load(jf)

    # check if there are many images
    if isinstance(data["image"], list):
        # Start instances for all images
        for i in data["image"]:
            cmd = ["docker run --rm -t -d --name test test_{}{}".format(i, data["image"])]
            logging.debug(cmd)
            subprocess.run(cmd, shell=True)
    else:
        cmd = ["docker run --rm -t -d --name test {}".format(data["image"])]
        logging.debug(cmd)
        subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

    # Create user and configure
    cmd = ["docker exec test apt update"]
    logging.debug(cmd)
    subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    cmd = ["docker exec test apt install sudo"]
    logging.debug(cmd)
    subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    cmd = ["docker exec test useradd user -m -G sudo"]
    logging.debug(cmd)
    subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    cmd = ["docker exec test bash -c \"cat << EOF > /etc/sudoers.d/user\n user ALL=(ALL) NOPASSWD:ALL\nEOF\""]
    logging.debug(cmd)
    subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

    # Run bash commands
    for i in range(0, data["ntests"]):
        t = data["{}".format(i)]
        for j in range(0, t["ncmd"]):
            c = t["{}".format(j)]

            # Check type
            if t["type"] == "bash":
                cmd = ["docker exec -u user -w /home/user test {}".format(c)]
            elif t["type"] == "fortran":
                fn = "hello.f90"
                cmd = ["docker exec -u user -w /home/user test bash -c \"echo '{}' >> {}\"".format(c.replace('\'','\\\"'), fn)]
            else:
                cmd = []

            logging.debug(cmd)

            if cmd != []:
                if "expected" in t.keys():
                    # Do not run output commands
                    if j == int(t["expected"])-1:
                        logging.debug("Don't run command")
                        break
                    else:
                        p = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                else:
                    p = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

                # if success
                if p.returncode == 0:
                    # check with expected result if any
                    if "expected" in t.keys():
                        exp = t["{}".format(int(t["expected"])-1)]
                        if exp == p.stdout:
                            logging.info("{}: ok".format(cmd))
                        else:
                            logging.info("{}: ERROR (unexpected output. Expected {} but got {})".format(cmd, exp, p.stdout))
                    else:
                        logging.info("{}: ok".format(cmd))
                else:
                    logging.info("{}: ERROR (command failed)".format(cmd))

    # Stop instance
    cmd = ["docker stop test"]
    logging.debug(cmd)
    subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)


