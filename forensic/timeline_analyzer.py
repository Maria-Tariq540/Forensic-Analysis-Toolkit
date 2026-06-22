import os
import time

def generate_timeline(file_path):

    stats = os.stat(file_path)

    events = [
        ("Created", time.ctime(stats.st_ctime)),
        ("Modified", time.ctime(stats.st_mtime)),
        ("Accessed", time.ctime(stats.st_atime))
    ]

    return events