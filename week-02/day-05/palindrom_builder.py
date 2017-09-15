word = input("Let me make a word to a palindrom: " )
palindrome = ""


def palindrome_builder(creat_word):
    palindrome = creat_word + creat_word[::-1]
    return palindrome



print(palindrome_builder(word))
