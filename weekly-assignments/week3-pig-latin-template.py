
# helpful function to see if word starts with vowel
def starts_with_vowel(word):
    """
    Return True if the work starts with a vowel, False otherwise
    :param word: A word as a string
    :return: Whether the word begins with a vowel
    """

    # make word lower case
    word = word.lower()

    # check all combinations
    if word[0] == 'a' or word[0] == 'e' \
            or word[0] == 'i' or word[0] == 'o' or word[0] == 'u':
        return True
    else:
        return False


def main(sentence):
    """
    A function to translate a normal sentence into pig latin
    :param sentence: An 'english' language sentence
    :return: A 'pig latin' sentence
    """
    # a variable to hold the new sentence once it is created
    new_sentence = ""

    # break sentence in various words
    words = sentence.split(" ")

    # create new list to hold sentence
    pig_latin = list()

    # iterate through words in sentence changing each element as necessary
    # put each new word in a list that we will re-assemble
    for word in words:
        # word is too short. Do nothing.
        if len(word) < 3:
            # place the word in the pig_latin list
            ### your code here ###
            continue

        # starts with vowel, modify accordingly and put in list
        elif starts_with_vowel(word) == True:
            # modify the word and place in pig_latin list
            ### your code here ###
            continue

        # starts with consonant, modify accordingly  and put in list
        else:
            # modify word and place in pig_latin list
            ### your code here ###
            continue

    # re-assemble list of words into string
    for word in pig_latin:
        new_sentence += word + " "

    # do not modify this line
    return new_sentence


if __name__ == "__main__":
    # create a meaningful sentence. You may change this line
    sentence = "I bombed this problem in Introduction to Programming I hope you do better"

    # print out what you are to do
    print("Turn the following sentence into pig latin: ", sentence)

    # call your function to translate the sentence
    translation = main(sentence)

    # print out the results
    print("Your translation is: ",translation)