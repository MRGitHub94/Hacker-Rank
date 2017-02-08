def find_partitions(input_list):
    # set up an output list to return at the end
    output = []
    # check for empty lists
    if input_list == None or len(input_list) == 0:
        return output
    # check for one length
    if input_list == 1:
        output.append(str(input_list[0]))
    # instantiate previous to be the first value in the list
    previous = input_list[0]
    # instantiate first to be the same as previous for now
    first = previous
    # set up an iterator
    i = 1
    # go through a while loop until the iterator is equal to the length of the list
    while i < len(input_list):
        # check if there's overlap at the current value in the list
        if(input_list[i] == previous + 1):
            # youre at the end of the list
            if(i == len(input_list) - 1):
                output.append(str(first)+"-"+str(input_list[i]))
        else: # there is no overlap so you set previous to this current value 
            if(first == previous): # if it's the first entry in the list
                output.append(str(first))
            else: 
                output.append(str(first) + "-"+str(previous))  
            if(i == len(input_list)-1):
                output.append(str(input_list[i]))
            # iterate through the while loop
            first = input_list[i]
        
        previous = input_list[i]
        i = i + 1

    return output