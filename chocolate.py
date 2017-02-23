#Chocolate Time

# There are N students standing in a line where each student has some points. 
# Each student must have at least one chocolate and students with higher points
# get more chocolates than their neighbors.

# Write a method to computer the minimum number of chocolates distributed such
# that the above conditions are satisfied.

def distribute_chocolate(points):
    # check if there are points
    if not points:
        return 0
    # memoize num_chocolates variable    
    num_chocolates = [1]
    for i in range(1, len(points)):
        if points[i] > points[i-1]:
            num_chocolates.append(num_chocolates[i-1]+1)
        else:
            num_chocolates.append(1)
    result = num_chocolates[len(points)-1]
    for i in range(len(points)-2, -1, -1):
        if points[i] > points[i+1]:
            num_chocolates[i] = max(num_chocolates[i], num_chocolates[i+1] + 1)
        result += num_chocolates[i]
    return result

print distribute_chocolate([2,3,3,2,1,5,2]) # 2, 3, 3, 2, 1, 4, 2
# 12
print distribute_chocolate([1,5,7,1]) # 1, 2, 3, 1
# 7
print distribute_chocolate([])
# 0
print distribute_chocolate([2])
# 1