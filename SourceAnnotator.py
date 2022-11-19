import re
import os

_LANG_COM_SYMS = {
    "cpp": "//",
    "c": "//",
    "h": "//",
    "hpp": "//",
    "js": "//",
    "py": "#",
    "r": "#",
    "R": "#"
}

def remove_line_comments(lines, comment_symbol) -> list:

    # If system could not remove line comments, just return all lines
    if not comment_symbol:
        return lines

    # Regex for finding single line comments.
    _LINE_COMMENT = re.compile(f'\\s*{comment_symbol}+.*', flags=re.DOTALL)

    new_lines = []
    for line in lines:
        # Only append lines that are not comments
        if not _LINE_COMMENT.match(line):
            new_lines.append(line)
    return new_lines

class SourceAnnotator():
    """SourceAnnotator class as described in the PPALMS design document."""

    def __init__(self) -> None:
        self._file_lines = []
        self._line_tuples = []
        self._selected_lines = []
        self._file_type = None
    
    def upload_file(self, path) -> bool:
        """Check if input file specified by path exists. 
        If so, read file into this object and remove single line comments.

        args: 
            path: (str) Path to input file. File cannot be empty or contain only line comments.

        returns: 
            (bool) True for successful file read, False for failure.
        """

        # Ensure file exists before opening. If not, return false.
        if not os.path.exists(path):
            return False
        
        # Read file
        with open(path, 'r') as infile:
            self._file_lines = infile.readlines()
        
        self._file_type = path.rsplit('.', 1)[1]

        # Return True for successful file read. 
        # NOTE: File cannot be empty
        if len(self._file_lines) > 0:
            return True
        else:
            return False
    
    def strip_comments(self):
        comment_symbol = _LANG_COM_SYMS.get(self._file_type)
        self._file_lines = remove_line_comments(self._file_lines, comment_symbol)
        
    def select_lines(self, lines) -> list:
        """Updated which lines are selected. Ensure there are no duplicates in the set of selected lines.
        
        args:
            lines: (list of int) The list of line numbers selected
        
        returns:
            self._selected_lines: (list of int) The unique set of line numbers selected
        """
        self._selected_lines = set(lines)
        return self._selected_lines
    
    def create_tuple(self) -> tuple:
        """Form selected lines into tuple, append to list of tuples, and return the new tuple.
        
        returns:
            new_tuple: (tuple) The new tuple.
        """
        new_tuple = tuple(self._selected_lines)
        self._line_tuples.append(new_tuple)
        return new_tuple
    
    def get_tuples(self) -> list:
        """Return any tuples formed by create_tuple()"""
        return self._line_tuples
    
    def get_lines(self) -> list:
        """Prints contents of self._file_lines."""
        return self._file_lines
    
    def get_selected_lines(self) -> list:
        return self._selected_lines