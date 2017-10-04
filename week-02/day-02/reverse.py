# - Create a variable named `aj`
#   with the following content: `[3, 4, 5, 6, 7]`
# - Reverse the order of the elements in `aj`
# - Print the elements of the reversed `aj`


one_line = ""
aj = [3, 4, 5, 6, 7]

for n in reversed(aj):
    one_line = one_line + str(n) + ", "
print(one_line)

print revers(aj)