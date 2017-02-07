"""Q1. Given a list, count the number of unique repeated items.

    input: [1,1,2,2,2,3]
    output: 2
    explanation: 1 is repeated once and 2 is repeated twice, for a total
    of 2 repeated numbers.
"""
from collections import Counter
def count_number_repeats(lst):
  # lst = Counter(lst)
  dicti = {}
  for n in lst:
    dicti[n] = dicti.get(n, 0) + 1
  for keys, values in dicti.items():
    if values < 2:
      del dicti[keys]
  return len(dicti)

print count_number_repeats([1,1,2,2,2,3])

"""Q2. Given a list of numbers, for each num of coins, return the number of
       completed rows.

       Rules: 1. Each row i must have i coins.

                   Example:
                   Row 1 must have 1 coin.
                   Row 2 must have 2 coins.
                   Row 3 must have 3 coins.

             2. Each row is not considered complete if it has less than the
                number required. i.e. Row 3 is not considered complete if it
                has 2 coins or 1 coin.

             3. Each row cannot have more than i coins. i.e. Row 2 cannot have
                more than 2 coins.

       input:  [2, 5, 8]
       output: [1, 2, 3]
       explanation: 2 - Given two coins, the max number of rows completed is 1:
                        1 on row 1, and 1 on row 2. Row 2 is not complete, so 1
                        should be returned.

                        x
                        x

                    5 - Given five coins, the max number of rows completed is 2:
                        1 on row 1, 2 on row 2 and 2 on row 3. Row 3 is not
                        complete because it only has 2 coins, so 2
                        should be returned.

                        x
                        xx
                        xx

                    8 -  3 should be returned.

                        x
                        xx
                        xxx
                        x    # incomplete row
"""
# def find_completed_rows(nums):
#   # follow fib dynamic recursive answer
#   # look up number of coins and the value is how many levels can be completed
#   dicti = {1:1, 3:2, 6:3, 10:4, 15:5, 21:6, 28:7}
#   ouput = []
#   for n in nums:
#     # check if the number translates to exact number of levels completed
#     if dicti.get(n):
#       return dicti[n]
#     # check to see if the number is captured within the scope of the dictionary
#     elif n = dicti[n]:
#       return 



"""Q3. Given a string of chars, return unique, sorted combinations.

       input: 'ba'
       output: ['a', 'b', 'ba']

       input: 'abc'
       output: ['a', 'ab', 'ac', 'abc', 'b', 'bc', 'c']

"""
def return_combinations(chars):
  if len(chars) < 1:
    return []
  result = list(chars)
  return result

  # need to return permutations
  # if len(chars) == 1:
  #   return [chars]
  # result = []
  # for i,v in enumerate(chars):
  #   result += [v + p for p in return_combinations(chars[:i]+ chars[i+1:])]
  # return result

print return_combinations("ba")