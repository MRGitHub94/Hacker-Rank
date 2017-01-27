# Insert a star inbetween common letters

def insert_star_between_pairs(a_string):
    # check for a None input
    if a_string is None:
        # breaks out of the function
        return None
    # base case - check if the string is only a character
    elif len(a_string) <= 1:
        # breaks out of the function
        return a_string
    # check if the first character is identical to the character next to it
    elif a_string[:1] == a_string[1:2]:
        # recursively call the rest of the list with a star inbtwn
        return a_string[:1] + "*" + insert_star_between_pairs(a_string[1:len(a_string)]) # b*b 
    
    return a_string[:1] + insert_star_between_pairs(a_string[1:len(a_string)]) # ab*b

print insert_star_between_pairs("abb")