# create a function that takes a number,
# divides ten with it,
# and prints the result.
# it should print "fail" if the parameter is 0

def divides_with_ten():
    try:
        num = int(input("Give me a nmber:"))
        result = 10 / num
        print(result)
    except ZeroDivisionError:
        print("FAIL")

        
divides_with_ten()
    
