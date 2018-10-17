import sum_numbers
import pytest


@pytest.mark.parametrize("filename, expected", [
    ("testfile1.txt", 12)
    ])

def test_sum_numbers(filename,expected):
    assert sum_numbers.main(filename) == expected
