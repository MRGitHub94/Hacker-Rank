# Determine the ASCII difrerence between two strings
from collections import Counter
def different_ascii(string1, string2):
    dict_1 = Counter(string1)
    dict_2 = Counter(string2)
    # print dict_1
    # print dict_2
    difference_1 = []
    ascii_difference = 0
    for k,v in dict_1.items():
        if k not in dict_2:
            difference_1.append((k,v))
        else:
            if v != dict_2[k]:
                difference_1.append((k,v))
    for k,v in dict_2.items():
        if k not in dict_1:
            difference_1.append((k,v))
        else:
            if v != dict_1[k]:
                difference_1.append((k,v))
    for k,v in difference_1:
        ascii_difference += (ord(k)*v)
    return ascii_difference
    # difference_2 = {k:v for k,v in dict_1.items() if k not in dict_2}
    # difference_1 = {k:v for k,v in dict_1.items() if k not in dict_2 or v != dict_1[k]}
    # print difference_1
    # print difference_2


print different_ascii("cat", "at")
# >>> 99

print different_ascii("cat", "bat")
# >>> 197