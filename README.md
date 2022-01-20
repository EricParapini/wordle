# Wordle Word Search

A simple assistant for the new wordle game. Allows you to specify a regex pattern based off information the game provides as well as the ability to specify required letters in the word ("yellow" hints). 

This repository comes with a provided dictionary of five letter words - users are free to specify their own source file instead. 

Currently only works in verbose mode - no other output implemented at the moment. 

## Arguments
-p / --pattern      regex pattern to match
-r / --require      letters that must appear anywhere in the word - input individually as 'a' 'b' 'c' etc.
-s / --source_file  path to dictionary file to look up against
-d / --dest_file    - CURRENTLY UNUSED - path to destination file to output identified wordles
-v / --verbose      Print matching results to terminal, ends with identified wordles

## Usage Example
./wordle.py -s ./words.txt -p '[^c][^bde][^cde][f][^de]' -r a l o -v

This would the program to match with words that has:
- First letter is not an 'c'
- Second letter is not 'b' 'd' or 'e'
- Third letter is not 'c' 'd' or 'e'
- Fourth letter is 'f'
- Fifth letter is not 'd' or 'e'

As well as have the letters 'a' 'l' or 'o' anywhere in the word.

This identifies the following wordles:
- aloft
- loafs
- loofa
- solfa