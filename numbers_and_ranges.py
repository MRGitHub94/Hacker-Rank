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


def find_range(input_list,input_number):
    output = []
    for index, num in enumerate(input_list): 
        if index == input_number:
            output.append(num)
    return output
