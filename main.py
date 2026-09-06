#================/@/==================
#.         import the modules  
#================/@/==================

from pathlib import Path
from scanner import scan_folder
from classifier import classify_file
from planner import planner
from organizer import organize_file
#================/@/==================
# INPUT VALIDATION
#================/@/==================

def check_input(prompt, max_val = 10, min_val = 1):
    print(" ")
    
    while True:
        value = input(prompt)
        value = value.strip()
        
        try:
            num = int(value)
            
            if min_val <= num <= max_val:
                return num
            
            else:
                print("Invalid input! Please enter a value between", min_val, "and", max_val)
        
        except ValueError:
          print("Invalid input! Please enter a valid integer.")


#================/@/==================
# ORGANISE FILES
#================/@/==================

def show_summary(moved_files, failed_files, folder_created):
    print("===============SUMMARY===============")
    if not moved_files:
        print("No files moved ")
    else:
        for folder, count in moved_files.items():
            print(f"{folder}     : {count} files moved")
        total_files = sum(moved_files.values())
        print(f"Total files Moved   : {total_files}")
    print("")
    if not failed_files:
        print("Failed files : None")
    else:
        for item, error in failed_files:
            print("Failed operation")
            print(f"{item}     :    {error}")
    print(f"Folders Created   : {folder_created}")
    print("")
    
        
def dry_run(plans):
    print("==============PREVIEW==============")
    print("")
    for item, final_dest in plans:
        print(f"{item}     ---->    {final_dest}")
    print("")
    print("==============••••••••==============")
    


def validate_path(target_path):
   
    target_path = Path(target_path)

    if target_path.exists():
        if target_path.is_dir():
                
            return target_path
        else:
            print("Given Path is not a folder")
            return False
    else:
        print("Given path does not exists")
        return False
def get_target_folder():
    while True:
        input_path = input("Enter the folder path you want to organize: ")
        target_path = validate_path(input_path)
        if not target_path:
            user_choice = check_input("Organise different folder\n1. Yes\n2. No \nEnter Choices:  ", max_val = 2)
            if user_choice == 2:
                return False
        else:
            return target_path 


def logical_work(target_path):
    files = scan_folder(target_path)
    organised_files = []
    for item in files:
        category = classify_file(item)
        organised_files.append((item, category))
    plans = planner(organised_files, target_path)
    if plans:
        dry_run(plans)
        user_choice = check_input("Confirm to do above operations:\n1. Yes\n2. Return to main menu\nEnter Choices:  ", max_val = 2)
        if user_choice == 2:
            return True
        moved_files, failed_files, folder_created = organize_file(plans)
        show_summary(moved_files, failed_files, folder_created)
    else: 
        print("No files Found in the folder")
    next_choice = check_input("1. Return to main menu\n2. Exit\nEnter Your Choice:  ", max_val = 2)
    if next_choice == 1:
        return True
    else:
        return False

            
def main_menu():
    print("======================================")
    print("FILE Automation Tool")
    print("======================================")
    print("")
    user_input = check_input("1. Organize a folder\n2. Exit", max_val = 2)
    if user_input == 1:
        target_path = get_target_folder()
        if not target_path:
            return False
        return logical_work(target_path)
    
    else:
        return False

while True:
    if not main_menu():
        break


