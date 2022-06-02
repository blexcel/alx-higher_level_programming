#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    a = len(sys.argv)
    if(a <= 0):
        print("{} arguments.".format(a))
    else:
        if(a == 2):
            print("{} argument:".format(a - 1))
        else:
            print("{} arguments:".format(a - 1))
        for i in range(1, a):
            print("{}: {}".format(i, sys.argv[i]))
