#works only if file was not created by terminal

import os

def list_files(path, ignore):
    file_in_dir =[]
    for root, dirs,files in os.walk(path):
        for file in files:
            #remove unwanted files
            if ignore:
                if file in ignore:
                    continue
            file_in_dir.append(os.path.join(root, file))
    return file_in_dir

_last_files = list_files('./', None)

while 1:
    new_files = set(list_files('./', None)) ^ set(_last_files)
    if new_files:
        print("new file:{}".format(new_files))
    _last_files = list_files('./', None)