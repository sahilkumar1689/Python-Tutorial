import os;

# os module = Python built-in os module gives you the ability to interact with the operating system related task.Like making the files and folders, removing files and folders, creating the paths of the files and folders,etc. 


# Example 1: Get the current working directory
current_directory = os.getcwd()
print("Current Working Directory:", current_directory)


# Example 2: List all files and directories in the current directory
files_and_dirs = os.listdir(current_directory)
print("Files and Directories in '", current_directory, "':", files_and_dirs)


# Example 3: Create a new directory
new_directory = "example_dir"
if not os.path.exists(new_directory):
    os.mkdir(new_directory)
    print("Directory", new_directory, "created")
    
    
# Example 4: Rename the newly created directory
renamed_directory = "renamed_example_dir"
os.rename(new_directory, renamed_directory)
print("Directory renamed to", renamed_directory)


# Example 5: Remove the renamed directory
os.rmdir(renamed_directory)
print("Directory", renamed_directory, "removed")


# Example 6: Get the absolute path of a file
file_path = "sample.txt"
os.path.abspath(file_path)
print("Absolute path of", file_path, "is", os.path.abspath(file_path))


# Example 7: Check if a path exists
path_exists = os.path.exists(file_path)
print("Does the path", file_path, "exist?", path_exists)


# Example 8: Split the file path into directory and file name
directory, file_name = os.path.split(file_path)
print("Directory:", directory)
print("File Name:", file_name)


# Example 9: Get the file extension
file_extension = os.path.splitext(file_path)[1]
print("File Extension of", file_path, "is", file_extension)


# Example 10: Join two paths
joined_path = os.path.join(current_directory, file_path)
print("Joined Path:", joined_path)
print("Directory", new_directory, "created")


# Example 11: Change the current working directory
os.chdir(current_directory)
print("Changed working directory to:", os.getcwd())
print("Directory", new_directory, "created")

# Note = After doing the os.chdir(), the current working directory will be changed to the specified path.So its very important to chagne the sys.path if you are working with multiple directories in order to run the import statements correctly.
# e.g.:
# import sys
# print("sys.path:", sys.path)

# # Add a path for a one-off import (prefer importlib in advanced use)
# sys.path.insert(0, changed_directory_path) # It will add the changed directory path to the start of sys.path list.If one path is not running the import statement correctly then it will check the next path in the sys.path list.
# print("sys.path after inserting changed directory:", sys.path)  



# Example 12: Get the size of a file
if os.path.exists(file_path):
    file_size = os.path.getsize(file_path)
    print("Size of", file_path, "is", file_size, "bytes")
else:
    print("File", file_path, "does not exist to get size")
    print("Directory", new_directory, "created")
    
    
# Example 13: List only files in the current directory
only_files = [f for f in os.listdir(current_directory) if os.path.isfile(os.path.join(current_directory, f))]
print("Files in '", current_directory, "':", only_files)
print("Directory", new_directory, "created")


# Example 14: List only directories in the current directory
only_dirs = [d for d in os.listdir(current_directory) if os.path.isdir(os.path.join(current_directory, d))]
print("Directories in '", current_directory, "':", only_dirs)
print("Directory", new_directory, "created")


# Example 15: Check if a path is a file or directory
is_file = os.path.isfile(file_path)
is_dir = os.path.isdir(renamed_directory)
print(file_path, "is a file:", is_file)
print(renamed_directory, "is a directory:", is_dir)
print("Directory", new_directory, "created")



# 2. Pathlib Module = The pathlib module offers classes representing filesystem paths with semantics appropriate for different operating systems.Pathlib module provides an object-oriented interface to work with file system paths.In simple words, it allows you to handle and manipulate file system paths in a more intuitive and readable way compared to traditional methods like using the os module.

# e.g.:
from pathlib import Path

# Example 1: Create a Path object
path = Path(current_directory)
print("Path Object:", path)
# Example 2: List all files and directories in the current directory using Pathlib
files_and_dirs_pathlib = [p.name for p in path.iterdir()]
print("Files and Directories in '", current_directory, "' using Pathlib:", files_and_dirs_pathlib)
# Example 3: Create a new directory using Pathlib
new_dir_pathlib = path / "pathlib_example_dir"
if not new_dir_pathlib.exists():
    new_dir_pathlib.mkdir()
    print("Directory", new_dir_pathlib, "created using Pathlib")
    
# Example 4: Rename the newly created directory using Pathlib
renamed_dir_pathlib = path / "pathlib_renamed_example_dir"
new_dir_pathlib.rename(renamed_dir_pathlib)
print("Directory renamed to", renamed_dir_pathlib, "using Pathlib")

# Example 5: Remove the renamed directory using Pathlib
renamed_dir_pathlib.rmdir()
print("Directory", renamed_dir_pathlib, "removed using Pathlib")

# Example 6: Get the absolute path of a file using Pathlib
file_path_pathlib = path / "sample.txt"
print("Absolute path of", file_path_pathlib.name, "is", file_path_pathlib.resolve())

# Example 7: Check if a path exists using Pathlib
path_exists_pathlib = file_path_pathlib.exists()
print("Does the path", file_path_pathlib, "exist?", path_exists_pathlib)

# Example 8: Get the file extension using Pathlib
file_extension_pathlib = file_path_pathlib.suffix
print("File Extension of", file_path_pathlib.name, "is", file_extension_pathlib)

# Example 9: Join two paths using Pathlib
joined_path_pathlib = path / file_path_pathlib.name
print("Joined Path using Pathlib:", joined_path_pathlib)

# Example 10: Get the size of a file using Pathlib
if file_path_pathlib.exists():
    file_size_pathlib = file_path_pathlib.stat().st_size
    print("Size of", file_path_pathlib.name, "is", file_size_pathlib, "bytes using Pathlib")    
else:
    print("File", file_path_pathlib.name, "does not exist to get size using Pathlib")
    
# Example 11: List only files in the current directory using Pathlib
only_files_pathlib = [p.name for p in path.iterdir() if p.is_file()]
print("Files in '", current_directory, "' using Pathlib:", only_files_pathlib)
# Example 12: List only directories in the current directory using Pathlib
only_dirs_pathlib = [p.name for p in path.iterdir() if p.is_dir()]
print("Directories in '", current_directory, "' using Pathlib:", only_dirs_pathlib)
# Example 13: Check if a path is a file or directory using Pathlib
is_file_pathlib = file_path_pathlib.is_file()
is_dir_pathlib = renamed_dir_pathlib.is_dir()
print(file_path_pathlib.name, "is a file using Pathlib:", is_file_pathlib)
print(renamed_dir_pathlib.name, "is a directory using Pathlib:", is_dir_pathlib)
print("Directory", new_directory, "created using Pathlib")




    

