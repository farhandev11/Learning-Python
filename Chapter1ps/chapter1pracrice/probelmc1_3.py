import os
# Specify the directory you want to list
directory_path = '/coding'
# List all files and directories in the specified path 1
contents = os. listdir(directory_path)
# Print each file and directory name
for item in contents:
        print(item)
