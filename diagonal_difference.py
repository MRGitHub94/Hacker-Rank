"""Given a square matrix of size NxN, calculate the absolute difference between
the sums of its diagonals. 

First line is the number of lines
Sample input 
3 
11 2 4
4 5 6
10 8 -12

Sample output 
15

The primary diagonal is 11 5 -12
so sum it up 4
Then the secondary diagonal is 
4 5 10 
so sum it up 19 
and then the difference of  those two diagonals up absolute value style to be 15

|4 - 19| = 15 """

import sys

n = int(raw_input().strip())
matrix = []
for a_i in xrange(n):
    a_temp = map(int, raw_input().strip().split(' '))
    matrix.append(a_temp)

    
# rows = len(matrix) 

# cols = len(matrix[0]) 

# # Assess that it's a square
# assert rows is cols, "Matrix must be a square!" # rows and cols are both ints

# sum_first_diagonal, sum_second_diagonal = 0, 0
# matrix[0][0] + matrix[1][1] + matrix[2][2] 
# matrix[0][2] + matrix[1][1] + matrix[2][0]
# # The row value in matrix is row - 1 
# for x in range(rows-1):
#     for y in range(cols-1):
#         sum_first_diagonal += matrix[rows+x][cols+y]
# print sum_first_diagonal


primSum,secSum = 0, 0    
#go through the rows
for row in xrange(n):
    primSum += matrix[row][row]
    secSum += matrix[row][n - 1 - row]
print abs(primSum - secSum)

a = [list(map(int, input().split())) for _ in range(int(input()))]
print(abs(sum([a[i][i]-a[i][-i-1] for i in range(len(a))])))