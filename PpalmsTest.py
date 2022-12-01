import unittest
import io
import sys
from unittest.mock import MagicMock
import SourceAnnotator
from SourceAnnotatorTestCases import *
import ppalms


_FUNCTIONS = {
        "1" : ppalms.exit_ppalms,
        "2" : ppalms.print_menu,
        "3" : ppalms.show_file,
        "4" : ppalms.strip_comments,
        "5" : ppalms.select_lines,
        "6" : ppalms.show_selected_lines,
        "7" : ppalms.create_tuple,
        "8" : ppalms.get_tuples,
        "9" : ppalms.main,
}

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
class PpalmsTest(unittest.TestCase):
    """TestCase subclass to run unittests on all functions in ppalms.py"""

    def setUp(self): # Gets run before each test
        self.src_annotator = SourceAnnotator.SourceAnnotator()
        SourceAnnotator.print = MagicMock()
    def tearDown(self): # Gets run after each test
        SourceAnnotator.print = print
        pass
        
    # We will not test the main() function in PpalmsTest since the only change is the path
    # of the upload file in the commend, and tihe test of upload file path will be test in
    # SourceAnnotatorTest
    
    # Every test in PpalmsTest will be running with the valid file path since the program 
    # will not be running with invalid file path  
    
    # Every test in PpalmsTest will be running with the valid cpp file, since SourceAnnotatorTest will
    # detect the different behavior between cpp and py file.
    	
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
    	self.assertEqual(capturedOutput.getvalue(), '\n0 #include <iostream>\n1 \n2 // Using namespace std is bad practice\n3 using namespace std;\n4 \n5 int main() {\n6     // Variable declarations\n7     int x = 0;\n8     int y = 0;\n9     int z = 0;\n10 \n11     // Variables must be declared before they are used\n12     cout << "x = " << x << endl;\n13     cout << "y = " << x << endl;\n14     cout << "z = " << x << endl;\n15 \n16     return 0;\n17 }\n')
    	
    def test_strip_comments(self):
    	capturedOutput = io.StringIO()
    	sys.stdout = capturedOutput
    	self.src_annotator.upload_file(VALID_CPP_PATH)
    	self.assertEqual(_FUNCTIONS.get("4")(self.src_annotator), False)
    	sys.stdout = sys.__stdout__
    
    # This test need the computer to input some words automatically, so it require some an extra package. 
    # But this package "pyautogui" is not installed on our lab machine. 
    # Hence, I comment out this test for now.
    
    def test_select_lines(self):
    
    	# Test for valid input value
    	print()
    	print("please input 1 for this test")
    	capturedOutput = io.StringIO()
    	sys.stdout = capturedOutput
    	self.src_annotator.upload_file(VALID_CPP_PATH)
    	self.assertEqual(_FUNCTIONS.get("5")(self.src_annotator), False)
    	sys.stdout = sys.__stdout__
    	self.assertEqual(capturedOutput.getvalue(), '\n0 #include <iostream>\n1 \n2 // Using namespace std is bad practice\n3 using namespace std;\n4 \n5 int main() {\n6     // Variable declarations\n7     int x = 0;\n8     int y = 0;\n9     int z = 0;\n10 \n11     // Variables must be declared before they are used\n12     cout << "x = " << x << endl;\n13     cout << "y = " << x << endl;\n14     cout << "z = " << x << endl;\n15 \n16     return 0;\n17 }\nEnter your selection as line numbers separated by spaces\ne.g. - \n1 2 5 7 10\n\nYour line selection: 	-- Selected Lines: [1]\n')
    	
    	# Test for invalid input value
    	print()
    	print("please input 100 for this test")
    	capturedOutput = io.StringIO()
    	sys.stdout = capturedOutput
    	self.src_annotator.upload_file(VALID_CPP_PATH)
    	self.assertEqual(_FUNCTIONS.get("5")(self.src_annotator), False)
    	sys.stdout = sys.__stdout__
    	self.assertEqual(capturedOutput.getvalue(), '\n0 #include <iostream>\n1 \n2 // Using namespace std is bad practice\n3 using namespace std;\n4 \n5 int main() {\n6     // Variable declarations\n7     int x = 0;\n8     int y = 0;\n9     int z = 0;\n10 \n11     // Variables must be declared before they are used\n12     cout << "x = " << x << endl;\n13     cout << "y = " << x << endl;\n14     cout << "z = " << x << endl;\n15 \n16     return 0;\n17 }\nEnter your selection as line numbers separated by spaces\ne.g. - \n1 2 5 7 10\n\nYour line selection: 	-- No lines selected!\n')
    	
    	
    def test_show_selected_lines(self):
    	capturedOutput = io.StringIO()
    	sys.stdout = capturedOutput
    	self.src_annotator.upload_file(VALID_CPP_PATH)
    	self.assertEqual(_FUNCTIONS.get("6")(self.src_annotator), False)
    	sys.stdout = sys.__stdout__
    	
    def test_create_tuple(self):
    	capturedOutput = io.StringIO()
    	sys.stdout = capturedOutput
    	self.src_annotator.upload_file(VALID_CPP_PATH)
    	self.assertEqual(_FUNCTIONS.get("7")(self.src_annotator), False)
    	sys.stdout = sys.__stdout__
    	
    def test_get_tuples(self):
    	capturedOutput = io.StringIO()
    	sys.stdout = capturedOutput
    	self.src_annotator.upload_file(VALID_CPP_PATH)
    	self.assertEqual(_FUNCTIONS.get("8")(self.src_annotator), False)
    	sys.stdout = sys.__stdout__
    
    	
    

if __name__ == "__main__":
    unittest.main() # run all tests
