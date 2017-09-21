# Write a recursive function that takes one parameter: n and adds numbers from 1 to n.
def adds_numbers(n):
    if n <= 0:
        return 0
    else:
        print(n)
        return n + adds_numbers(n-1)
print("To add numbers from 1 to n is", adds_numbers(20))
        