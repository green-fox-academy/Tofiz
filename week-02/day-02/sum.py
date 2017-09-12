# - Write a function called `sum` that sum all the numbers
#   until the given parameter

n = int(input("Give me a number: "))

def sum(num):
    x = 0
    for i in range(1, num+1):
        x += i 
    return x
        # print(sum(x))
        
number = sum(n)

print(number)