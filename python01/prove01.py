import random

print("This is the \"guess a number\" game.")

print("You try to guess a random number in the smallest number of attempts.")

value_max = int(input("Pick a positive integer: "))
value_random = random.randint(1, value_max)

userGuesses = []
n = input("Guess a number between 1 and " + str(value_max) + ".\n")
userGuesses.append(n)
i = 1

while value_random != n:
    if n > value_random:
        n = input("Too high!\n")
    elif n < value_random:
        n = input("Too low!\n")
    userGuesses.append(n)
    i += 1


print("You were able to find the number in " + str(i) + " guesses.")
print("The numbers you guessed were: " + str(userGuesses))
