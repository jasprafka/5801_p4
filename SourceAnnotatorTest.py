import unittest
from unittest.mock import MagicMock
import SourceAnnotator

_VALID_CPP_PATH = "./test_files/test_code.cpp"
_VALID_PY_PATH = "./test_files/test_code.py"
_EMPTY_PY_PATH = "./test_files/test_empty.py"
_EMPTY_CPP_PATH = "./test_files/test_empty.cpp"
_COMMENT_PY_PATH = "./test_files/test_only_comments.py"
_COMMENT_CPP_PATH = "./test_files/test_only_comments.cpp"
_INVALID_PATH = "./invalid_path.cat"

_CSTYLE_COMMENT_LINES = [
    "int x = 0;",
    "x = 0; // comment",
    "// comment\n",
    " // comment",
    "\t// comment",
    "//// comment \n",
    " //// comment\t\n",
    "\t//// comment"
]

_PYTHONIC_COMMENT_LINES = [
    "x = 0",
    "x = 0 # comment",
    "# comment",
    " # comment\n",
    "\t# comment \n",
    "## comment\n",
    " ## comment",
    "\t## comment\t\n"
]

_COMMENTLESS_LINES = [
    "int x = 0;",
    "z = 0",
    "print('# some string')"
]

_SELECTED_lINES = [1, 2, 2, 3, 4, 5, 6, 6]
_LINE_TUPLE = (1, 2, 3, 4, 5, 6)

class SourceAnnotatorTest(unittest.TestCase):
    """TestCase subclass to run unittests on all functions in SourceAnnotator."""

    def setUp(self): # Gets run before each test
        self.src_annotator = SourceAnnotator.SourceAnnotator()
        SourceAnnotator.print = MagicMock()

    def tearDown(self): # Gets run after each test
        pass
    
    def test_upload_file(self):
        self.assertTrue(self.src_annotator.upload_file(_VALID_CPP_PATH))
        self.assertTrue(self.src_annotator.upload_file(_VALID_PY_PATH))
        self.assertFalse(self.src_annotator.upload_file(_EMPTY_PY_PATH))
        self.assertFalse(self.src_annotator.upload_file(_EMPTY_CPP_PATH))
        self.assertFalse(self.src_annotator.upload_file(_COMMENT_PY_PATH))
        self.assertFalse(self.src_annotator.upload_file(_COMMENT_CPP_PATH))
        self.assertFalse(self.src_annotator.upload_file(_INVALID_PATH))
    
    def test_remove_line_comments(self):
        self.assertEqual(SourceAnnotator.remove_line_comments(_CSTYLE_COMMENT_LINES, '//'), _CSTYLE_COMMENT_LINES[0:2])
        self.assertEqual(SourceAnnotator.remove_line_comments(_PYTHONIC_COMMENT_LINES, '#'), _PYTHONIC_COMMENT_LINES[0:2])
        self.assertEqual(SourceAnnotator.remove_line_comments(_COMMENTLESS_LINES, '#'), _COMMENTLESS_LINES)
        self.assertEqual(SourceAnnotator.remove_line_comments(_COMMENTLESS_LINES, '//'), _COMMENTLESS_LINES)
    
    def test_select_lines(self):
        lines = self.src_annotator.select_lines(_SELECTED_lINES)
        self.assertEqual(lines, set(_SELECTED_lINES))
        self.assertNotEqual(lines, _SELECTED_lINES)
    
    def test_create_tuple(self):
        self.src_annotator.select_lines(_SELECTED_lINES)
        self.assertTupleEqual(self.src_annotator.create_tuple(), _LINE_TUPLE)
        self.assertListEqual(self.src_annotator._line_tuples,[_LINE_TUPLE])



if __name__ == "__main__":
    unittest.main() # run all tests