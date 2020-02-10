import random

numberOfGuesses = 0
name = input('What is your name? ')
number = input('Hello ' + name + '!' + ' What number would you like to select? ')
print('So ' + name + ',' + ' you chose the number ' + number + '. Let\'s get started! ')

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
    print('The computer was able to guess your number in ' + numberOfGuess + ' tries :(')

if guess != number:
    number = str(number)
    print('The computer was not able to guess your number of ' + number)