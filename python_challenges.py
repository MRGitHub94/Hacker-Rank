def power_of_two_bitwise(n):
    # & is a bitwise AND
    return n > 0 and (n & (n - 1)) == 0

def is_power_of_three(n):
    # divisible by 3 
    while (n % 3 == 0):
        # reduce n by three
        n /= 3
    return n == 1

def is_power_of_four(n):
    
    while n and not (n & 0b11):
        n >>= 2
    return (n == 1)

def is_perfect_square(n): # Product of two equal integers
    x = n // 2
    y = set([x])
    while x * x != n:
        x = (x + (n //x)) // 2 
        if x in y:
            return False
        y.add(x)
    return True  