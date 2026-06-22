import os
import time

def get_metadata(file_path):

    stats = os.stat(file_path)

    return {
        "File Name": os.path.basename(file_path),
        "Size (Bytes)": stats.st_size,
        "Created": time.ctime(stats.st_ctime),
        "Modified": time.ctime(stats.st_mtime),
        "Accessed": time.ctime(stats.st_atime)
    }