import os
import sys

def find_longest_subdirectory(directory):
    longest_subdir = ""
    max_length = 0
    for root, dirs, files in os.walk(directory):
        for dir_name in dirs:
            full_path = os.path.join(root, dir_name)
            path_length = len(full_path)
            print(f"Checking directory: {full_path}, path length: {path_length}")
            if path_length > max_length:
                longest_subdir = full_path
                max_length = path_length
                print(f"New longest subdirectory: {longest_subdir}")
    return os.path.basename(longest_subdir)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python app.py <directory>")
        sys.exit(1)
    
    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        sys.exit(1)
    
    longest_subdir = find_longest_subdirectory(directory)
    print(longest_subdir)
