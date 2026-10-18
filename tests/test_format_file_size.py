
import pytest

from formatter.disk_size import format_file_size


    # test_example.py
def test_format_file_size():
    assert format_file_size(220) == "220.00 B"


