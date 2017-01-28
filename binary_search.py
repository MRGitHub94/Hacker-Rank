"""Binary Search"""

def binary_search(lst, item):
    # instantiate variables
    first = 0
    last = len(lst) - 1 #capture the index
    found = False

    # run this loop until you exhuast all options or find the item
    while first <= last and not found:
        # midpoint gets rebinded each time the while loop runs
        midpoint = (first + last) // 2
        if lst[midpoint] == item:
            found = True
        else:
            if item < lst[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found

def binary_search_recursive(lst, item):
    if len(lst) == 0:
        return False 
    else:
        midpoint = len(lst) // 2
        if lst[midpoint] == item: 
            return True
        else: 
            if item < lst[midpoint]:
                return binary_search_recursive(lst[:midpoint], item)
            else:
                return binary_search_recursive(lst[midpoint + 1:], item)