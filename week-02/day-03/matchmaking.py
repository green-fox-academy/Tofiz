# Join the two lists by matching one girl with one boy in the order list
# Exepected output: ["Eve", "Joe", "Ashley", "Fred"...]

# for loop solution

girls = ["Eve", "Ashley", "Bözsi", "Kat", "Jane"]
boys = ["Joe", "Fred", "Béla", "Todd", "Neef", "Jeff"]
order = []

length = len(girls) + len(boys)

for i in range(len(girls)):
    order = girls[i] + " : " + boys[i] 
    print(order)

# for loop solution in one line

girls = ["Eve", "Ashley", "Bözsi", "Kat", "Jane"]
boys = ["Joe", "Fred", "Béla", "Todd", "Neef", "Jeff"]
order = []

one_line = ""
length = len(girls) + len(boys)

for i in range(len(girls)):
    order = girls[i] + ", " + boys[i] + ", " 
    one_line += str(order)
print(one_line)

# easy solution
order = girls[0] + boys[0] + girls[1] + boys[1] + girls[2] + boys[2] + girls[3] + boys[3] + girls[4] + boys[4]


