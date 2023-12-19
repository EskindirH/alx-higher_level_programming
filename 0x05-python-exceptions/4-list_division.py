#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []

    for r in range(list_length):
        try:
            result = my_list_1[r] / my_list_2[r]
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        finally:
            new_list.append(result)

    return (new_list)
