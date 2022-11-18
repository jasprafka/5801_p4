from SourceAnnotator import SourceAnnotator

_VALID_TEST_PATH = "./test.cpp"

def main():
    annotator = SourceAnnotator()
    annotator.upload_file(_VALID_TEST_PATH)
    annotator.show_file()

if __name__ == "__main__":
    main()