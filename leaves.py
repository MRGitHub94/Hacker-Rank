Count the leaves of a binary search tree

class TreeNode:
    def __init__(self, data, left_child = None, right_child = None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child 

class Binary_Tree:
    def __init__(self, root_node = None):
        self.root = root.node 

    def number_of_leaves(self, root):
        # Check for empty tree
        if root == None:
            return 0
        # if you're at the end of the tree
        if root.left_child == None and root.right_child == None:
            return 1
        # you need to recurse otherwise and add the two function calls together 
        return self.number_of_leaves(root.left_child) + self.number_of_leaves(root.right_child)


class BinaryTree:
    def __init__(self, root_node = None):
            self.root = root_node

    def number_of_leaves(self,root):
        if root is None: return 0
        
        stack, count = [root], 0
        
        while len(stack) > 0:
            node = stack.pop()
            
            if node.left_child is None and node.right_child is None:
                count += 1
                continue
            
            if node.left_child:
                stack.append(node.left_child)
                
            if node.right_child:
                stack.append(node.right_child)

        return count