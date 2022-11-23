VALID_CPP_PATH = "./test_files/test_code.cpp"
VALID_PY_PATH = "./test_files/test_code.py"
EMPTY_PY_PATH = "./test_files/test_empty.py"
EMPTY_CPP_PATH = "./test_files/test_empty.cpp"
COMMENT_PY_PATH = "./test_files/test_only_comments.py"
COMMENT_CPP_PATH = "./test_files/test_only_comments.cpp"
INVALID_PATH = "./invalid_path.cat"
NO_PATH = ""

CSTYLE_COMMENT_LINES = [
    "int x = 0;",
    "x = 0; // comment",
    "// comment\n",
    " // comment",
    "\t// comment",
    "//// comment \n",
    " //// comment\t\n",
    "\t//// comment"
]

PYTHONIC_COMMENT_LINES = [
    "x = 0",
    "x = 0 # comment",
    "# comment",
    " # comment\n",
    "\t# comment \n",
    "## comment\n",
    " ## comment",
    "\t## comment\t\n"
]

COMMENTLESS_LINES = [
    "int x = 0;",
    "z = 0",
    "print('# some string')"
]

SELECTED_lINES = [1, 2, 2, 3, 4, 5, 6, 6]
(LINE_TUPLE_1) = (1, 2, 3, 4, 5, 6)