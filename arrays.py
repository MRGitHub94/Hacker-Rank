"""Arrays: Left Rotation

Print out a single line of n space separated integers denoting the final state
of the array after performing d left rotations

Sample Input 
5 4 
1 2 3 4 5

Sample Output
5 1 2 3 4 
"""

def array_left_rotation(a, n, k):

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip.split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str, answer))