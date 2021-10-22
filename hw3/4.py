#!/bin/python3

arr = []

with open('table.csv', 'r') as f:
    for line in f:
        str_nums = line.split(',')
        arr.append(list(map(int, str_nums)))

# Добавляем строчку из нулей
arr.insert(len(arr) // 2, [0] * len(arr[0]))

# Добавляем столбец из нулей
for line in arr:
    line.insert(len(line) // 2, 0)

# Сохраняем массив обратно
with open('new_table.csv', 'w') as f:
    for line in arr:
        str_line = list(map(str, line))
        f.write(', '.join(str_line))
        f.write('\n')
