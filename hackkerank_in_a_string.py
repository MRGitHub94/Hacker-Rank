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