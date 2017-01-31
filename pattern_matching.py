# Pattern Matching
# A function takes in two strings 
def match_patterns(longer_string, key_string):
    longer_str_list = list(longer_string.split(" "))
    pattern_dict = {}
    for index, letters in enumerate(key_string):
        if not pattern_dict.get(letters):
            pattern_dict[letters] = longer_str_list[index]
        elif pattern_dict.get(letters) != longer_str_list[index]:
            return False
    return True

print match_patterns("apple berry apple", "aba") # True
print match_patterns("apple berry cherry", "abc") # True
print match_patterns("yellow blue green", "abb") # False