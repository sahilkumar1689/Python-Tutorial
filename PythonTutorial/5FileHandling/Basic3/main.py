import shutil

# 1. Shutil Module= The shutil module in Python provides a way to perform high-level file operations.It build on top of os module and allow us to copy,move,rename,and delete files and directories.

# Now there are many functions in shutil module but we will see some of the most commonly used functions.Some of them are:

# 1. shutil.copy(src, dst): This function is used to copy the contents of the file from the source path (src) to the destination path (dst) with the permission bits.
shutil.copy('source.txt', 'destination.txt')

# 2. shutil.copyfile(src, dst): This function is similar to shutil.copy() but it only copy the file contents without the permission bits.
shutil.copyfile('source.txt', 'destination.txt')

# 3. shutil.copy2(src, dst): This function is similar to shutil.copy() but it also copies the metadata of the file such as creation and modification times.
shutil.copy2('source.txt', 'destination.txt')

# 4. shutil.copytree(src, dst): This function is used to copy an entire directory tree from the source path (src) to the destination path (dst).
shutil.copytree('source_directory', 'destination_directory')

# 5. shutil.move(src, dst): This function is used to move a file or directory from the source path (src) to the destination path (dst).
shutil.move('source.txt', 'destination.txt')
# 6. shutil.rmtree(path): This function is used to delete an entire directory tree at the specified path.
shutil.rmtree('directory_to_delete')


# 2. Creating the temp directory = The tempfile module in Python provides a way to create temporary files and directories. These temporary files and directories are created in a secure manner and are automatically deleted when they are no longer needed.It is basically used in those cases when we want the sandbox environement for different processing tasks running in the background in order to provide them the isolated space to work on without affecting the main file system.

import tempfile

# 1. Creating a temporary file in simple way:
temp_file = tempfile.TemporaryFile()
print('Temporary file created:', temp_file.name)
print('Temporary file created:', temp_file.path)

# 2. Creating a temporary directory:

# It create the temporary directory at the system default location for temporary files and directories.
temp_dir = tempfile.gettempdir()
print('Temporary directory created:', temp_dir) # It return the path of the temporary directory.

# If you wan to create a temporary directory at a specific location, you can use the dir parameter:
custom_temp_dir = tempfile.mkdtemp(dir='.')
print('Custom temporary directory created:', custom_temp_dir)
# It create the temporary directory at the current working directory.
# Note: Remember to clean up the temporary files and directories when they are no longer needed to avoid cluttering the file system.
shutil.rmtree(custom_temp_dir)
# It delete the custom temporary directory created above.
# The temporary file created above will be automatically deleted when it is closed or when the program ends.
temp_file.close()

# 3. More cleaner way to create temporary files and directories using context managers:

# For temp directory:
import tempfile
from pathlib import Path

with tempfile.TemporaryDirectory() as tmp:
    tmp_path = Path(tmp)
    print(tmp_path)
    # do work
# directory auto-deleted here

# One more way to create temp directory:
tmp = tempfile.mkdtemp()
tmp_path = Path(tmp)
print(tmp_path)
# do work


# For temp files:
import tempfile

with tempfile.NamedTemporaryFile(delete=True) as f:
    f.write(b"hello")
    f.seek(0)
    print(f.read())

