#!/usr/bin/python3
for r in range(ord('a'), ord('z') + 1):
    if chr(r) not in ['q', 'e']:
        print("{}".format(chr(r)), end='')
