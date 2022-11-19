import os
import sys
import argparse
from SourceAnnotator import SourceAnnotator

from time import sleep

_DESCRIPTION = ""

_BAD_INPUT = "\t-- Sorry, your input must be a valid number!"

_MENU = (
    "\nWhat would you like to do?\n"
    "1. Exit\n"
    "2. Print this menu\n"
    "3. Show file\n"
    "4. Strip line comments\n"
    "5. Select lines\n"
    "6. Show selected lines\n"
    ". Create Tuple\n"
    ". Get Tuples\n"
    ". Show selected lines"
)

def _parse_args(argv):
    parser = argparse.ArgumentParser(
        prog="ppalms.py",
        description=_DESCRIPTION
    )
    parser.add_argument(
        "path",
        help="Path to the file to be uploaded."
    )

    args = parser.parse_args()

    if not os.path.exists(args.path):
        print(f"File {args.path} not found!")
        return None

    return args

def print_menu(unused_annotator):
    print(_MENU)

def exit_ppalms(unused_annotator):
    print("Goodbye!")
    exit()

def show_file(annotator):
    print_string = "\n"
    lines = annotator.get_lines()
    for line_num, line in enumerate(lines):
        print_string += f'{line_num} {line}'
    print(print_string)

def strip_comments(annotator):
    annotator.strip_comments()
    print("\t-- Line comments stripped!")

def select_lines(annotator):
    print("can't do this yet!")
    pass

def show_selected_lines(annotator):
    selected_lines = annotator.get_selected_lines()
    if selected_lines:
        print(f"\t-- {selected_lines}")
    else:
        print("\t-- No lines selected!")
    

def main_loop(annotator):
    done = False
    user_input = None

    _FUNCTIONS = {
        "1" : exit_ppalms,
        "2" : print_menu,
        "3" : show_file,
        "4" : strip_comments,
        "5" : select_lines,
        "6" : show_selected_lines
    }

    print_menu(None)
    while not done:
        user_input = input("Your choice: ")
        if not user_input.isdigit():
            print(_BAD_INPUT)
            continue
        
        if not _FUNCTIONS.get(user_input):
            print(_BAD_INPUT)
            continue

        _FUNCTIONS.get(user_input)(annotator)

def main(argv):
    args = _parse_args(argv)
    if not args:
        return
    
    annotator = SourceAnnotator()
    if not annotator.upload_file(args.path):
        return
    main_loop(annotator)
    

if __name__ == "__main__":
    main(sys.argv[1:])