#!/usr/bin/env python3

import argparse
import logging
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

    arg_group = arg_parser.add_mutually_exclusive_group()
    arg_group.add_argument('-p', '--parse', metavar='FILE', action='store', type=str, help='Parse console commands in FILE. FILE can be a CSV file with the list of file or a markdown file. Output a JSON file.')
    arg_group.add_argument('-c', '--check', metavar='JSON', action='store', type=str, help='Check command from JSON file produced by the --parse switch')
    arg_group.add_argument('-r', '--report', metavar='DAYS', action='store', type=int, default=1, help='List articles older than a period in days (default is 1). Output a CSV file. This option is used by default.')

    args = arg_parser.parse_args()

    if args.debug:
        verbosity = logging.DEBUG

    logging.basicConfig(format='[%(levelname)s]\t%(message)s', level = verbosity)
    logging.debug("Verbosity level is set to " + level[verbosity])

    if args.check:
        logging.debug("Checking " + args.check)
        check.check(args.check)
    elif args.parse:
        logging.debug("Parsing " + args.parse)
        cmd = parse.parse(args.parse)
        parse.save(args.parse, cmd)
    elif args.report:
        logging.debug("Creating report of articles older than {} days".format(args.report))
        report.report(args.report)


if __name__ == "__main__":
    main()
