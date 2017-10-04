# Write a program that stores 3 sides of a cuboid as variables (doubles)
# The program should write the surface area and volume of the cuboid like:
# 
# Surface Area: 600
# Volume: 1000

# V = l × w × h 

length = float(input("Give me the length(cm): "))
width = float(input("Give me the width(cm): "))
heigh = float(input("Give me the heigh(cm): "))


def surface(l, w, h):
    s = 2 * l * w + 2 * l * h + 2 * w * h
    print("The Surface Area is " , s , "cm^2 of the cuboid.") 
    return s
s = surface(length, width, heigh)

def volume(l, w, h):
    v = s * h
    print("The Volume is " , v , "cm^2 of the cuboid.") 
    return v
v = volume(length, width, heigh)
print()
