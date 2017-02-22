# Return the number of four-letter words in a sentence
def give_four(sentence):
    parsed = sentence.split(" ")
    count = 0
    for w in parsed:
        if len(w) == 4:
            count += 1
    return count

print give_four("Hey this has a four word situation.")
# >>> 3