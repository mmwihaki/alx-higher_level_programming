#!/usr/bin/python3
def uppercase(s):
    for char in s:
        if 'a' <= char <= 'z':
            offset = ord('a') - ord('A')
            print("{}".format(chr(ord(char) - offset)), end="")
        else:
            print("{}".format(char), end="")
    print()
