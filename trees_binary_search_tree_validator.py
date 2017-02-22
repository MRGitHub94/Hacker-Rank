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
    # returns boolean
    return (root is None or 
            (root.data < max_ and root.data > min_ and 
             check(root.left, min_, root.data) and 
             check(root.right, root.data, max_)))

def check_binary_search_tree_(root):
    return check(root, -float('inf'), float('inf'))

# ==============================================================================
class TreeNode:
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self. right_child = right_child

class BinaryTree:
    def __init__(self, root_node=None):
        self.root = root_node

    def validate_BST_iterative(self, root):
        # within this function there is a class
        class TreeBoundaryNode:

            def __init__(self, tree_node=None, left_boundary=None, right_boundary=None):
                self.tree_node = tree_node
                self.left_boundary = left_boundary
                self.right_boundary = right_boundary

            if root == None or (root.left_child == None and root.right_child == None):
                return True

            queue = deque()
            queue.append(TreeBoundaryNode(root, -sys.maxint-1, sys.maxint))
            while queue:
                tree_binary_node = queue.popleft()
                tree_node = tree_binary_node.tree_node
                if (tree_node.data <= tree_binary_node.left_boundary) or (tree_node.data >= tree_binary_node.right_boundary):
                    return False

                if tree_node.left_child != None:
                    queue.append(TreeBoundaryNode(tree_node.left_child, tree_binary_node.left_boundary, tree_node.data))

                if tree_node.right_child != None:
                    queue.append(TreeBoundaryNode(tree_node.right_child, tree_node.data, tree_binary_node.right_boundary))

            return True 