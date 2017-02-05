def push_first(lst):
    a = [0 for i in range(lst.count(0))]
    x = [i for i in lst if i != 0]
    x.extend(a)
    return x
    

print push_first([0,2,3])

def move_last(lst): 