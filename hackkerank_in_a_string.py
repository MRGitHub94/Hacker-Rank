# HackerRank in a String!

# We say that a string, s, contains the word hackerrank if a subsequence of the
# characters in a word, s, spell hackerrank. For example, haackkerrannkk does 
# contain hackerrank, but haacckkerannk does not (the characters all appear 
# in the same order, but it's missing a second r). 

# Answer q queries, where each query i consists of a string, si. For each query,
# print YES on a new line if si contains hackerrank; otherwise print No.


# 2 
# hereiamstackerrank YES
# hackerworld NO

#!/bin/python

import sys


q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    # your code goes here
    h = "hackerrank"
    def match(s, h):
        # j keeps track of the length of the substring in the string
        i, j = 0, 0
        while i < len(s) and j < len(h):
            if s[i] == h[j]:
                j += 1
            i += 1
        # if j isnt the same length as hackerrank then we havent found the 
        # complete word
        if j == len(h):
            return "YES"
        else:
            return "NO"
    print match(s, h)


def count_substring(string, sub_string):
    # initialize a counter at 0
    counter = 0
    # determine the length of the sub_string you're hoping to find
    sub_len = len(sub_string)
    # go through the length of the string
    for i in range(0, len(string)):
        # if the letter matches the first letter in the substring
        if string[i] == sub_string[0]:
            # go from the current position until the end of the sub_string if 
            # it's in the exact order
            if string[i:(i + sub_len)] == sub_string:
                # increase counter
                counter = counter + 1
    # return counter's value
    return counter