#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_int = set()
    for num in my_list:
        unique_int.add(num)
    total = sum(unique_int)
    return total
