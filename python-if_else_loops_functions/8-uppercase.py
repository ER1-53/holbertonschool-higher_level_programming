def uppercase(str):
    for i in range(len(str)):
        if ord('a') <= ord(str[i]) <= ord('z'):
            upp = ord(str[i]) - 32
        else:
            upp = ord(str[i])
        print("{}".format(chr(upp)), end='')
    print()
