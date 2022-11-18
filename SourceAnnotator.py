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

def _remove_line_comments(lines, comment_symbol) -> list:

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
    
    def upload_file(self, path) -> bool:
        """Check if input file specified by path exists. If so, read file into this object and remove single line comments.

        args: 
            self: (SourceAnnotator) Pointer to object
            path: (str) Path to input file. File cannot be empty or contain only comments.

        returns: 
            (bool) True for successful file read, False for failure.
        """

        # Ensure file exists before opening. If not, return false.
        if not os.path.exists(path):
            print(f"File {path} not found!")
            return False
        
        # Read file
        with open(path, 'r') as infile:
            self._file_lines = infile.readlines()
        
        file_ext = path.rsplit('.', 1)[1]
        comment_symbol = _LANG_COM_SYMS[file_ext]
        self._file_lines = _remove_line_comments(self._file_lines, comment_symbol)

        # Return True for successful file read. 
        # NOTE: File cannot be empty or contain only comments.
        if len(self._file_lines) > 0:
            return True
        else:
            return False
    
    def show_file(self) -> None:
        """Temporary testing function. Prints contents of self._file_lines. 
        This function should be removed later.
        """
        print("".join(self._file_lines))