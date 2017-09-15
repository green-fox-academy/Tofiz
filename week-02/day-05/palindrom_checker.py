print("'Palindrom checker' checks a word if is it exatly the same in reverse writing ")
word_one = input("Type a word: ")

print("Let me see, is it a palindrom? " )
word_two = word_one


# def anagram (word_one, word_two):
#     if word_one == word_two[::-1]:
#         print(True)
#     else:
#         print(False)

# anagram(word_one, word_two)

print(word_one == word_two[::-1])

