#!/usr/bin/python3
def uniq_add(my_list=[]):
    lst = set(my_list)
    num = 0

    for i in lst:
        num += i
    return num
