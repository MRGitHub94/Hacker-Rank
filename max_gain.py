def max_gain(input_list):
    # initialize the variable 
    max_gain = input_list[1] - input_list[0]
    # initialize the min number to the first value in the list
    min_num = input_list[0]
    i = 0
    # while loop runs through the length of the list
    while i < len(input_list):
        # check for a better max gain by subtracting the number by the min number
        if (input_list[i] - min_num > max_gain):
            max_gain = input_list[i] - min_num
        # check for a smaller min number
        if (input_list[i] < min_num):
            min_num = input_list[i]
        # increment the while loop 
        i += 1
    # control for negative max_gain
    return 0 if max_gain < 0 else max_gain

def max_gain(input_list):
    max = 0
    for i in range(0, len(input_list)):
        for j in range(i, len(input_list)):
            gain = input_list[j] - input_list[i]
            if gain > max:
                max = gain
    return max