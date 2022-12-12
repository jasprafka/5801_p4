import unittest
import io
import sys
from unittest.mock import MagicMock
from unittest.mock import patch
import SourceAnnotator
from SourceAnnotatorTestCases import *
from unittest import mock
import ppalms


_FUNCTIONS = {
    "1": ppalms.exit_ppalms,
    "2": ppalms.print_menu,
    "3": ppalms.show_file,
    "4": ppalms.strip_comments,
    "5": ppalms.select_lines,
    "6": ppalms.show_selected_lines,
    "7": ppalms.create_problem,
    "8": ppalms.show_probs,
    "9": ppalms.input_num_students,
    "0": ppalms.show_students
}

_MAIN_MENU = (
    "1. Exit\n"
    "2. Print this menu\n"
    "3. Show file\n"
    "4. Strip line comments\n"
    "5. Select lines\n"
    "6. Show selected lines\n"
    "7. Create Problem\n"
    "8. Show Problems\n"
    "9. Input Number of Students\n"
    "0. Print Number of Students\n"
)

_TEST_OUTPUT=(
    "Your line selection: 12 13 14\n"
    "        -- Selected Lines: [12, 13, 15]\n"
    "What would you like to do?\n"
    "Your choice: "
)


class PpalmsTest(unittest.TestCase):
    """TestCase subclass to run unittests on all functions in ppalms.py"""
    
    def setUp(self):  # Gets run before each test
        self.src_annotator = SourceAnnotator.SourceAnnotator()
        SourceAnnotator.print = MagicMock()

    def tearDown(self):  # Gets run after each test
        SourceAnnotator.print = print
        pass

    def test_exit_ppalms(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.src_annotator.upload_file(VALID_CPP_PATH)
        self.assertEqual(_FUNCTIONS.get("1")(self.src_annotator), True)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "Goodbye!\n")

    def test_print_menu(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.src_annotator.upload_file(VALID_CPP_PATH)
        self.assertEqual(_FUNCTIONS.get("2")(self.src_annotator), False)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), _MAIN_MENU+"\n")

    def test_show_file(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.src_annotator.upload_file(VALID_CPP_PATH)
        self.assertEqual(_FUNCTIONS.get("3")(self.src_annotator), False)
        sys.stdout = sys.__stdout__

        # I don't think this is necessary, this part should be tested in SourceAnntatorTest.
        self.assertEqual(capturedOutput.getvalue(
        ), '\n0 #include <iostream>\n1 \n2 // Using namespace std is bad practice\n3 using namespace std;\n4 \n5 int main() {\n6     // Variable declarations\n7     int x = 0;\n8     int y = 0;\n9     int z = 0;\n10 \n11     // Variables must be declared before they are used\n12     cout << "x = " << x << endl;\n13     cout << "y = " << x << endl;\n14     cout << "z = " << x << endl;\n15 \n16     return 0;\n17 }\n')

    def test_strip_comments(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.src_annotator.upload_file(VALID_CPP_PATH)
        self.assertEqual(_FUNCTIONS.get("4")(self.src_annotator), False)
        sys.stdout = sys.__stdout__

    
    string_of_ints = '12 13 14'
    @patch('builtins.input', return_value=string_of_ints)
    def test_select_lines(self,mock_input):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.src_annotator.upload_file(VALID_CPP_PATH)
        result = ppalms.select_lines(self.src_annotator)
        sys.stdout = sys.__stdout__
        self.assertEqual(result, False)
    

    def test_show_selected_lines(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.src_annotator.upload_file(VALID_CPP_PATH)
        self.assertEqual(_FUNCTIONS.get("6")(self.src_annotator), False)
        sys.stdout = sys.__stdout__

    
    def test_create_problem(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.src_annotator.upload_file(VALID_CPP_PATH)
        self.assertEqual(_FUNCTIONS.get("7")(self.src_annotator), False)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(),"\t-- No lines selected!"+"\n")

    string_of_ints = '1'
    @patch('builtins.input', return_value=string_of_ints)
    def test_create_problem_2(self,mock_input):
        self.src_annotator.upload_file(VALID_CPP_PATH)
        self.src_annotator.select_lines([12,13,14])
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.assertEqual(_FUNCTIONS.get("7")(self.src_annotator), False)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(),"\nProblem types:\n1: randomize\n2: Multiple Choice\n4: Fill in the Blank\n\t-- Created Problem Problem Type: 1\nLines:(12, 13, 14)\n")


    def test_show_probs(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.src_annotator.upload_file(VALID_CPP_PATH)
        self.assertEqual(_FUNCTIONS.get("8")(self.src_annotator), False)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(),"\t-- No Problems created!\n")

    def test_show_probs_2(self):
        self.src_annotator.upload_file(VALID_CPP_PATH)
        self.src_annotator.select_lines([12,13,14])
        self.src_annotator.create_problem(1)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.src_annotator.upload_file(VALID_CPP_PATH)
        self.assertEqual(_FUNCTIONS.get("8")(self.src_annotator), False)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(),"\t-- [Problem Type: 1\nLines:(12, 13, 14)]\n")

    string_of_ints = '-1'
    @patch('builtins.input', return_value=string_of_ints)
    def test_input_num_students(self,mock_input):
        self.src_annotator.upload_file(VALID_CPP_PATH)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.assertEqual(_FUNCTIONS.get("9")(self.src_annotator), False)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(),"\t-- Sorry, number of students must be a positive integer.\n")

    string_of_ints = '10'
    @patch('builtins.input', return_value=string_of_ints)
    def test_input_num_students_2(self,mock_input):
        self.src_annotator.upload_file(VALID_CPP_PATH)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.assertEqual(_FUNCTIONS.get("9")(self.src_annotator), False)
        sys.stdout = sys.__stdout__

    def test_show_students(self):
        self.src_annotator.upload_file(VALID_CPP_PATH)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.assertEqual(_FUNCTIONS.get("0")(self.src_annotator), False)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(),"\t-- Current number of students: 10\n")
        


if __name__ == "__main__":
    unittest.main()  # run all tests
