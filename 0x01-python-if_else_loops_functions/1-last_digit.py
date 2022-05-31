#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l_digit = number % 10
if(l_digit > 5):
    print("Last digit of {0} is {1} and is greater than 5".format(number,l_digit))
elif(l_digit == 0):
    print("Last digit of {0} is {1} and is 0".format(number,l_digit))
else:
    if((l_digit < 6) and (l_digit != 0)):
        print("Last digit of {0} is {1} and is less than 6 and not 0".format(number,l_digit))
        
