#!/usr/bin/env python3

import argparse
import logging
import os
# Local import
import report
import parse
import check


# Set default verbosity level
verbosity = logging.INFO
# [debugging] Verbosity settings
level = { 10: "DEBUG",  20: "INFO",  30: "WARNING",  40: "ERROR" }


'''
Main function
'''
def main():
    global verbosity, level

    arg_parser = argparse.ArgumentParser(description='Maintenance tool.', prefix_chars='-')
    arg_parser.add_argument('-v', '--version', action='version', version='Maintenance toolkit version 0.1', help='Display software version')
    arg_parser.add_argument('-d', '--debug', action='store_true', help='Enable debugging messages')
    arg_parser.add_argument('-l', '--link', metavar='URL', action='store', type=str, help='URL to github actions report. Used wen patching sources files with --check')

    arg_group = arg_parser.add_mutually_exclusive_group()
    arg_group.add_argument('-p', '--parse', metavar='FILE', action='store', type=str, help='Parse console commands in FILE. FILE can be a CSV file with the list of file or a markdown file. Output a JSON file.')
    arg_group.add_argument('-c', '--check', metavar='DEST', action='store', type=str, help='DEST can be a JSON file or a folder. Check commands produced by the --parse switch. Output an Junit XML file with test results.')
    arg_group.add_argument('-r', '--report', metavar='DAYS', action='store', type=int, default=1, help='List articles older than a period in days (default is 1). Output a CSV file. This option is used by default.')

    args = arg_parser.parse_args()

    if args.debug:
        verbosity = logging.DEBUG

    logging.basicConfig(format='[%(levelname)s]\t%(message)s', level = verbosity)
    logging.debug("Verbosity level is set to " + level[verbosity])

    if args.check:
        if args.check.endswith("_cmd.json"):
            logging.info("Checking " + args.check)
            res = check.check(args.check)
            res = {'ubuntu:latest': 1, 'fedora:latest': 1}
            logging.info("Patching " + args.check.replace("_cmd.json", "") + " with test results")
            check.patch(args.check.replace("_cmd.json", ""), res, args.link)
        elif os.path.isdir(args.check):
            logging.info("Checking folder for _cmd.json files" + args.check)
            l = os.listdir(args.check)
            for i in l:
                if i.endswith("_cmd.json"):
                    logging.info("Found json. Checking " + i)
                    res = check.check(args.check + "/" + i)
                    logging.info("Patching " + i.replace("_cmd.json", "") + " with test results")
                    check.patch(i.replace("_cmd.json", ""), res, args.link)
        else:
            logging.error("Parsing expects a .md file or a .csv list of files")
    elif args.parse:
        # check if article is a csv file corresponding to a file list
        if args.parse.endswith(".csv"):
            logging.info("Parsing CSV " + args.parse)
            with open(args.parse) as f:
                next(f)
                for line in f:
                    fn = line.split(",")[0]
                    logging.debug("Parsing " + fn)
                    cmd = parse.parse(fn)
                    parse.save(fn, cmd)
        elif args.parse.endswith(".md"):
            logging.info("Parsing " + args.parse)
            cmd = parse.parse(args.parse)
            parse.save(args.parse, cmd)
        else:
            logging.error("Parsing expects a .md file or a .csv list of files")
    elif args.report:
        logging.info("Creating report of articles older than {} days".format(args.report))
        report.report(args.report)


if __name__ == "__main__":
    main()
