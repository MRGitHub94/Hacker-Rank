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
    r = len(matrix) - 1
    c = len(matrix[0]) - 1
    temp = 0
    i = 0
    while i <= r/2:
        j = 0
        while j <= c:
            temp = matrix[i][j]
            matrix[i][j] = matrix[r-i][j]
            matrix[r-i][j] = temp
            j = j+1
        i = i + 1