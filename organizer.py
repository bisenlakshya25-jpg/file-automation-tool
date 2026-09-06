import shutil


def organize_file(plans):
    moved_files = {}
    failed_files = []
    folder_created = 0

    for item, final_dest in plans:
        dest_folder = final_dest.parent

        if not dest_folder.exists():
            dest_folder.mkdir()
            folder_created += 1

        try:
            shutil.move(str(item), str(final_dest))

            folder_name = dest_folder.name
            moved_files[folder_name] = moved_files.get(folder_name, 0) + 1

        except OSError as error:
            failed_files.append((item, error))

    return moved_files, failed_files, folder_created
