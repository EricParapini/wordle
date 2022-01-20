#!/usr/bin/python
import argparse
import re

### Script Arguments
def define_argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p','--pattern',required=True)
    parser.add_argument('-r','--require',nargs='*', required=False) # if empty = args.require is None

    parser.add_argument('-s','--source_file',nargs='?',required=True)
    parser.add_argument('-d','--dest_file',nargs='?',required=True)

    parser.add_argument('-v','--verbose',action='store_true')
    return parser

def find_wordles(regex_pattern,required_letters,source_file,is_verbose):
    with open(source_file, 'r') as f:
        for row in f:
            print(row)

def print_wordles(wordle_list,destination_file,is_verbose):
    pass

def main():
    # Get the args
    args = define_argument_parser().parse_args()
    wordles = find_wordles(args.pattern,args.require,args.source_file,args.verbose)

if __name__ == "__main__":
    main()
