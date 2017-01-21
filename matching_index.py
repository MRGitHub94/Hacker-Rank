# Brute Force O(n) runtime 
def matching_index(nums):
    # for n in range(len(nums)-1):
    #     if nums[n] - n == 0:
    #         return n
    # return -1

    for index, num in enumerate(nums):
        # print (index, num)
        if index == num: # check that it's the same number
            return index
    # this is unindented because the for loop needs to check each tuple first
    return -1


# Solution with binary search
def matching_index(arr):
    # set variable begin to 0
    begin = 0
    end = len(arr) - 1 # because list indices start at 0
    while begin <= end: 
        i = int((begin+end)/2) # binary search start in the middle
        print "i", i, "arr[i]", arr[i], "arr[i] - i", arr[i] - i
        if (arr[i] - i < 0):
            begin = i + 1
            print "begin", begin
        elif (arr[i] - i == 0):
            return i
        else:
            end = i - 1
            print "end", end
    return -1

print matching_index([-8, 0, 2, 5]) 
#>>> 2

print matching_index([-1, 0, 3, 6])
#>>> -1

print matching_index([-5, -3, 2, 3, 12]) # only will show the first time it matches
# >>> 2


