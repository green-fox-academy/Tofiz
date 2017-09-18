# Write a program that opens a file called "my-file.txt", then prints
# each of lines form the file.
# If the program is unable to read the file (for example it does not exists),
# then it should print an error message like: "Unable to read file: my-file.txt"

try:
    my_file = open("my_file.txt", "r")
    print(my_file.readline())
except FileNotFoundError:
    print("Unable to read file: my_file.txt")
