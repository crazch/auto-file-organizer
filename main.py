from pathlib import Path
import os
import shutil

file_path = '/home/ray/Projects/python/file-organizer/files'
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

# This function loop through current file_path and return file_path + filename
def list_of_file():
    file_list = [file for file in os.listdir(file_path) if os.path.isfile(os.path.join(file_path, file))]
    return file_list


# This function loop and list files according to extension and return list of file endswith each extenstion
def filtered_move(file_list):
    py_files = [file for file in file_list if file.endswith(".py")]
    js_files = [file for file in file_list if file.endswith(".js")]
    return py_files, js_files

def move_files_directory(current, destination):
    for filename in list_of_file():
        source_path = os.path.join(current, filename)
        destination_path = os.path.join(destination, filename)

        try:
            shutil.move(source_path, destination_path)
            print(f"Moved '{filename}' to '{destination}'")
        except Exception as e:
            print(f"Error moving '{filename}' {e}")

# This is the MAIN function  to run the script
def main():
    list_of_file()
    filtered_move(list_of_file())
    move_files_directory(file_path, destination_path)