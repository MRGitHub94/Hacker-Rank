Recursive Postorder Traversal
post_ordered_list = []
class BinaryTree:

    def __init__(self, root_data):
        self.data = root_data
        self.left = None
        self.right = None

    def postorder(self):
        if self != None:
            if self.get_left():
                self.get_left().postorder()
            if self.get_right():
                self.get_right().postorder()
            post_ordered_list.append(self.get_root_val())

    def get_right(self):
        return self.right

    def get_left(self):
        return self.left

    def set_root_val(self, obj):
        self.data = obj

    def get_root_val(self):
        return self.data

    def preorder(self):
        pre_ordered_list.append(self.get_root_val())
        if self.get_left_child():
            self.get_left_child().preorder()
        if self.get_right_child():
            self.get_right_child().preorder()