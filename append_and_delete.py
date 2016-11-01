"""Append and Delete

You have a string, s, of lowercase letters. You can perform two types of
operations on s:

1. Append a lowercase letter to the end of the string
2. Delete the last character in the string. Performing this operation on an 
   empty string results in an empty string. 

Given an integer, k, and two strings, s and t, determine whether or not you can 
convert s to t by performing exactly k of the above operations on s. If it's 
possible, print Yes; otherwise, print No.

Input Format
The first line contains a string, s, denoting the initial string. 
The second line contains a string, t, denoting the desired final string. The 
third line contains an integer, k, denoting the desired number of operations.

Constraints
abs value of all variables between 1 - 100

Output Format
Print Yes if you can obtain string t by performing exactly k operations on s; 
otherwise, print No. 

Sample Input 0

hackerhappy
hackerrank
9

Sample Output 0

Yes

Explanation
We perform 5 delete operations to reduce string s to hacker. Next, we perform 4 
append operations to get hackerrank. Because we were able to convert s to t by 
performing exactly k = 9 operations, we print Yes. 

Sample Input 1

aba
aba 
7

Sample Output 1

Yes
We perform 4 deletions to reduce string s to an empty string. Next, we perform 3
append operations. Because we were able to convert s to t by performing exactly 
7 operations, we print Yes. """

#!/bin/python

import sys


s = raw_input().strip()
t = raw_input().strip()
k = int(raw_input().strip())

#two methods that can be performed
.append()
.pop()
#initialize the count variables, these need to equal k or less
count_remove = 0
count_add = 0 
 
# w = zip(s,t) when the [i][i+1] aren't the same we want to know
# what index in w it is 










