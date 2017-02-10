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

# import sys


# n = int(raw_input().strip())
# height = map(int,raw_input().strip().split(' '))

# tallest = max(height)
# n = 0
# for c in height:
#     if c == tallest:
#         n += 1

# print n


# Enter your code here. Read input from STDIN. Print output to STDOUT
# import sys

# 8
# UDDDUDUU
# >>> 1

# n = int(raw_input().strip())
# mountain = list(raw_input().strip())

# A valley is a non-empty sequence of consecutive steps below sea level, 
# starting with a step down from sea level and ending with a step up to sea 
# level.

# def find_valleys(mountain):
#     sea_level = 0
#     height_count = []
#     valley_count = 0
#     zero_count = 0
#     if len(mountain) < 1:
#         return 0

#     # want to traverse the list and know if there is a D and a U
#     # find the greatest number of Ds or Us together 
#     for n in mountain:
#         if n == 'U':
#             sea_level = sea_level + 1
#             height_count.append(sea_level)
#         elif n == 'D':
#             sea_level = sea_level - 1
#             height_count.append(sea_level)
#     # if there are more than 2 0s and not next to each other, count += 1
#     for l in height_count:
#         if l == 0:
#             zero_count += 1

#     if zero_count <= 1:
#         return 0
#     else:
#         for m in height_count:
#             if (height_count[m] == 0) and (height_count[m+1] != 0):
#                 valley_count = len([i for i in height_count if i == 0])
#     return valley_count - 1

# def find_valleys(mountain):
#     up, down, valley, cur, prev = 0, 0, 0, 0, 0
#     for i in mountain:
#         if i == 'U':
#             up += 1
#             cur += 1
#         else:
#             down += 1
#             cur -= 1
#         if (cur == 0) and (up-down == 0) and (prev == -1):
#             valley += 1
#     return valley


# print find_valleys(['U', 'D', 'D', 'D', 'U', 'D', 'U', 'U'])
# [1, 0, -1, -2, -1, -2, -1, 0]


