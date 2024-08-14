import os


Pipe = chr(9474)
Tee = chr(9500)
Elbow = chr(9492)
Space_Prefix = "  "
PIPE_PREFIX = "│   "




def print_directory(path, indentation_level=0):


    directory_counter = 0
    file_counter = 0


    prefix =""

    #tree.append(Pipe)
    entries = os.scandir(path)
    sorted_entries = sorted(entries, key=lambda f: f.name.lower())
    entries_count = len(sorted_entries)
    for index, entry in enumerate(sorted_entries):
        connector = Elbow if index == entries_count - 1 else Tee
        if entry.is_dir():
            print(PIPE_PREFIX*indentation_level+f"{prefix}{connector}{chr(9472)} {entry.name}{os.sep}")

            subdirectory_counter, subfile_counter = print_directory(entry.path, indentation_level+1)
            directory_counter += 1
            directory_counter+=subdirectory_counter
            file_counter+=subfile_counter
        else:
            print(PIPE_PREFIX*indentation_level+f"{prefix}{connector}{chr(9472)} {entry.name}")
            file_counter+=1
    return directory_counter, file_counter

directory_count, file_count = print_directory(".")
print(f"{directory_count} Verzeiche,  {file_count} Dateien")