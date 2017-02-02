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

# import sys


# s = raw_input().strip()
# t = raw_input().strip()
# k = int(raw_input().strip())

#two methods that can be performed
# .append()
# .pop()
# #initialize the count variables, these need to equal k or less
# count_remove = 0
# count_add = 0 
 
# w = zip(s,t) when the [i][i+1] aren't the same we want to know
# what index in w it is 

# i = 0
# for letter in s:
#         if letter[i] == t[i]:
#             i += 1
#         else:
#             return i
def append_and_delete(s, t, k):
    # set variables to the lengths of the two parameter strings
    length1 = len(s)
    length2 = len(t)

    # set length equal to the smaller of the lengths 
    length = length1 if length1 <= length2 else length2
    # set count to zero
    count = 0

    # go through the lenght 
    for i in range(length):
        # if the characters in the two strings are the same
        if s[i] == t[i]:
            # increase count
            count += 1
        else:
            break

    # deletions are the length of each string minus the count
    deletions = length1 - count
    additions = length2 - count

    # operations is the sum of both the deletions and the additions
    operations = deletions + additions

    # check if string1 is the same as string 2
    doubled = 0
    if s == t:
        doubled = (length1 * 2) + 1
        print "doubled", doubled

    # check these conditions for 'Yes'
    if (((length1 == length2) or (length1 > length2)) and operations <= k):
        print "length1", length1, "length2", length2
        print "s.count(s[0])", s.count(s[0])
        print "t.count(t[0])", t.count(t[0])
        return 'Yes'
    elif doubled == k or (s.count(s[0]) == length1 and t.count(t[0]) == length2):
        print "doubled", doubled
        print "length1", length1, "length2", length2
        print "s.count(s[0])", s.count(s[0])
        print "t.count(t[0])", t.count(t[0])
        return 'Yes'
    else:
        print "length1", length1, "length2", length2
        print "s.count(s[0])", s.count(s[0])
        print "t.count(t[0])", t.count(t[0])
        return 'No'

print append_and_delete("hackerhappy", "hackerrank", 9)
# hackerhappy
# hackerrank
# 9
print append_and_delete("cat", "fat", 6)
print append_and_delete("taco", "taci", 2)
print append_and_delete("cactus", "cactus", 12)








