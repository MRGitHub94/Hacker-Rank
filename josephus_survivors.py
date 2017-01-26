# Josephus Survivors 

# Return the node.data of the last survivor
# Defined node class 
def find_survivor(num_people, freq):
    # make a circular LL

    # want this to run until there's only one node left
    while node.next != node:
        # range() captures the number of people we skip
        for i in range(freq - 1):
            # this one is going to get cut out
            node = node.next

        # need to change the references of the LL (in this case it's a doubly-
        # linked list)
        node.prev.next = node.next
        node.next.prev = node.prev

        # increment in the while loop
        node = node.next

    return node.data