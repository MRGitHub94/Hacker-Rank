"""Monica wants to buy one keyboard and one USB drive. 
n brands of keyboards, m brands of USB drives 
Exactly s dollars to spend (the total cost of her purchase must be maximal)
If she doesnt have enough money to buy one keyboard and one USB drive, print -1

"""

import sys

s,n,m = raw_input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = map(int,raw_input().strip().split(' '))
pendrives = map(int,raw_input().strip().split(' '))

Sample Input 
10 2 3
3 1 
5 2 8

s = 10 # Money to spend
n = 2 # Brands of keyboards
m = 3 # Brands of USBs 
keyboards = [3, 1] # price of each keyboard 
pendrives = [5, 2, 8] # price of each USB drive 
min_remainder = 0

# length of keyboards = n, length of penndrives = m


good_sum = []
for n in keyboards:
    for o in pendrives:
        if sum([n, o]) < s:
            good_sum.append(sum([n, o]))
best_result = max(good_sum)            
print best_result




best_keyboard, best_USB = max(keyboards), max(pendrives) # 3, 8
while best_keyboard + best_USB > min_remainder:
    if best_keyboard > best_USB:
        try:
            pendrives.pop(best_USB)
            best_USB = max(pendrives)
        except:
            pass
    else:
        try:
            keyboards.pop(best_keyboard)
            best_keyboard = max(keyboards) # pop either best_key or best_USB from each list to see if it fits 
        except:
            pass
print sum(best_keyboard, best_USB)

#IndexError pop index out of range
