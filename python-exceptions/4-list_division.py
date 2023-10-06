#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for num in range(list_length):
        try:
            div_result = my_list_1[num] / my_list_2[num]
            result.append(div_result)
        except IndexError:
            print("out of range0")
            result.append(0)
        except TypeError:
            print("wrong type")
            result.append(0)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
    return result