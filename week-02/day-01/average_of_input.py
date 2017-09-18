# Write a program that asks for 5 integers in a row,
# then it should print the sum and the average of these numbers like:
#
# Sum: 22, Average: 4.4

print("Give me 5 numbers to get the sum and avg of tham.")
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
print(int(a + b + c + d + e) , " is the sum, and the avg is " , float((a + b + c + d + e)/5))