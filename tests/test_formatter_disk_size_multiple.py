import pytest
from formatter.disk_size import format_file_size


@pytest.mark.parametrize(
    "size_bytes, expected_result",
    [
        (0, "0B"),
        (1, "1.00 B"),
        (1024, "1.00 KB"),
        (1024**2, "1.00 MB"),
        (1024**3, "1.00 GB"),
        (1024**4, "1.00 TB"),
        (1024**5, "1.00 PB"),
    ],
)
def test_format_file_size(size_bytes, expected_result):
    assert format_file_size(size_bytes) == expected_result


def test_format_file_size_rejects_negative_sizes():
    with pytest.raises(ValueError, match="Size cannot be negative"):
        format_file_size(-1)
