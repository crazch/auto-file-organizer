from pathlib import Path
import os
import shutil

# Extensions and their corresponding target folders:
file_target_dirs = {
    ".py": "/home/ray/Projects/python/file-organizer/experiment/python/",
    ".js": "/home/ray/Projects/python/file-organizer/experiment/javaScript/"
    # Add more extensions and target path
}
# TODO: RENAME THIS VAR
file_path = '/home/ray/Projects/python/file-organizer/experiment/files'

# TODO: REMOVE
destination_path = '/home/ray/Projects/python/file-organizer/target-folder'

# THis Function Loop and return directory with matching/filtered file extension
'''def loop_through_directory():
    for file in os.listdir(file_path):
        filename = os.fsdecode(file)
        files = [os.path.join(file_path, filename)]
        if filename.endswith(".py"):
            py_files_list = [x for x in files]
            files_array.append(py_files_list)
            continue
        else:
            continue
loop_through_directory()
'''

# This function loop through source_path file_path and return file_path + filename
def list_of_file():
    file_list = [file for file in os.listdir(file_path) if os.path.isfile(os.path.join(file_path, file))]
    return file_list


# This function loop and list files according to extension and return list of file endswith each extenstion
# NOT USED
'''
def filtered_move(file_list):
    py_files = [file for file in file_list if file.endswith(".py")]
    js_files = [file for file in file_list if file.endswith(".js")]
    return py_files, js_files
'''

# MOVE FILES
def move_files_directory(source_path):
    for filename in list_of_file():
        _, extension = os.path.splitext(filename)
        if extension.lower() in file_target_dirs:
            src_path = os.path.join(source_path, filename)
            destination_path = os.path.join(file_target_dirs[extension.lower()], filename)
            os.makedirs(os.path.dirname(destination_path), exist_ok=True)
            try:
                shutil.move(src_path, destination_path)
                print(f"Moved '{filename}' to '{destination_path}'")
            except Exception as e:
                print(f"Error moving '{filename}' {e}")
        else:
            print(f"{extension} not registered!")

# This is the MAIN function  to run the script
def main():
    move_files_directory(file_path)
