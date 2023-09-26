#!/usr/bin/python3
def fizzbuzz():
    f = "Fizz"
    b = "Buzz"
    fb = "FizzBuzz"
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("{}".format(fb), end=" ")
        elif num % 3 == 0:
            print("{}".format(f), end=" ")
        elif num % 5 == 0:
            print("{}".format(b), end=" ")
        else:
            print("{}".format(num), end=" ")
