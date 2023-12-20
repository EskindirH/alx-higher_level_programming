#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0

    for r in range(x):
        try:
            print("{}".format(my_list[r]), end='')
        except IndexError:
            break
        else:
            count += 1
    print()
    return (count)