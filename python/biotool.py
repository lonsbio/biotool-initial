import logging
import time
import datetime
import re
import os
import sys

def subcommand1(args):
    """
    Subcommand1
    """
    print("This is subcommand1")

def subcommand2(args):
    """
    Subcommand2
    """
    print("This is subcommand2")

def echo(args):
    """
    echo
    """
    print("No subcommands given. use -h or --help for a list of subcommands")


def info(args):
    """
    Function to print to STDERR to ask for a subcommand, unless doi or citation information is required
    """

    doi_text = "doi:10.1186/2047-217X-2-15"

    citation_text = """
Seemann, T. (2013).
Ten recommendations for creating usable bioinformatics command line software.
GigaScience, 2, 15. doi:10.1186/2047-217X-2-15
        """

    if(args.doi):
        print("{} {}".format(sys.argv[0] , doi_text))
    elif(args.citation):
        print("{} \n {}".format(sys.argv[0],citation_text))
    else:
        print("A subcommand is required. Use -h or --help for more information.")

def main():


    import argparse
    parser = argparse.ArgumentParser()
    logginggroup = parser.add_mutually_exclusive_group()
    logginggroup.add_argument('--debug', action='store_true', help='include debug information in log')
    logginggroup.add_argument('--verbose', action='store_true',help='include extra information in log')
    logginggroup.add_argument('--quiet', action='store_true',help='include only errors in log')

    parser.add_argument('--logfile', type=str, help='log filename')
    parser.add_argument('-v','--version', action='version', version='%(prog)s 1.0')
    

    subparsers = parser.add_subparsers(help='subcommands of %(prog)s',                                       title='subcommands')

    #citation information
    parser_info = subparsers.add_parser('info', help='get citation info')
    parser_info.add_argument('--citation', action='store_true', default=True, help='display citation only')
    parser_info.add_argument('--doi', action='store_true',help='display doi only')
    parser_info.set_defaults(func=info)

    #subcommmand 1
    parser_subcommand1 = subparsers.add_parser('subcommand1', help='do tasks required for subcommand1')
    parser_subcommand1.add_argument('files',nargs='*', type=argparse.FileType('r'), default=sys.stdin,help="input files")
    parser_subcommand1.set_defaults(func=subcommand1)

    #subcommmand 2
    parser_subcommand2 = subparsers.add_parser('subcommand2', help='do tasks required for subcommand2')
    parser_subcommand2.add_argument('files',nargs='*', type=argparse.FileType('r'), default=sys.stdin,help="input files")
    parser_subcommand2.set_defaults(func=subcommand2)

    args = parser.parse_args()


    if (args.debug):
        loglevel=logging.DEBUG
    elif(args.verbose):
        loglevel=logging.INFO
    elif(args.quiet):
            loglevel=logging.ERROR
    else:
        loglevel=logging.WARNING

    if (args.logfile):
        logging.basicConfig(filename=args.logfile,level=loglevel,
                            format='%(asctime)s %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
    else:
        logging.basicConfig(filename='{}_{}.log'.format(sys.argv[0],
                            datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S')),level=loglevel,format='%(asctime)s %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')

    args.func(args)

if __name__ == "__main__":
    main()
