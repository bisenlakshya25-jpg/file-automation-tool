📁 File Automation Tool

A modular Python-based file automation tool that scans a folder, classifies files based on their extensions, creates an organization plan, previews the planned changes, and safely organizes files.

✨ Features

* 📂 Scan files from a selected folder
* 🏷️ Automatically classify files by extension
* ⚙️ Configurable file categories using config.json
* 🧠 Separate planning phase before making changes
* 👀 Preview planned file movements before execution
* 🔄 Automatic duplicate filename handling
* 📁 Automatically create category folders
* ✅ Track successfully moved files
* ❌ Track failed file operations
* 📊 Display an operation summary after organization
* 🧩 Modular project structure

🏗️ Project Structure

file-automation-tool/
│
├── main.py
├── scanner.py
├── classifier.py
├── planner.py
├── organizer.py
├── config.json
└── README.md

🔄 How It Works

User selects folder
        ↓
    scanner.py
        ↓
      Files
        ↓
   classifier.py
        ↓
 (File, Category)
        ↓
    planner.py
        ↓
   Organization Plan
        ↓
      Preview
        ↓
   User Confirmation
        ↓
   organizer.py
        ↓
   Files Organized
        ↓
     Summary

⚙️ Configuration

File categories and extensions are stored in config.json.

Example:

{
    "Images": [".jpg", ".jpeg", ".png"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Audio": [".mp3", ".wav"],
    "Videos": [".mp4", ".mkv"],
    "Code": [".py", ".js", ".html"],
    "Archives": [".zip", ".rar"]
}

New categories and extensions can be added without changing the classifier logic.

🧩 Modules

main.py

Handles user interaction, input validation, folder selection, preview, confirmation, and final summary.

scanner.py

Scans the selected folder and returns the files that need to be processed.

classifier.py

Determines the category of each file using the extensions defined in config.json.

planner.py

Creates the complete organization plan and handles duplicate filenames before any files are moved.

organizer.py

Executes the approved plan, creates required folders, moves files, and tracks successful and failed operations.

🚀 Future Improvements

Planned improvements may include:

* 🧹 File cleanup utilities
* 🔍 Duplicate file detection
* 📝 File renaming rules
* 📦 Archive old files
* 📊 Detailed reports
* ⏰ Scheduled automation
* 🎯 More advanced configuration options

🛠️ Built With

* Python
* pathlib
* json
* shutil

📌 Project Status

Version 2 — Core automation system implemented

Testing and further features will be added in future updates.