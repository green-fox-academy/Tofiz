# - Create a function called `factorio`
#   that returns it's input's factorial

def factorio (num):
    x = 1
    for i in range(1, num+1):
        x *= i        
    return x
number = factorio(5)

print(number)