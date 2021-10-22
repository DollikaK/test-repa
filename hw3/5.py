#!/bin/python3

try:
    print('Do you want throw exception ? (0-no, 1-yes)')
    ret = int(input())
    if ret == 0:
        pass
    elif ret == 1:
        raise ZeroDivisionError 
except Exception as e:
    print('I am exception', type(e))
else:
    print('No any exceptions')
finally:
    print('I am finaly')
