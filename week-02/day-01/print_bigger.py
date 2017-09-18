# Write a program that asks for two numbers and prints the bigger one

a = input("Give me a number: ")
b = input("Give me one more number: ")


try:
    if int(a) > int(b):
        print(a , "is the bigger")
    elif int(b) > int(a):
        print(b , "is the bigger")
    else:
        print("They are equal")
except ValueError:
    print("oops, that is not a number")
