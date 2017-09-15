import  random

generated_number = random.randint(0,100)

user_input = (input("Guess a number between 1-100:                          # to calibrate the game type the following: 'set the game' \n"))

end = []
def set_generated_number(u_input,g_number):
    guess = ""
    if u_input == "set the game":
        from_number = input("Give me the lowest number: ")
        till_number = input("Give me the highest number: ")
        g_number = random.randint(int(from_number),int(till_number))
        print("The generated numbers will between" , from_number,"-", till_number)
        guess = int(input("Guess a number:"))
    else:
        guess = int(user_input)   
    return guess, g_number
     


guess, generated_number = set_generated_number(user_input, generated_number)


def turn_one(guess,generated_number):
    if guess == generated_number:
        print("Congratulations!!! You win!")
        
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
        print("Congratulations!!! You win!")
        
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
        print("Congratulations!!! You win!")
        
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
        print("Congratulations!!! You win!")
            
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
        print("Congratulations!!! You win!")
        
    elif guess > generated_number:
        print("Oooops, You have died...Unfortunately it is too high again...")
    else:
        print("Oooops, You have died...Unfortunately it is too high again...")
    return guess

turn_last(guess,generated_number)
print("The number was", generated_number,)
