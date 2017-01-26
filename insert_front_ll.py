# Insert at the front of a singly-linked list

class Node:
    def __init__(self):
        self.data = None
        self.next = None
     
    def setData(self,data):
        self.data = data
      
    def getData(self):
        return self.data
     
    def setNext(self,next):
        self.next = next
     
    def getNext(self):
        return self.next

class SinglyLinkedList(object):
    def __init__(self):
        self.head = None

    def set_head(self, head):
        self.head = head

    def insert_at_front(self, data):
        new_Node = Node()
        new_Node.set_Data(data)

        if self.head == None:
            self.head = new_Node
        else:
            new_Node.setNext(self.head)
            self.head = new_Node