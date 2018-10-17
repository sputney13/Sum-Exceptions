from sum_numbers import add_file_lines
import pytest


@pytest.mark.parametrize("filename, expected", [
    ("testfile1.txt", 12)
    ])

def test_sum_numbers(filename,expected):
    assert add_file_lines(filename) == expected
