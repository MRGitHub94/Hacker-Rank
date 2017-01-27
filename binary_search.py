"""Binary Search"""

def binary_search(lst, item):
    first = 0
    last = len(lst) - 1
    found = False

    while first <= last and not found:
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