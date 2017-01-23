# http://thenoisychannel.com/2011/08/08/retiring-a-great-interview-problem

# Given an input string and a dictionary of words, segment the input string into
# a space-separated sequence of dictionary words if possible. For example, if 
# the input string is "applepie" and the dictionary contains a standard set of 
# English words, then we would return the string "apple pie" as output.

# A FizzBuzz Solution
# Only considers segmentation into two words
def segment_string(str_input, str_dict):
    for i in range(len(str_input)):
        str_prefix = str_input[:i]

        if str_prefix in str_dict:
            str_suffix = str_input[i:]
            if str_suffix in str_dict:
                return str_prefix + " " + str_suffix
    return None

# A General Solution 
# The input string may be segmented into any number of dictionary words
# Recursive backtracking
def segment_string_recursive(str_input, str_dict):
    if str_input in str_dict:
        return str_input
    for i in range(len(str_input)):
        str_prefix = str_input[:i]
        if str_prefix in str_dict:
            str_suffix = str_input[i:]
            str_seg_suffix = segment_string_recursive(str_suffix, str_dict)
            if str_seg_suffix != None:
                return str_prefix + " " + str_seg_suffix
    return None
#O(2^n)

# An Efficient Solution - Dynamic Programming 

# def segment_string_dynamic(str_input, str_dict):
#     if str_input in str_dict:
#         return str_input
#     if str_dict[str_input]  

