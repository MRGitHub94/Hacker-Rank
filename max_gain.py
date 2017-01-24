def max_gain(input_list):
    max_gain = input_list[1] - input_list[0]
    min_num = input_list[0]
    i = 0
    while i < len(input_list):
        if (input_list[i] - min_num > max_gain):
            max_gain = input_list[i] - min_num
        if (input_list[i] < min_num):
            min_num = input_list[i]
        i += 1
    return 0 if max_gain < 0 else max_gain