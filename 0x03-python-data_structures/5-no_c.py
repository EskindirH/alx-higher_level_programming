#!/usr/bin/python3
def no_c(my_string):
    for s in my_string:
        print("{}".format(s if s != 'c' and s != 'C' else ''), end='')
    print()
