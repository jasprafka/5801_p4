# PPALMS V_0.1 - Group 12
## -- How to run PPALMS --
**To run ppalms.py -**  
From the **5801_p4** directory, issue:  
`python3 ppalms.py <input-file-path>`  

where `<input-file-path>` is the path to the source code you wish to annotate. Some example source files have been provided in the `test_files` directory.  

**e.g. -**  
`python3 ppalms.py test_files/test_code.cpp`  

The program runs on the command line, offering several options for source code annotation and print out as the following menu (including the removal of line comments and forming line tuples).
```
1. Exit
2. Print this menu
3. Show file
4. Strip line comments
5. Select lines
6. Show selected lines
7. Create Tuple
8. Get Tuples
```
The user can input numbers 1-8 to make a choice.

## -- How to run the testing Suite --  
This software package uses the python `unittest` library for testing. The testing files included are `SourceAnnotatorTest.py` and `PpalmsTest.py`.  

In the `unittest` library, the `unittest.TestCase` class is subclassed out, and the individual test cases for each module are created as methods on the subclass object. The inputs and expected outputs to each test case are defined in the `SourceAnnotatorTestCases.py` and `PpalmsTestCases.py` files, for their respective tests.

**To run a test -**  
From the **5801_p4** directory, issue:  
`python3 <test-file-name>.py`  

**e.g. -**  
`python3 SourceAnnotatorTest.py`  

_or_  

`python3 PpalmsTest.py`  

**Test Results -**  
The unittest library automatically runs each test in the subclass, although in no particular order. If all tests pass, the output will be similar to:  
```
$ py MyTest.py
........
----------------------------------------------------------------------
Ran 8 tests in 0.002s

OK
```

The status of each test is indicated by a character. Tests that pass are shown with the `.` character. Tests that fail get an `F`, and tests that throw an exception get `E`. In the above example, all 8 tests passed, so each was given a `.` as its output.  

Here is an example of a failed test:  
```
$ py SourceAnnotatorTest.py
....F...
======================================================================
FAIL: test_remove_line_comments (__main__.SourceAnnotatorTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\jaspr\Documents\UofM\Software Engineering\5801_p4\SourceAnnotatorTest.py", line 31, in test_remove_line_comments
    self.assertNotEqual(SourceAnnotator.remove_line_comments(CSTYLE_COMMENT_LINES, '//'), CSTYLE_COMMENT_LINES[0:2])
AssertionError: ['int x = 0;', 'x = 0; // comment'] == ['int x = 0;', 'x = 0; // comment']

----------------------------------------------------------------------
Ran 8 tests in 0.002s

FAILED (failures=1)
```
