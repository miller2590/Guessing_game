# Guess the number game
import random
print("Hello, what is your name?")
name = input()

print("Well " + name + ", I am thinking of a number between 1 and 20.")
secret_number = random.randint(1, 20)

for guess_taken in range(1, 7):
    print("Take a guess.")
    guess = int(input())

    if guess < secret_number:
        print("Your guess is to low.")
    elif guess > secret_number:
        print("Your guess is to high.")
    else:
        break  # This condition is for correct guess

if guess == secret_number:
    print("Good job " + name + "! You guessed my number in " + str(guess_taken) + " guesses.")
else:
    print(" Nope, The number I was thinking of was " + str(secret_number))






