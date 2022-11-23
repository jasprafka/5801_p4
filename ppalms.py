import os
import sys
import argparse
from SourceAnnotator import SourceAnnotator

from time import sleep

_DESCRIPTION = ""

_BAD_INPUT = "\t-- Error, your input must be a valid number!"
_BAD_SELECTION = "\t-- Error, your input must be only valid line numbers!"

_MAIN_MENU = (
    "1. Exit\n"
    "2. Print this menu\n"
    "3. Show file\n"
    "4. Strip line comments\n"
    "5. Select lines\n"
    "6. Show selected lines\n"
    "7. Create Tuple\n"
    "8. Get Tuples\n"
)

_SELECT_LINES_MENU = (
    "Enter your selection as line numbers separated by spaces\n"
    "e.g. - \n1 2 5 7 10\n"
    "\nYour line selection: "
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

# ----------- BEGIN OPTION FUNCTIONS -----------
"""
The following option functions all have the same 
syntax. They take a SourceAnnotator object as their
only argument and return a boolean. This way, the 
functions can be indexed in a dictionary and the user
can very easily select the function they want to run.
"""
def print_menu(unused_annotator) -> bool:
    """Print the options menu.

    args:
        unused_annotator: (SourceAnnotator) Pointer to SourceAnnotator instance.
            This function does not use the SourceAnnotator instance.
    
    returns:
        (bool) Returns false so main ppalms loop continues.
    """
    print(_MAIN_MENU)
    return False

def exit_ppalms(unused_annotator) -> bool:
    """Exit the main ppalms loop.

    args:
        unused_annotator: (SourceAnnotator) Pointer to SourceAnnotator instance.
            This function does not use the SourceAnnotator instance.
    
    returns:
        (bool) Returns True so main ppalms loop exits.
    """
    print("Goodbye!")
    return True

def show_file(annotator) -> bool:
    """Print the contents of annotator._file_lines with line numbers.

    args:
        annotator: (SourceAnnotator) Pointer to SourceAnnotator instance
    
    returns:
        (bool) Returns false so main ppalms loop continues.
    """
    print_string = "\n"
    lines = annotator.get_lines()
    for line_num, line in enumerate(lines):
        print_string += f'{line_num} {line}'
    print(print_string)
    return False


def strip_comments(annotator) -> bool:
    """Strip all line comments from annotator._file_lines.

    args:
        annotator: (SourceAnnotator) Pointer to SourceAnnotator instance
    
    returns:
        (bool) Returns false so main ppalms loop continues.
    """
    annotator.strip_comments()
    print("\t-- Line comments stripped!")
    return False


def show_selected_lines(annotator) -> bool:
    """Print the array indicating which lines are selected.

    args:
        annotator: (SourceAnnotator) Pointer to SourceAnnotator instance
    
    returns:
        (bool) Returns false so main ppalms loop continues.
    """
    selected_lines = annotator.get_selected_lines()
    if selected_lines:
        print(f"\t-- Selected Lines: {selected_lines}")
    else:
        print("\t-- No lines selected!")

    return False


def select_lines(annotator) -> bool:
    """
    args:
        annotator: (SourceAnnotator) Pointer to SourceAnnotator instance
    
    returns:
        (bool) Returns false so main ppalms loop continues.
    """
    show_file(annotator)
    done = False
    while not done:
        user_input = input(_SELECT_LINES_MENU)
        selected_lines = user_input.split()
        good_input = [line.isdigit() for line in selected_lines]
        if not all(good_input):
            print(_BAD_SELECTION)
            if input("Try again? (y/n): ") != 'y':
                done = True
        else:
            annotator.select_lines([int(line) for line in selected_lines])
            show_selected_lines(annotator)
            done = True

    return False


def create_tuple(annotator) -> bool:
    """Create a tuple from annotator._selected_lines if it is not None.

    args:
        annotator: (SourceAnnotator) Pointer to SourceAnnotator instance
    
    returns:
        (bool) Returns false so main ppalms loop continues.
    """
    selected_lines = annotator.get_selected_lines()
    if not selected_lines:
        print("\t-- No lines selected!")
    else:
        
        new_tuple = tuple(selected_lines) 
        if new_tuple in annotator.get_tuples():
            already_created = input(f"\t-- Tuple {new_tuple} already created. Create it again? (y/n):")
            if already_created != 'y':
                return False

        print(f"\t-- Created tuple {annotator.create_tuple()}")
    return False
    

def get_tuples(annotator) -> bool:
    """Print the line tuples in annotator._line_tuples.

    args:
        annotator: (SourceAnnotator) Pointer to SourceAnnotator instance
    
    returns:
        (bool) Returns false so main ppalms loop continues.
    """
    tuples = annotator.get_tuples()
    if not tuples:
        print("\t-- No tuples created!")
    else:
        print(f"\t-- {tuples}")
    
    return False
# ----------- END OPTION FUNCTIONS -----------


def main_loop(annotator):
    done = False
    user_input = None

    _FUNCTIONS = {
        "1" : exit_ppalms,
        "2" : print_menu,
        "3" : show_file,
        "4" : strip_comments,
        "5" : select_lines,
        "6" : show_selected_lines,
        "7" : create_tuple,
        "8" : get_tuples
    }

    print_menu(None)
    while not done:
    
        user_input = input("What would you like to do?\nYour choice: ").split()[0]
        if not user_input.isdigit() or not _FUNCTIONS.get(user_input):
            print(_BAD_INPUT)
            continue
        done = _FUNCTIONS.get(user_input)(annotator)

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