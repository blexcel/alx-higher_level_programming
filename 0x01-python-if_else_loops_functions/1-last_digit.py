#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l_d = number % 10
if(l_d > 5):
    print("Last digit of {0} is {1} and is greater than 5".format(number, l_d))
elif(l_d == 0):
    print("Last digit of {0} is {1} and is 0".format(number, l_d))
elif(l_d < 6 and l_d != 0):
        print("Last digit of {0} is {1} and is less than 6 and not 0".format(number, l_d))
