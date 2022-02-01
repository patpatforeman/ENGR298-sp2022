# helpful function to see if word starts with vowel
def starts_with_vowel(word):
    if word[0] == 'a' or word[0] == 'e' \
            or word[0] == 'i' or word[0] == 'o' or word[0] == 'u' or word[0] == 'I' :
        return True
    else:
        return False


# create a meaningful sentence
sentence = "I bombed this problem in Introduction to C++ I hope you do better"

# break sentence in various words
words = sentence.split(" ")

# create new list to hold sentence
pig_latin=list()

# iterate through words in sentence

for i in words:
    if starts_with_vowel(i) == True:
        i += 'way'
        pig_latin.append(i)
    else:
        new = i[1:] + i[0] + 'ay'
        pig_latin.append(new)

# re-assemble list of words into string
new_sentence = ""
for w in pig_latin:
    new_sentence += w + " "

# print out final sentence
print(new_sentence)
