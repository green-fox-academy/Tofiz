word_one = ""


print("Anagrama checker:")
word_one = input("Type a word: ")
word_two = input("and an other:")


def anagram (word_one, word_two):
    if word_one == word_two[::-1]:
        print(True)
    else:
        print(False)

anagram(word_one, word_two)
# print(if word_one == word_two:)

# if word_one = word_two[::-1]:
