# Absolute difference in an array
#!/bin/python

import sys


n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
# your code goes here
value = max(a)
a = sorted(a)
i = 0
while i < n:
    if abs(a[i-1]-a[i]) < value:
        value = abs(a[i-1]-a[i])
    i+= 1
print value