def push_first(lst):
    a = [0 for i in range(lst.count(0))]
    x = [i for i in lst if i != 0]
    x.extend(a)
    return x
    

print push_first([0,2,3])

def find_len_last_word(string):
     list_of_words = string.split(" ")
     print list_of_words
     return len(list_of_words[-1])

print find_len_last_word("There are some things")