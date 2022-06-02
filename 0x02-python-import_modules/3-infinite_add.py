#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    a = len(argv)
    total = 0
    for i in range(1, a):
        total += int(argv[i])
    print("{:d}".format(total))
