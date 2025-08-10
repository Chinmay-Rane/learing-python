#use of premade AI code

import os
# This program gives you the directory and location of the files in the directories
# Specify the path you want to list (you can use "." for current directory)
directory_path = "/"

try:
    # Get the list of all files and directories
    contents = os.listdir(directory_path)

    print(f"Contents of directory '{directory_path}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print(f"The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"Permission denied to access '{directory_path}'.")
