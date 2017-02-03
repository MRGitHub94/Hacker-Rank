# Insert at the front of a singly-linked list

class Node:
    # A node has data and next capabilities
    def __init__(self):
        self.data = None
        self.next = None

    # set the data 
    def setData(self,data):
        self.data = data

    # function to get data when called in another function  
    def getData(self):
        return self.data
    
    # function to set the next node when called in another function 
    def setNext(self,next):
        self.next = next
    
    # function returns the next node when called in another function 
    def getNext(self):
        return self.next

# new class for the singly linked list
class SinglyLinkedList(object):
    # has a head node
    def __init__(self):
        self.head = None

    # this function sets the head node
    def set_head(self, head):
        self.head = head

    def insert_at_front(self, data):
        # make a new node instance
        new_Node = Node()
        # set the data to the new node
        new_Node.set_Data(data)

        # if there isn't a head node make this the head node
        if self.head == None:
            self.head = new_Node
        else:
            # use the setNext function to set the next node to be the head
            new_Node.setNext(self.head)
            # make the new node the head
            self.head = new_Node


  def insert_at_front(self,data):
        new_node = Node()
        new_node.setData(data)
        new_node.setNext(self.head)
        self.setHead(new_node)

    def reverse(self):
        last = None
        current = self.head
        while current is not None:
            next = current.getNext()
            current.setNext(last)
            last = current
            current = next 
        self.head = last