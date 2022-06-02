#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    a = len(sys.argv)
    if(a <= 1):
        print("{:d} arguments.".format(a - 1))
    else:
        if(a == 2):
            print("{:d} argument:".format(a - 1))
        else:
            print("{:d} arguments:".format(a - 1))
        for i in range(1, a):
            print("{:d}: {}".format(i, sys.argv[i]))
