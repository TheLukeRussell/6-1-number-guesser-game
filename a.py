import random #imports random number generator

numberOfGuesses = 0 #starting point of guesses
number = random.randint(1,100) #states the number is between 1 and 100

name = input('Hey player! What is your name? ') #gives user an input to state their name

print(name + ', I am thinking of a number between 1 and 100.  Do you think you can beat me?') #prints out the users name and adds a prompt

while numberOfGuesses < 10: #as long as guess is less than 10, these three lines will fire 
    guess = input('What is your guess? ') #guessing input
    guess = int(guess) #switches the guess into an integer

    numberOfGuesses = numberOfGuesses + 1;
    guessesLeft = 10 - numberOfGuesses;

    if guess < number:
        guessesLeft = str(guessesLeft)
        print('Your guess was lower than the expected value! You now have' + ' ' + guessesLeft + ' ' + 'guesses left')

    if guess > number:  
        guessesLeft = str(guessesLeft)
        print('Your guess was higher than the expected value! You now have' + ' ' + guessesLeft + ' ' + 'guesses left') 

    if guess == number:
        break

if guess == number:
    numberOfGuesses = str(numberOfGuesses)
    print('Awesome Work! You guessed the number in ' + numberOfGuesses + ' tries!!')

if guess != number:
    number = str(number)
    print('Oh dear... you were not able to guess ' + number + '. Come back and try again!')