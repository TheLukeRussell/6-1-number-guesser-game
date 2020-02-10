print("\t\t Think you can outsmart a computer in 2020?")
print("\n\t The computer should have the upperhand...")

import random

numberOfGuesses = 0
name = input('\n What is your name? ')
number = input('\n Hello ' + name + '!' + ' What number would you like to select? ')

print('\n So ' + name + ',' + ' you chose the number ' + number + '. Let\'s get started! ')

while numberOfGuesses < 10:
    guess = random.randint(1,100)
    guess = int(guess)
    print(guess)

    numberOfGuesses = numberOfGuesses + 1;
    guessesLeft = 10 - numberOfGuesses;

    if guess == number:
        break
    
if guess == number:
    numberOfGuesses = str(numberOfGuesses)
    print('\n The computer was able to guess your number in ' + numberOfGuess + ' tries :(')
    print('\n Silly human, did you really think you could beat a computer?')

if guess != number:
    number = str(number)
    print('\n The computer was not able to guess your number of ' + number)
    print('\n Congrats human... you have won this round')