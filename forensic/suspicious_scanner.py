import os

def scan_directory(folder_path):

    suspicious_extensions = [
        ".exe",
        ".bat",
        ".cmd",
        ".ps1",
        ".vbs"
    ]

    suspicious_files = []

    for root, dirs, files in os.walk(folder_path):

        for file in files:

            file_path = os.path.join(root, file)

            for ext in suspicious_extensions:

                if file.lower().endswith(ext):

                    suspicious_files.append(file_path)

    return suspicious_files