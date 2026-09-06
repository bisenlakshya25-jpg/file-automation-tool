from pathlib import Path
def scan_folder(folder_path):
    files = []
    for item in folder_path.iterdir():
        if item.is_file():
            files.append(item)
    return files
