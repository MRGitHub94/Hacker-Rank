# You are given an m x n 2D image matrix (List of Lists) where each integer 
# represents a pixel. Flip it in-place along its horizontal axis.

# Example:

# Input image :  
#               1 1
#               0 0 
# Modified to :   
#               0 0
#               1 1

def flip_horizontal_axis(matrix): 
    # instantiate variables   
    r = len(matrix) - 1
    c = len(matrix[0]) - 1
    temp = 0
    i = 0
    # keep the loop running while halfway through the num of rows
    while i <= r/2:
        # here's a new variable too
        j = 0
        # keep this loop running while j is less than the num of cols
        while j <= c:
            # set the temp variable to the iterators of the while loop
            temp = matrix[i][j]
            # this does the horizontal swap
            matrix[i][j] = matrix[r-i][j]
            matrix[r-i][j] = temp
            # increment
            j = j+1
        i = i + 1

def flip_horizontal_axis(matrix):
    return matrix.reverse()

def flip_vertical_axis(matrix):    
    r = len(matrix) - 1
    c = len(matrix[0]) - 1
    temp = 0
    i = 0
    while i <= r:
        j = 0
        while j <= (c/2):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][c - j]
            matrix[i][c - j] = temp
            j = j + 1
        i = i + 1

def flip_vertical_axis(matrix):
    for i in range(len(matrix)):
        matrix[i] = matrix[i][::-1]
        
def flip_vertical_axis(matrix):
    for row in matrix:
        row.reverse()
    return matrix
