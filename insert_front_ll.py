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
    # set up last variable
    last = None
    # set up current to start at the head
    current = self.head
    # make sure you aren't at the tail 
    while current is not None:
        # set up next to be the next node
        next = current.getNext()
        # use set last to change the reference
        current.setNext(last)
        # set up last to be the current node
        last = current
        # current moves to the next
        current = next 
    # return self.head as the last
    self.head = last

def reverse(self):
        current = None
        next = self.head
        while next:
            next, current, prev = next.getNext(), next, current
            current.setNext(prev)

        self.setHead(current)
class SinglyLinkedList:
    #constructor
    def __init__(self):
        self.head = None
        
    #method for setting the head of the Linked List
    def setHead(self,head):
        self.head = head
                     
    #method for inserting a new node at the end of a Linked List   
    def insertAtEnd(self,data):
        # initialize Node instance
        newNode = Node()
        # set new node's data
        newNode.setData(data)

        # if there is no node set the head
        if self.head == None:
            self.head = newNode
        else:
            # instantiate current
            current = self.head
            # set while loop while the LL hasn't reached the end
            while current.getNext() != None:
                current = current.getNext()
            # once you reach the last node set the next one to be the newNode
            current.setNext(newNode)
