#!/usr/bin/python3
def uppercase(s):
    for char in s:
        if 'a' <= char <= 'z':
            offset = ord('a') - ord('A')
            char = chr(ord(char) - offset)
        print("{}".format(char), end="")
    print()

