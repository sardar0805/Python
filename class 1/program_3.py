import os

# Define the path to the directory
directory_path = '/'

# Check if the directory exists
if os.path.exists(directory_path):
    # Get a list of all files and folders in the directory
    directory_contents = os.listdir(directory_path)
    
    # Print each item in the directory
    print(f"Contents of '{directory_path}':")
    for item in directory_contents:
        print(item)
else:
    print(f"The directory '{directory_path}' does not exist.")
