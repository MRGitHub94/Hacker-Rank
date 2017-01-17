def check_binary_search_tree_(root, seen=None):
    if seen is None:
        seen = set()                         
    if root:
        if root.data in seen:
            return False
        else:
            seen.add(root.data)
            
        if not root.left and not root.right: #one node tree
            return True
        elif root.left and root.right: #it has kids
            if (root.data <= root.left.data) or (root.data >= root.right.data):
                return False
            return check_binary_search_tree_(root.left, seen) and check_binary_search_tree_(root.right, seen)
        else:
            return False
    
def check(root, min_, max_):
    return (root is None or 
            (root.data < max_ and root.data > min_ and 
             check(root.left, min_, root.data) and 
             check(root.right, root.data, max_)))

def check_binary_search_tree_(root):
    return check(root, -float('inf'), float('inf'))