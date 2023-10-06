#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for element in range(x):
            if type(my_list[element]) == int:
                print("{:d}".format(my_list[element]), end='')
                count += 1
    except ValueError:
        pass
    except IndexError:
         print("Traceback (most recent call last):")
    finally:
        print()
        return count
