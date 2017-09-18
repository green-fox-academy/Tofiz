# Write a program that reads a number from the standard input, then draws a
# triangle like this:
#
# *
# **
# ***
# ****
#
# The triangle should have as many lines as the number was

size = int(input("Give me the size of the triangle"))

for i in range(size):
    i +=  1
    print("*" * i)
    

