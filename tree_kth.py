# Find the kth largest node in a BST
class BinaryTree:
    def __init__(self, root_node=None):
        # only contains the root_node 
        self.root = root_node

    def size(size, root):
        # Determines the size of the tree
        if root == None:
            # if there isn't a root, then the size is zero
            return 0
        else:
            # add the left and right child plus the root of the tree 
            # this keeps being called while there is a left and right child 
            return (self.size(root.left_child) + 1 + self.size(root.right_child))

    def find_kth_largest(self, root, k):
        # As a class method, self is passed in, as well as the root of the tree 
        # and the size k to be found
        if root == None:
            return None

        # instantiate right_size at zero, like a count variable 
        right_size = 0 

        # traverse the right size of the tree since the values on the right are
        # assumed greater than the values on the left
        # Keep going while there is somewhere to go
        if root.right_child != None:
            # call the size() function to determine how far right_size is
            right_size = self.size(root.right_child)

        # find when right_size + 1 is equal to the kth largest value we're 
        # searching for
        if right_size + 1 == k:
            # return the root of the tree
            return root
        # if k is less than the right_size
        elif k <= right_size:
            # call the function again with these parameters
            return self.find_kth_largest(root.left_child, k)
        # if k is greater than the right_size
        else:
            # We've gone too far!
            return self.find_kth_largest(root.left_child, k - right_size - 1)

class TreeNode:
    # sets up the tree
    def __init__(self,data, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child

    def __str__(self):
        return '{}'.forma(self.data)
