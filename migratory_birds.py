# migratory birds

# A flock of n birds is flying across the continent. Each bird has a type, and 
# the different types are designated by the ID numbers 1, 2, 3, 4, 5

# Given an array of n integers, find and print the type number of the most 
# common bird. If two or more types of birds are equally common, choose the
# type with the smallest ID number

# 6
# 1 4 4 4 5 3 

#!/bin/python

import sys
from collections import Counter
import operator


n = int(raw_input().strip())
types = map(int, raw_input().strip().split(' '))
# your code goes here
types_dict = Counter(types)
sorted_values = sorted(types_dict.items(), key=operator.itemgetter(1))

print sorted_values[-1][0] 

def find_max_value(types):
    types = Counter(types)
    sorted_values = sorted(types.items(), key=operator.itemgetter(1))
    max_value = sorted_values[-1][1] 
    keys_list = []
    for keys, values in types.items():
        if max_value == values:
             keys_list.append(keys)
    sorted_keys = sorted(keys_list)
    return sorted_keys[0]