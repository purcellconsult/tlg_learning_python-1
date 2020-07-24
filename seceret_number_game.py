import random
secretnumber = random.randint(1, 100)
secretnumbergame= "Welcome to the secret number game ! ! ! !"
print(secretnumbergame.upper())
print()
guess = 0
while guess != secretnumber:
    guess = int(input("Guess any number between 1 and 100: "))

    if guess == secretnumber:
        print("You guessed it!")
        print("You win!")
        break

    elif guess < secretnumber:
        print("Guessed too low, try again")

    elif guess > secretnumber:
        print("Guessed too high, try again")
