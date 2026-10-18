def format_file_size(size_bytes):
    if size_bytes < 0:
        raise ValueError("Size cannot be negative")

    elif size_bytes == 0:
        return "0B"

    size_name = ["B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"]
    unit_index = 0
    while size_bytes >= 1024 and unit_index < len(size_name) - 1:
        size_bytes /= 1024
        unit_index += 1

    return f"{size_bytes:.2f} {size_name[unit_index]}"
