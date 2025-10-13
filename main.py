

import sys

from formatter.disk_size import format_file_size

if len(sys.argv) >= 2:
    try:
        size_bytes = int(sys.argv[1])
        formatted_size = format_file_size(size_bytes)
        print(formatted_size)
    except ValueError:
        print("Please provide a valid file size in bytes as a command-line argument.")
else:
    print("Please provide the file size in bytes as a command-line argument.")
