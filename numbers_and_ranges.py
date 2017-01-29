# Numbers and Ranges
# Given a sorted list and an input number as inputs, write a function to return
# a Range object, consisting of the indices of the first and last occurences of 
# the first and last occurrences of the input number in the list. 

# Examples 
# input list: [1, 2, 5, 5, 8, 8, 10]
# input number: 8
# output: [4, 5]

# input list: [1, 2, 5, 5, 8, 8, 10]
# input number: 2
# output: [1,1]


# def find_range(input_list,input_number):
#     output = []
#     for index, num in enumerate(input_list): 
#         if index == input_number:
#             output.append(num)
#     return output

class Range(object):
    def __init__(self):
        self.lower_bound = -1
        self.upper_bound = -1
    
    def __init__(self,lower_bound,upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

def find_range(input_list,input_number):
    first = 0
    lower_bound = -1
    upper_bound = -1
    last = len(input_list) - 1
    while first < last:
        mid = (first+last)/2
        if input_list[mid] < input_number:
            first = mid + 1
        else:
            last = mid

    if input_list[first] != input_number:
        return Range()
    else:
        lower_bound = first
    first = 0
    last = len(input_list) - 1
    while first < last:
        mid = (first + last)/2
        if (input_list[mid] < input_number + 1):
            first = mid + 1
        else:
            last = mid

    if(input_list[first] == input_number):
        upper_bound = first
    else:
        upper_bound = first-1
    return Range(lower_bound,upper_bound)

    def find_range(input_list, input_number):
        lst = []
        for index, num in enumerate(input_list):
            if num == input_number:
                lst.append(index)
        lst = sorted(lst)
        first = lst[0]
        last = lst[-1]
        return Range(first, last)