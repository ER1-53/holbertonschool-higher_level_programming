#!/usr/bin/python3
for dozen in range(10):
    for unit in range(10):
        if dozen >= unit:
            continue
        else:
            if dozen != 8:
                print("{}{}".format(dozen, unit), end=', ')
            else:
                print("{}{}".format(dozen, unit))
