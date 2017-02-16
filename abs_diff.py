# Find smallest absolute difference in an array
#!/bin/python

import sys


n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
# your code goes here
# set up value to be something that can be rebound 
# setting it to the maximum value in the array is good 
value = max(a)
# sort the array since the smallest difference is bound to be next to one another
a = sorted(a)
# set up a while loop iterator
i = 0
# while the iterator is less than the len(a)
while i < n:
    # check if the absolute value difference of two values in the area are less
    # than the current smallest value
    if abs(a[i-1]-a[i]) < value:
        # if it is, rebind value to equal this difference
        value = abs(a[i-1]-a[i])
    # increment
    i+= 1
# return the smallest value
print value