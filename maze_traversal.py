# ==============================================================================
# Tree Traversals
# class Node(object):
#     def __init__(self, data, children):
#         self.data = data
#         self.children = children
    # def find(self, data):
    #     to_visit =[self]
    #     while to_visit:
    #         current = to_visit.pop()
    #         if current.data == data:
    #             return current
    #         to_visit.extend(current.children)

# Graph Traversals 

# class PersonNode(object):
#     def __init__(self, name, adjacent = None):
#         if adjacent is None:
#             adjacent = set()  
#         self.name = name
#         self.adjacent = adjacent

# class FriendGraph(object):
#     def __init__(self):
#         self.nodes = set()

#     def add_person(self, person):
#         self.nodes.add(person)

#     def set_friends(self, person1, person2):
#         person1.adjacent.add(person2)
#         person2.adjacent.add(person1)

"""Maze Traversal"""
grid =  [[0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0, 1],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 2]]

def find_end(x, y):
    if grid[x][y] == 2:
        print "Found goal at {}, {}".format(x, y)
        return True
    elif grid[x][y] == 1:
        print "Found wall at {}, {}".format(x, y)
        return False
    elif grid[x][y] == 3:
        print "Visited at {}, {}".format(x, y)
        return False

    print "visted {} {}".format(x, y)

    grid[x][y] = 3 # convert 0 to visited
    if ((x < len(grid)-1 and find_end(x+1, y))
        or (y > 0 and find_end(x, y-1))
        or (x > 0 and find_end(x-1, y))
        or (y < len(grid)-1 and find_end(x, y+1))):
        return True
    return False

find_end(0, 0)