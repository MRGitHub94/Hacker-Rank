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

# def matching_index(arr):

print matching_index([-8, 0, 2, 5]) 
#>>> 2

print matching_index([-1, 0, 3, 6])
#>>> -1