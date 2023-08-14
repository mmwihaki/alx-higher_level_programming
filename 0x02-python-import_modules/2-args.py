#!/usr/bin/python3
import sys

argc = len(sys.argv) - 1
argv = sys.argv[1:]

if argc == 0:
    print("0 arguments.")
elif argc == 1:
    print("1 argument:")
    print("1: {}".format(argv[0]))
else:
    print("{} arguments:".format(argc))
    for i, arg in enumerate(argv):
        print("{}: {}".format(i + 1, arg))
