# - Create (dynamically) a two dimensional list
#   with the following matrix. Use a loop!
#
#   1 0 0 0
#   0 1 0 0
#   0 0 1 0
#   0 0 0 1
#
# - Print this two dimensional list to the output

n = int(input("Gimme the size of the matrix: "))

def matrix(num):
    outer = []
    for i in range(num):
        inner = []
        for j in range(num):
            if j == i:
                inner.append(1)
            else:
                inner.append(0)
        outer.append(inner)
    return(outer)
    
for l in matrix(n):
    print(l)
