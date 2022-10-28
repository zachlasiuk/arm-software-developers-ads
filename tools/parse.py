#/usr/bin/env python3

import argparse
import logging
import subprocess
import json
import yaml
import os


'''
Parse commands in markdown article and return list of commands
'''
def parse(article):
    with open(article) as file:
        content = file.read()
        file.close()

    cmd = []
    for i in content:
        start = content.find("```") + 3
        end = content.find("```", start)

        if end == start-3:
            # No code section left
            return cmd
        else:
            cmd.append(content[start:end])
            content = content[end+3:-1]


'''
Parse header to check file or not
Returns list with the following elements:
    0: bool value to check the article
    1: int value with number of targets supported
    2: int value with weight of article when in a learning path
'''
def header(article):
    with open(article) as file:
        content = file.read()
        header = []
        for i in content:
            start = content.find("---") + 3
            end = content.find("---", start)
            if end == start-3:
                # No header
                logging.debug("No header found in {}".format(article))
                return [False, -1, -1]
            else:
                header = content[start:end]
                data = yaml.safe_load(header, )
                # Should we test this file?
                if "test_maintenance" in data.keys() and "test_images" in data.keys() and "weight" in data.keys():
                    return [data["test_maintenance"], data["test_images"], data["weight"]]
                if "test_maintenance" in data.keys() and "test_images" in data.keys() and not "weight" in data.keys():
                    # This is not a learning path
                    return [data["test_maintenance"], data["test_images"], -1]
                elif "test_maintenance" in data.keys() and not "test_images" in data.keys():
                    logging.error("\"test_maintenance: true\" requires a list of test_images to run on")
                    return [False, -1, -1]
                elif not "test_maintenance" in data.keys():
                    logging.debug("File {} maintenance is turned off. Add or set \"test_maintenance: true\" otherwise.".format(article))
                    return [False, -1, -1]


'''
Save list of command in json file
'''
def save(article, cmd):
    # Parse file header
    maintain, img, wght = header(article)

    if not maintain:
        logging.info("File {} settings don't enable parsing.".format(article))
        return

    content = { "image": img, "weight": wght}

    logging.debug(content)

    for i_idx,i  in enumerate(cmd):
        l = list(filter(None, i.split("\n")))
        # if bash type, check fo arguments
        if "bash" in l[0]:
            content[i_idx] = {"type": "bash"}
            # check if return code is specified
            if "ret_code" in l[0]:
                ret = l[0].split("ret_code=\"")[1].split("\"")[0]
                content[i_idx].update({"ret_code": ret })
            else:
                content[i_idx].update({"ret_code": "0" })
            # check target
            if "target" in l[0]:
                tgt = l[0].split("target=\"")[1].split("\"")[0]
                content[i_idx].update({"target": tgt })
            # check if any expected result
            if "|" in l[0]:
                expected_result = l[0].split("| ")[1].split("\"")[0]
                content[i_idx].update({"expected": expected_result })
        # for other types, we're assuming source code
        # check if a file name is specified
        else:
            content[i_idx] = {"type": l[0]}
            # check file name
            if "file_name" in l[0]:
                fn = l[0].split("file_name=\"")[1].split("\"")[0]
                content[i_idx].update({"file_name": fn })

        for j_idx,j in enumerate(l[1:]):
            content[i_idx].update({j_idx: j})
            content[i_idx].update({ "ncmd": j_idx+1 })
        content.update({ "ntests": i_idx+1 })

        logging.debug(content[i_idx])

    fn = article + "_cmd.json"
    logging.info("Saving commands to " + fn)

    with open(fn, 'w') as f:
        json.dump(content, f)

