import json
from pathlib import Path
extensions = {}

def load_data():
    global extensions
    try:
        with open("config.json", "r") as db_file:
            extensions = json.load(db_file)
    except FileNotFoundError:
        extensions = {}

def classify_file(file_path):
    file_ext = file_path.suffix.lower()
    if file_ext == "":
        return "No extension"
    for category, extention in extensions.items():
        if file_ext in extention:
            return category
        
    
    return "Other"
