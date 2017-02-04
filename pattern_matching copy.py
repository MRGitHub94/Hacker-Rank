# Pattern Matching
# A function takes in two strings 
def match_patterns(longer_string, key_string):
    # make the string into a list
    longer_str_list = list(longer_string.split(" "))
    # set up an empty dictionary
    pattern_dict = {}
    # go through the key_string
    for index, letters in enumerate(key_string):
        # check if the key is in the dict
        if not pattern_dict.get(letters):
            # if it isn't then you set it up
            pattern_dict[letters] = longer_str_list[index]
        # if the key is in the dict an it isn't matching the other value
        elif pattern_dict.get(letters) != longer_str_list[index]:
            # return False immediately
            return False
    return True

print match_patterns("apple berry apple", "aba") # True
print match_patterns("apple berry cherry", "abc") # True
print match_patterns("yellow blue green", "abb") # False