# Write a function that returns the values that have even indices

# Write a recursive funtion that returns the length of parameter list

# Needle in a haystack problem in the HB challenge book

# Write a function that performs the .split() method given a phrase and a splitter

def split(phrase, splitter):
    output = []
    i = 0
    while len(phrase) >= len(splitter) + 1:
        if phrase[i: len(splitter)+i] == splitter:
            output.append(phrase[:i])
            # need to rebind phrase
            phrase.remove(phrase[len(splitter)+i :])
            i = 0
        else:
            i += 1
    output.append(phrase)
    return output

print split("hello world", " ")