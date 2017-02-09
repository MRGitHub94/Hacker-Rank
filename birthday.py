# Birthday Cake Candles 

# Colleen is turning n years old. She has n candles of various heights on her 
# cake, and candle i has height height. Because the taller candles tower over 
# the shorter ones, Colleen can only blow out the tall ones. 

# Given the height, for each individual candle, find and print the number of
# candles she can successfully blow out. 

# Sample input 
# 4
# 3 2 1 3

# Sample Output
# 2

#!/bin/python

import sys


n = int(raw_input().strip())
height = map(int,raw_input().strip().split(' '))

tallest = max(height)
n = 0
for c in height:
    if c == tallest:
        n += 1

print n