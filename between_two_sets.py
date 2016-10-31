"""Consider two sets of positive integers, A ={...} and B={...}. 
We say that a positive integer, x, is between sets A and B if the following 
conditions are satisfied:

1. All elements in A are factors of x.
2. x is a factor of all elements in B.
Given A and B, find and print the number of integers (i.e., possible xs) 
that are between the two sets.

Input Format

The first line contains two space-separated integers describing the respective 
values of  A (the number of elements in set A) and B
(the number of elements in set B). 
The second line contains n distinct space-separated integers describing . 
The third line contains m distinct space-separated integers describing .

Constraints

1 <= n, m <= 10
1 <= a <= 100
1 <= b <= 100

Output Format

Print the number of integers that are considered to be between A and B.

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
from math import sqrt 

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
    #every number is divisible between one and itself
    fact = [1, a]
    #initialize check 
    check = 2
    #root of the input
    rootn = int(a**0.5)
    while check < rootn:
        if a % check == 0:
            fact.append(check)
            fact.append(a/check)
            check += 1
        if rootn == check:
            fact.append(check)
    fact.sort()
    return fact
#returns a list of factors
        
#function takes in the two sets as parameters
def return_integers_between_sets(a, b):
    # a = set(2, 4) b = set(16, 32, 96) the integers that are between them are 4, 8, 16 
    # (all factors of a and also b) -> return 3
    integers_between_sets = find_span(a, b) #call the find_span function
    lst_of_factors = [find_factor(b)]
    result = []
    #go through all the numbers between set A and set B
    for nums in integers_between_sets:
        #if the number is in the list of factors 
        if nums in lst_of_factors:
            #add it to results
            result.append(nums) 
    #return the length of the result list
    return len(result)

print return_integers_between_sets(a, b)

