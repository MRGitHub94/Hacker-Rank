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
        # inner loop iterator
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

# [0, 1]
def flip_vertical_axis(matrix):  
    # instantiate variables  
    r = len(matrix) - 1
    c = len(matrix[0]) - 1
    temp = 0
    i = 0
    # keep the loop running while i is less than the number of rows
    while i <= r:
        # iterator for inner while loop 
        j = 0
        # go through half the column length
        while j <= (c/2):
            # swap
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][c - j]
            matrix[i][c - j] = temp
            # increment j
            j = j + 1
        # increment i 
        i = i + 1

def flip_vertical_axis(matrix):
    for i in range(len(matrix)):
        matrix[i] = matrix[i][::-1]

def flip_vertical_axis(matrix):
    for row in matrix:
        row.reverse()
    return matrix

def transpose_matrix(matrix):
    # set variables 
    rows = len(matrix)
    cols = len(matrix[0])
    temp = 0

    # iterate through the rows 
    for i in range(0, rows):
        # start at the i+1 until the cols to compare across the diagonal
        for j in range(i+1, cols):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

def transpose_matrix(m):
    m[:] = map(list,zip(*m))

transpose_matrix([[1,0], [0,0]])
# >>> [[1,0],[0,0]]
transpose_matrix([[1,0,1],[1,0,1],[1,0,1]])
# >>> [[1,1,1],[0,0,0],[1,1,1]]
transpose_matrix([[1,2,3],[4,5,6],[7,8,9]])
# >>> [[1,4,7],[2,5,8],[3,6,9]]
