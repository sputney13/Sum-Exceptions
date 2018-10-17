from sum_numbers import add_file_lines
import pytest


@pytest.mark.parametrize("filename, expected", [
    ("testfile1.txt", 12),
    ("testfile2.txt", 0),
    ("testfile3.txt", 21),
    ])

def test_sum_numbers(filename,expected):
    assert add_file_lines(filename) == expected

def test_error():
    with pytest.raises(FileNotFoundError):
        add_file_lines("testfile4.txt")
