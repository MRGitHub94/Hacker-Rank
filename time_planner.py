# The "Time Planner" Problem

# Implement a meeting planner that can schedule meetings between two persons at 
# a time.

# Time is represented by Unix format (also called Epoch) - a positive integer 
# holding the seconds since January 1st, 1970 at midnight. 

# Planner input:

# dur - Meeting duration in seconds (a positive integer).
# timesA, timesB - Availability of each person, represented by an array of 
# arrays. Each sub-array is a time span holding the start (first element) and 
# end (second element) times. You may assume that time spans are disjointed.

# Planner output:

# Array of two items - start and end times of the planned meeting, representing 
# the earliest opportunity for the two persons to meet for a dur length meeting.
# If no possible meeting can be scheduled, return an empty array instead.
# Design and implement an efficient solution and analyze its runtime 
# and space complexity.

# Test Cases
# timesA = [[8, 8.5], [10, 11], [13, 15]]
# timesB = [[9.5, 10], [13, 16]]
# dur = 3600
# >>> [13, 14]

# Need to check for overlap
# merge the times 
# go through the merged_list and find out if there are segments that are equal 
# or greater than the dur


# def plan_time(dur, timesA, timesB):
#     # Assuming military time
#     timesA = sorted(timesA)
#     timesB = sorted(timesB)

#     # this gets returned at the end of the function
#     earliest_meeting_time = []

#     # Go through the lists in the lists
#     for start_a, end_a in timesA:
#         for start_b, end_b in timesB:
#             # Establish the start 
#             if start_a <= end_b:
#                 earliest_start = start_a     
#             elif start_b <= end_a:
#                 earliest_start = start b
            




            # check that it's more or equal to dur

    # return earliest_meeting_time

# Helper function to convert to the appropriate time
def makeIntoSeconds(arr):
    newArr = []
    for a in arr:
        littleArr = []
        for b in a:
            littleArr += [3600*b]
        newArr += [littleArr]
    return newArr

def meetingTime(timesA, timesB, dur):
    for a in makeIntoSeconds(timesA):
        # check if the timesa block has sufficient duration
        if a[1] - a[0] >= dur:
            # iterate through b
             for b in makeIntoSeconds(timesB):
                # check for overlap
                if (a[0] <= b[0] and a[1] >= b[1]) or (a[0] >= b[0] and a[1] <= b[1]):
                    # is there enough overlap for the duration
                    if min(a[1], b[1]) - max(a[0], b[0]) >= dur:
                        # the plus dur is to be added to the start time
                        return [max(a[0], b[0]), max(a[0], b[0]) + dur]
    return []


# timesA = [[8, 8.5], [10, 11], [13, 15]]
# timesB = [[9.5, 10], [13, 16]]
# dur = 3600
# >>> [13, 14]
print meetingTime([[8, 8.5], [10, 11], [13, 15]], [[9.5, 10], [13, 16]], 3600)
