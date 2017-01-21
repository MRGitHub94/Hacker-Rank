# Given A, find and print the unique element

# Input Format
# The first line contains a single integer, n, denoting the number of integers
# in the array. The second line contains n space-separated integers describing
# the respective values in A.

# Output Format
# Print the unique number that occurs only once in A on a new line

# Sample Input
# 1
# 1

# Sample Output
# 1

# The array only contains 1 so we print 1 as our answer

# Sample Input 1
# 3
# 1 1 2

# Sample Output 1
# 2

# The array contains only one unique 2 so we print it

from collections import Counter

def lonely_integer(a):
    unique_value = Counter(a)
    for key, value in unique_value.items():
        if value == 1:
            return key


print lonely_integer([1, 1, 2])