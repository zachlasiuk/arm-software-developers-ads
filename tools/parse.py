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
                return [False, -1]
            else:
                header = content[start:end]
                data = yaml.safe_load(header, )
                # Should we test this file?
                if "maintain" in data.keys() and "docker_images" in data.keys():
                    return [data["maintain"], data["docker_images"]]
                elif "maintain" in data.keys() and not "docker_images" in data.keys():
                    logging.error("\"maintain: true\" requires a list of docker_images to run on")
                    return [False, -1]
                else:
                    logging.debug("File {} maintenance is turned off. Add or set \"maintain: true\" otherwise.".format(article))
                    return [False, -1]


'''
Save list of command in json file
'''
def save(article, cmd):
    # Parse file header
    maintain, img = header(article)

    if not maintain:
        logging.info("File {} settings don't enable parsing.".format(article))
        return

    content = { "image": img}

    logging.debug(content)

    for i_idx,i  in enumerate(cmd):
        l = list(filter(None, i.split("\n")))
        # if bash type, check fo arguments
        if "bash" in l[0]:
            content[i_idx] = {"type": "bash"}
            # check target
            if "target" in l[0]:
                tgt = l[0].split("target=\"")[1].split("\"")[0]
                content[i_idx].update({"target": tgt })
            # check if any expected result
            if "|" in l[0]:
                expected_result = l[0].split("| ")[1].split("\"")[0]
                content[i_idx].update({"expected": expected_result })
        # if bash type, check fo arguments
        elif "C" in l[0] or "fortran" in l[0]:
            content[i_idx] = {"type": l[0].split()[0]}
            # check file name
            if "file_name" in l[0]:
                fn = l[0].split("file_name=\"")[1].split("\"")[0]
                content[i_idx].update({"file_name": fn })

        # no expected argument for other types
        else:
            content[i_idx] = {"type": l[0]}

        for j_idx,j in enumerate(l[1:]):
            content[i_idx].update({j_idx: j})
            content[i_idx].update({ "ncmd": j_idx+1 })
        content.update({ "ntests": i_idx+1 })

        logging.debug(content[i_idx])

    fn = article + "_cmd.json"
    logging.info("Saving commands to " + fn)

    with open(fn, 'w') as f:
        json.dump(content, f)

