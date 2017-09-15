import  random

generated_number = random.randint(0,100)

guess = int(input("Guess a number between 1-100:                          # to calibrate the game type the following: 'set the game' \n"))



def turn_one(guess,generated_number):
    # guess = guess
    if guess == generated_number:
        print("Congratulations!!! You won!")
    elif guess > generated_number:
        print("Too high.")
        guess = int(input ("You have 4 lives left. Guess again: "))
    else:
        print("Too low.")
        guess = int(input ("You have 4 lives left. Guess again: "))
    return guess

guess = turn_one(guess, generated_number)

def turn_secound(guess,generated_number):
    if guess == generated_number:
        print("Congratulations!!! You won!")
    elif guess > generated_number:
        print("Too high.")
        guess = int(input ("You have 3 lives left. Guess again: "))
    else:
        print("Too low.")
        guess = int(input ("You have 3 lives left. Guess again: "))
    return guess

guess = turn_secound(guess, generated_number)

def turn_third(guess,generated_number):
    if guess == generated_number:
        print("Congratulations!!! You won!")
    elif guess > generated_number:
        print("Too high.")
        guess = int(input ("You have 2 lives left. Guess again: "))
    else:
        print("Too low.")
        guess = int(input ("You have 2 lives left. Guess again: "))
    return guess

guess = turn_third(guess, generated_number)

def turn_fourth(guess,generated_number):
    if guess == generated_number:
        print("Congratulations!!! You won!")
    elif guess > generated_number:
        print("Too high.")
        guess = int(input ("You have 1 lives left. Guess again: "))
    else:
        print("Too low.")
        guess = int(input ("You have 1 lives left. Guess again: "))
    return guess

guess = turn_fourth(guess, generated_number)

def turn_last(guess,generated_number):
    if guess == generated_number:
        print("Congratulations!!! You won!")
    elif guess > generated_number:
        print("Unfortunately it is too high again...")
    else:
        print("Unfortunately it is too high again...")
    return guess

turn_last(guess,generated_number)
print("Oooops, You have died...The number was", generated_number,)
