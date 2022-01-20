#!/usr/bin/python
import argparse
import re

### Script Arguments
def define_argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p','--pattern',required=True)
    parser.add_argument('-r','--require',nargs='*', required=False) # if empty = args.require is None

    parser.add_argument('-s','--source_file',nargs='?',required=True)
    parser.add_argument('-d','--dest_file',nargs='?',required=False)

    parser.add_argument('-v','--verbose',action='store_true')
    return parser

def find_wordles(regex_pattern,required_letters,source_file,is_verbose):
    wordles = []

    with open(source_file, 'r') as f:
        for word in f:
            word = word.strip()
            include_word = True
            
            if(re.match(regex_pattern,word)):
                if(is_verbose):
                    print(f"Matched word: {word} with pattern: {regex_pattern}")
                
                # Word has matched, now make sure includes required letters
                if required_letters is not None:
                    for letter in required_letters:
                        if(letter not in word):
                            if(is_verbose):
                                print(f"Word {word} does not contain letter {letter}")
                            include_word = False
                
                if (include_word):
                    wordles.append(word)

    return wordles

def print_wordles(wordle_list,destination_file,is_verbose):
    if(is_verbose):
        print(f"Found Wordles:")
        for wordle in wordle_list:
            print(wordle)

def main():
    # Get the args
    args = define_argument_parser().parse_args()
    wordles = find_wordles(args.pattern,args.require,args.source_file,args.verbose)
    print_wordles(wordles,args.dest_file,args.verbose)

if __name__ == "__main__":
    main()
