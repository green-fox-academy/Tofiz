# Write a program that asks for two integers
# The first represents the number of chickens the farmer has
# The seconf represents the number of pigs the farmer has
# It should print how many legs all the animals have

chickens = int(input("How many chickens do You count? "))
pigs = int(input("How many pigs do You count? "))

legs = (chickens * 2) + (pigs * 4)

print("Soo, there must be ", legs ," legs.")