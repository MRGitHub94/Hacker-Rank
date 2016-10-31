"""Consider two sets of positive integers, A ={...} and B={...}. We say that a positive integer, x, is between sets A and B if the following conditions are satisfied:

1. All elements in A are factors of x.
2. x is a factor of all elements in B.
Given A and B, find and print the number of integers (i.e., possible xs) that are between the two sets.

Input Format

The first line contains two space-separated integers describing the respective values of  (the number of elements in set ) and  (the number of elements in set ). 
The second line contains  distinct space-separated integers describing . 
The third line contains  distinct space-separated integers describing .

Constraints

Output Format

Print the number of integers that are considered to be between  and .

Sample Input

2 3
2 4
16 32 96

Sample Output

3

Explanation

The integers that are between A = {2, 4} and B = {16, 32, 96} are 4, 8, and 16.

Sample Input
1 3
1
3 5 11

Sample Output
2 

Explanation

The integers between set A and set B are the only xs that work """

#!/bin/python

import sys

n,m = raw_input().strip().split(' ') # 2 3
n,m = [int(n),int(m)] # [2,3]
a = map(int,raw_input().strip().split(' ')) # [2,4]
b = map(int,raw_input().strip().split(' ')) # [16, 32, 96]

#find the numbers that can be between the max of set a and the min of set b
def find_span(a, b):
    lower_bound = max(a)
    upper_bound = min(b)
    return range(lower_bound, upper_bound+1) #returns a list of all the numbers between a and b

#find x
def find_factor(a):
    if len(a) == 1:
        return a
    for integers in a:
        
        
#function takes in the two sets as parameters
def return_integers_between_sets(a, b):
    # a = set(2, 4) b = set(16, 32, 96) the integers that are between them are 4, 8, 16 (all factors of a and also b) -> return 3
    integers_between_sets = find_span(a, b) #call the find_span function