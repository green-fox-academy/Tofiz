# - Create a variable named `ai`
#   with the following content: `[3, 4, 5, 6, 7]`
# - Print the sum of the elements in `ai`

ai = [3, 4, 5, 6, 7]

x = 0
for n in range(0,len(ai)):
    x += ai[n]
print(x)

# An other solutions is:
print (sum(ai))
