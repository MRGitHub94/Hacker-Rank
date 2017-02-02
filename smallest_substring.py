# The "Smallest Substring of All Characters" Problem

# Given an array with unique characters arr and a string str, find the smallest 
# substring of str containing all characters of arr.

# Example:
# arr: [x,y,z], str: xyyzyzyx
# result: zyx

# Implement your solution and analyze the runtime complexity
# def get_shortest_unique_substring(arr, words_str):
#     arr_string = ""
#     for letters in arr:
#         arr_string += letters
#     concise_list = sorted(arr_string)
#     print concise_list
#     # get the len(words_string) and create the window
#     window = words_str[:len(words_str)+1]
#     for i in range(len(words_str)-1):
#         if window == words_str[:i]:
#             return words_str[:i]


# Solution

# We iterate the string from left to right, while using two indices - 
# tailIndex and h. At each iteration step, we examine the temp substring  
# [str.charAt(tailIndex), str.charAt(tailIndex+1) ..., str.charAt(h)]  
# and keep a copy of the shortest vaild substring we've seen so far.

# To examine substrings we use 2 counters:
# uniqueCounter (integer) - number of unique characters of arr in our 
# temp substring countMap (map/object/associative array - depends of your 
# language of choice) - number of occurrences of each char from arr in our 
# substring

from collections import Counter
    
def get_shortest_unique_substring(s, t):
    print "s", s
    print "t", t
    # instantiate the big string you need and the missing
    need, missing = Counter(t), len(t)
    print "need", need
    print "missing", missing
    # all the iterators are set to 0
    i = I = J = 0
    # new iterators to go through the little string
    for j, c in enumerate(s, 1):
        # reduce the numbe of missing characters if the letter is in need
        missing -= need[c] > 0
        print "c", c
        print "missing", missing 
        print "need[c]", need[c]
        need[c] -= 1
        if not missing:
            while i < j and need[s[i]] < 0:
                print "i", i, "j", j
                print "need[s[j]]", need[s[i]]
                need[s[i]] += 1
                i += 1
            if not J or j - i <= J - I:
                I, J = i, j
    print "s[I:J]", s[I:J]
    return s[I:J]

# Solution without Counter
# def get_shortest_unique_substring(s, t):
#     m = len(s) # where it should be found
#     n = len(t) # what needs to be found

#     # make sure that the big string is actually longer than the target
#     if m < n:
#         return ''
#     # making a dictionary 
#     lt = {}
#     # iterate through what needs to be found
#     for i in t:
#         if i not in lt:
#             lt[i] = 1
#         else:
#             lt[i] += 1
#     # instantiate what is missing to be the length of what we're looking for    
#     missing = n
#     # instantiate iterators 
#     i = I = J = 0
#     # using enumerate to go through the bigger string starting at index 1
#     for j, c in enumerate(s, 1):    
#         # check if it's in the dict and that the count is greater than 0
#         if c in lt and lt[c] > 0:
#             # we can reduce the number of chars missing now
#             missing -= 1
#         if c in lt:
#             lt[c] -= 1

#         while i < j and not missing:
#             if not J or j-i < J-I:
#                 I, J = i, j
#             if s[i] not in lt:
#                 i += 1
#                 continue
#             else:
#                 lt[s[i]] += 1
#                 if lt[s[i]] > 0:
#                     missing += 1
#                 i += 1
#     return s[I:J]

# function get_shortest_unique_substring(arr, str):
#    t = 0
#    result = null
#    uniqueCounter = 0
#    countMap = {}
#    # initialize countMap:
#    for i from 0 to length(arr)-1:
#       countMap.setValueOf(arr[i], 0)
#    # scan str
#    for h from 0 to length(str)-1:
#       # handle the new head
#       head = str.charAt(h)
#       if countMap.keyExists(head) == false:
#          continue
#       headCount = countMap.getValueOf(head)
#       if headCount == 0:
#          uniqueCounter = uniqueCounter + 1
#       countMap.setValueOf(head, headCount + 1)   
#       # push tail forward
#       while uniqueCounter == length(arr):
#          tempLength = h - t + 1
#          if tempLength == arr.length:
#             return str.substring(t, h)
#          if (!result or tempLength < length(result)):
#             result = str.substring(t, h)
#          tail = str.charAt(t) 
#          if countMap.keyExists(tail):
#             tailCount = countMap.getValueOf(tail) - 1
#             if tailCount == 0:
#                uniqueCounter = uniqueCounter - 1
#             countMap.setValueFor(tail, tailCount)
#          t = t + 1
#    return result

# Runtime Complexity: we're doing a linear iteration of both str and 
# arr of lengths n and m respectively, so the runtime complexity is a 
# linear O(n+m).

# Space Complexity: depends of your implementation for the mapping, 
# but generally: we're using countMap with m keys (the length of arr) plus few 
# constant size counters - O(m) space complexity.

print get_shortest_unique_substring("xyz", "xyyzyzyx")
# "zyx"

print get_shortest_unique_substring("abc", "adobecodebanc")
# "banc"