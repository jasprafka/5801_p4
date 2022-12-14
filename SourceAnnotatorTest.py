import unittest
import io
import sys
from unittest.mock import MagicMock
import SourceAnnotator
from SourceAnnotatorTestCases import *


class SourceAnnotatorTest(unittest.TestCase):
    """TestCase subclass to run unittests on all functions in SourceAnnotator."""

    def setUp(self): # Gets run before each test
        self.src_annotator = SourceAnnotator.SourceAnnotator()
        SourceAnnotator.print = MagicMock()
        self.rmlc = SourceAnnotator.remove_line_comments

    def tearDown(self): # Gets run after each test
        SourceAnnotator.print = print
        self.rmlc = None
        pass
    
    def test_upload_file(self):
        self.assertTrue(self.src_annotator.upload_file(VALID_CPP_PATH))
        self.assertTrue(self.src_annotator.upload_file(VALID_PY_PATH))
        self.assertTrue(self.src_annotator.upload_file(EMPTY_PY_PATH))
        self.assertTrue(self.src_annotator.upload_file(EMPTY_CPP_PATH))
        self.assertTrue(self.src_annotator.upload_file(COMMENT_PY_PATH))
        self.assertTrue(self.src_annotator.upload_file(COMMENT_CPP_PATH))
        self.assertFalse(self.src_annotator.upload_file(INVALID_PATH))
        self.assertFalse(self.src_annotator.upload_file(NO_PATH))
    
    def test_remove_line_comments(self):
        self.assertEqual(SourceAnnotator.remove_line_comments(CSTYLE_COMMENT_LINES, '//'), CSTYLE_COMMENT_LINES[0:2])
        self.assertEqual(SourceAnnotator.remove_line_comments(CSTYLE_COMMENT_LINES, None), CSTYLE_COMMENT_LINES)
        self.assertEqual(SourceAnnotator.remove_line_comments(PYTHONIC_COMMENT_LINES, '#'), PYTHONIC_COMMENT_LINES[0:2])
        self.assertEqual(SourceAnnotator.remove_line_comments(PYTHONIC_COMMENT_LINES, None), PYTHONIC_COMMENT_LINES)
        self.assertEqual(SourceAnnotator.remove_line_comments(COMMENTLESS_LINES, '#'), COMMENTLESS_LINES)
        self.assertEqual(SourceAnnotator.remove_line_comments(COMMENTLESS_LINES, '//'), COMMENTLESS_LINES)
    
    def test_strip_comments(self):

        SourceAnnotator.remove_line_comments = MagicMock()

        self.src_annotator._file_lines = CSTYLE_COMMENT_LINES
        self.src_annotator.strip_comments()
        SourceAnnotator.remove_line_comments.assert_any_call(CSTYLE_COMMENT_LINES, None)
        
        self.src_annotator._file_lines = CSTYLE_COMMENT_LINES
        self.src_annotator._file_type = "c"
        self.src_annotator.strip_comments()
        SourceAnnotator.remove_line_comments.assert_any_call(CSTYLE_COMMENT_LINES, '//')

        SourceAnnotator.remove_line_comments = self.rmlc

    def test_select_lines(self):
        SourceAnnotator.len = MagicMock(return_value=10)
        lines = self.src_annotator.select_lines(SELECTED_lINES)
        self.assertListEqual(lines, list(set(SELECTED_lINES)))
        self.assertNotEqual(lines, SELECTED_lINES)
        SourceAnnotator.len = len
    
    #def test_create_tuple(self):
        #SourceAnnotator.tuple = MagicMock(return_value=(LINE_TUPLE_1))
        #self.assertTupleEqual(self.src_annotator.create_problem(1), (LINE_TUPLE_1))
        #self.assertTupleEqual(self.src_annotator._problems[0], (LINE_TUPLE_1))
        #SourceAnnotator.tuple = tuple
        
    
    #def test_get_tuples(self):
        #self.assertFalse(self.src_annotator._problems)
        #self.src_annotator._problems = [LINE_TUPLE_1]
        #self.assertListEqual(self.src_annotator.get_probs(), [LINE_TUPLE_1])

    
    def test_get_lines(self):
        self.assertFalse(self.src_annotator._file_lines)
        self.src_annotator._file_lines = COMMENTLESS_LINES
        self.assertListEqual(self.src_annotator.get_lines(), COMMENTLESS_LINES)
    
    def test_get_selected_lines(self):
        self.assertFalse(self.src_annotator._selected_lines)
        self.src_annotator._selected_lines = SELECTED_lINES
        self.assertListEqual(self.src_annotator.get_selected_lines(), SELECTED_lINES)
    
    def test_create_pro(self):
        SourceAnnotator.tuple = MagicMock(return_value=(LINE_TUPLE_1))
        tmp = self.src_annotator.create_problem(1)
        self.src_annotator.create_problem(2)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(tmp)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "Problem Type: 1\nLines:(1, 2, 3, 4, 5, 6)\n")
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(self.src_annotator._problems[1])
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "Problem Type: 2\nLines:(1, 2, 3, 4, 5, 6)\n")

    def test_get_probs(self):
        SourceAnnotator.tuple = MagicMock(return_value=(LINE_TUPLE_1))
        tmp = self.src_annotator.get_probs()
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(tmp)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "[]\n")
        self.src_annotator.create_problem(1)
        self.src_annotator.create_problem(2)
        tmp = self.src_annotator.get_probs()
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(tmp)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "[Problem Type: 1\nLines:(1, 2, 3, 4, 5, 6), Problem Type: 2\nLines:(1, 2, 3, 4, 5, 6)]\n")


if __name__ == "__main__":
    unittest.main() # run all tests