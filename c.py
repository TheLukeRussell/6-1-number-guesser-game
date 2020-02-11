class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(f"\t\t\t{bcolors.HEADER} Think you can outsmart a computer in 2020?{bcolors.ENDC}")
print(f"\n\t\t{bcolors.OKBLUE} The computer should have the upperhand...{bcolors.ENDC}")
print(f'\n\t{bcolors.WARNING} BEWARE, many have fallen {bcolors.ENDC}')

import random

numberOfGuesses = 0
name = input(f'\n{bcolors.FAIL} What is your name? {bcolors.ENDC}')
print(f'\n {bcolors.FAIL}Between 1-100, what number would you like to choose? {bcolors.ENDC}')
number = input()
print(f'{bcolors.OKBLUE}\n So ' + name + ',' + ' you chose the number ' + number + '. Let\'s get started!')
number = int(number)

print(f"{bcolors.WARNING}\n Type either 'lower' if your chosen number is lower than the guess, or 'higher' if it is higher{bcolors.ENDC}")

min = 1
max = 100

while numberOfGuesses < 10:

    guess = random.randint(min,max)

    numberOfGuesses = numberOfGuesses + 1
    guessesLeft = 10 - numberOfGuesses

    # if userInput.lower()=='':
    if guess == number:
        break

    userInput = input(str(guess) + '? ')

    if userInput.lower()=='lower':
        max = guess - 1

    if userInput.lower()=='higher':
        min = guess + 1

if guess == number:
    numberOfGuesses = str(numberOfGuesses)
    print(guess)
    print(name + ', ' + 'The computer was able to guess your number in ' + numberOfGuesses + ' guesses')

if guess != number:
    number = str(number)
    print(name + ', The computer was not able to guess your number of ' + number)