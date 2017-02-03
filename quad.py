# Quad Combination

# Given an array of numbers arr and a number S, find 4 different numbers in arr 
# that sum up to S.
def find_array_quad_combinaton(arr, S):
   output = []
   for i in range(len(arr)):
      for j in range(i+1, len(arr)):
         for k in range(j+1, len(arr)):
            for m in range(k+1, len(arr)):
               if i + j + k + m == S:
                  output.append([i,j,k,m])
   return output
print find_array_quad_combinaton([1,2,3,4,5], 9)
print find_array_quad_combinaton([5,6,7,8,9,10,11], 45)
# >>> [0,1,2,3]?
# Write a function that gets arr and S and returns an array with 4 indices of 
# such numbers in arr, or null if no such combination exists.
# Explain and code the most efficient solution possible, and analyze its runtime 
# and space complexity.

# Hints & Tips
# The array is not sorted, and may hold any real number (positive, negative, 
# zero, integer or fraction)

# Any solution of more than O(n2) is not efficient enough. Please rate your peer
# feedback accordingly.

# If you peer can't even think of the naive solution, ask how can you check all 
# numbers in arr to come up with a solution.
# four nested for loops to get every combo?

# If your peer can't improve the naive solution, ask how can you use a pre-
# computation to save some work and improve efficiency. If that doesn't help, 
# ask how would a list of all pairs by their sum help to solve, and then ask 
# how can such a list be calculated and stored.

# Make sure that your peer's solution handles the case in which pairSum == 
# S-pairSum correctly.

# Solution
# The naive solution is to iterate on every possible combination of 4 numbers 
# from arr until the required combination if found. Using 4 nested loop 
# involves O(n4) time complexity and O(1) space complexity. This is quite 
# inefficient.

# We can do better, if we look at all the pairs in arr, and then try to build 
# the sum S from 2 different pairs.
# First, we iterate over all the possible pairs in arr with 2 nested loops and 
# hash each pair by its sum. Then, for each pairSum in the pairs hash table, 
# we look for its complement S - pairSum. When we find two pairs that sum up to 
# S, we need to check that these pairs are drawn from 4 different indices in arr 
# (in other words: that no number is used twice to reach the desired sum).

# function findArrayQuadCombination(arr, S):
#    if (arr == null OR S == null):
#       return null
#    n = length(arr)
#    if (n < 4):
#       return null
#    # hashing implementation language dependent:
#    pairHash = new HashTable()
#    for i from 0 to n-1
#       for j from i+1 to n-1
#          if !pairHash.isMapped(arr[i]+arr[j]):
#             pairHash.map(arr[i]+arr[j], [])
#          pairHash.get(arr[i]+arr[j]).push([i, j])

#    for pairSum in pairHash.getKeys()
#       if pairHash.isMapped(S - pairSum):
#          pairsA = pairHash.get(pairSum)
#          pairsB = pairHash.get(S - pairsSum)
#          combination = find4Uniques(pairsA, pairsB)
#          if (combination != null):
#             return combination
#    return null

# # Helper function.
# # Gets 2 arrays of sub-arrays of 2 numbers
# # Gets 4 unique numbers, from 2 sub-arrays of different arrays
# function find4Uniques(A, B):
#    lenA = length(A)
#    lenB = length(B)
#    for i from 0 to lenA-1:
#       for j from 0 to lenB-1:
#          if ( A[i][0] == B[j][0] OR A[i][1] == B[j][1] OR
#               A[i][0] == B[j][1] OR A[i][1] == B[j][0] ):
#             continue
#          else:
#             return [A[i][0], A[i][1], B[j][0], B[j][1]]
#    return null

# Time Complexity: Let n be the length or arr. Hashing all pairs in arr by their
# sum and iterating over all sums and their complements takes O(n2) time (n2 
# pairs and constant number of actions for each). Uniqueness check for all 
# indices of the pairs of sums that adds up to S until a valid combination is 
# found, is also O(n2) (checking at most n2 pairs with 4 comparisons for each). 
# Overall: quadratic O(n2) time complexity.

# Space Complexity: n2 pairs have up to n2 different sums. Hashing them takes 
# O(n2) space complexity.