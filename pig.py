def pig_latin(sentence):
    vowels = 'aeiou'
    words = sentence.split()
    result = []

    for word in words:
        if word[0] in vowels:
            result.append(word)
        else:
            result.append(word[1:] + word[0] + 'ay')
    
    return " ".join(result)

# Test cases
assert pig_latin("something") == "omethingsay"
assert pig_latin("awesome") == "awesome"
assert pig_latin("latin is a hard language") == "atinlay is a ardhay anguagelay"
assert pig_latin("y") == "yay"
assert pig_latin("e") == "e"

print("All tests passed!")
print("Discuss time and space complexity if there's time remaining")