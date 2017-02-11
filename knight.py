# KnightL on a chessboard

# KnightL is a chess piece that moves in a L shape. We define the possible 
# moves of KnightL(a,b) as any movement from some position (x, y) to some (x, y)
# satisfying either of the following:

# Observe that for each possible movement, the Knight moves 2 units in one 
# direction and 1 unit in the perpendicular direction.

# Given the value of n for a nXn chessboard, answer the following question for 
# each (a,b) pair:

# What is the minimum number of moves it takes KnightL(a,b) to get from position 
# (0,0) to position (n-1, n-1)? If it's not possible for the knight to reach 
# that destination, the answer is -1 instead. 

# Then print each KnightL(a,b) according to the output format specified below.

# Sample input 
# 5

# Sample output
# 4 4 2 8
# 4 2 4 4 
# 2 4 -1 -1
# 8 4 -1 1 