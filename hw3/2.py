#!/bin/python3

def write_array(array, file_name):
  """записывает строки из array в файл file_name"""
  text = '\n'.join(array)
  with open(file_name, 'w') as f:
    f.write(text)
