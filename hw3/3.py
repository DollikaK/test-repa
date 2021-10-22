#!/bin/python3

import zipfile
import os

def is_py_script_inside(arr):
   
    return True in ['.py' in a for a in arr]

# Распаковываем архив
with zipfile.ZipFile('main.zip', 'r') as zf:
    zf.extractall('main')


subdirs = ['main']
dirs_with_py = set()

while len(subdirs) > 0:   
    cur_dir = subdirs[-1]   
    subdirs.pop()          

    subdirs_and_files = os.listdir(cur_dir)

    if is_py_script_inside(subdirs_and_files):
        dirs_with_py.add(cur_dir)

    for sub_d_f in subdirs_and_files:
        if '.' not in sub_d_f: 
            subdirs.append(cur_dir + '/' + sub_d_f)

with open('result.txt', 'w') as f:
    for d in sorted(dirs_with_py):
        f.write(d)
        f.write('\n')
