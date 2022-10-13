#/usr/bin/env python3

import argparse
import logging
import os
import subprocess
import json
from junit_xml import TestSuite, TestCase


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

    logging.info("Container initialization completed")

    # Run bash commands
    test_cases= []
    for i in range(0, data["ntests"]):
        t = data["{}".format(i)]
        for j in range(0, t["ncmd"]):
            c = t["{}".format(j)]

            # Check type
            if t["type"] == "bash":
                cmd = ["docker exec -u user -w /home/user test {}".format(c)]
            elif t["type"] == "fortran":
                # TODO filename should probably read from the markdown files
                fn = "hello.f90"
                cmd = ["docker exec -u user -w /home/user test bash -c \"echo '{}' >> {}\"".format(c.replace('\'','\\\"'), fn)]
            elif t["type"] == "C":
                fn = "hello-world.c"
                cmd = ["docker exec -u user -w /home/user test bash -c \"echo '{}' >> {}\"".format(c.replace('\'','\\\"').replace('\"','\\\"'), fn)]
            else:
                cmd = []

            logging.debug(cmd)

            if cmd != []:
                if "expected" in t.keys():
                    # Do not run output commands
                    if j == int(t["expected"])-1:
                        logging.debug("{}: Expected output. Not running command.")
                        break
                    else:
                        p = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                else:
                    p = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

                # create test case
                test_cases.append(TestCase("Test-{}.{}".format(i,j), c, 0, p.stdout.rstrip().decode("utf-8"), ''))

                # if success
                if p.returncode == 0:
                    # check with expected result if any
                    if "expected" in t.keys():
                        exp = t["{}".format(int(t["expected"])-1)]
                        # strip out '\n' and decode byte to string
                        if exp == p.stdout.rstrip().decode("utf-8"):
                            msg = "{}: ok".format(c)
                        else:
                            msg = "{}: ERROR (unexpected output. Expected {} but got {})".format(c, exp, p.stdout.rstrip().decode("utf-8"))
                            test_cases[-1].add_failure_info(msg)
                    else:
                        msg = "{}: ok".format(c)
                else:
                    msg = "{}: ERROR (command failed. Return code is {})".format(c, p.returncode)
                    test_cases[-1].add_failure_info(msg)

                logging.debug(msg)
                #print("*", end = '')
                logging.info("{:.0f}% of all tests completed".format(i/data["ntests"]*100))
                #print("*", end = '')

    logging.info("100% of all tests completed")

    # add to test suite and write junit results
    ts = [TestSuite(json_file, test_cases)]
    with open(r'check_results.xml', mode='w') as lFile:
        TestSuite.to_file(lFile, ts, prettyprint=True)
        lFile.close()
        logging.info("Results written in check_results.xml")

    # Stop instance
    logging.info("Terminating container...")
    cmd = ["docker stop test"]
    logging.debug(cmd)
    subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)


