# Pattern Matching
# A function takes in two strings 
def match_patterns(longer_string, key_string):
    # make the longer input string into a list so each word is an item
    longer_str_list = list(longer_string.split(" "))
    # set up the empty dictionary
    pattern_dict = {}
    # go through each letter in the shorter pattern to be followed and it's index
    for index, letters in enumerate(key_string):
        # check if the pattern "a" for instance is already in the dict
        if not pattern_dict.get(letters):
            # if it isnt, set it up with the index from the longer string "apple" for instance
            pattern_dict[letters] = longer_str_list[index]
        # otherwise check that the corresponding value is the same at the index "apple" again
        elif pattern_dict.get(letters) != longer_str_list[index]:
            return False
    # return True after going through the key_string 
    return True

print match_patterns("apple berry apple", "aba") # True
print match_patterns("apple berry cherry", "abc") # True
print match_patterns("yellow blue green", "abb") # False