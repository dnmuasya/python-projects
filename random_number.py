""" Module for random numbers"""
import random

number = random.randint(1,25)
number_of_guesses = 0

while number_of_guesses < 5:
    #validate the entry to ensure it's a number
    try:
        guess = input('Guess a number between 1 and 25: ')
        guess = int(guess)
        number_of_guesses += 1
        if guess > 25:
            print('Guess out of scope!!')
        elif guess < number:
            print('Guess value too low!')
        elif guess > number:
            print('Guess value too high!')
        
        else:
            print('Correct!!you guessed the number in '+str(number_of_guesses)+ ' tries!')
            break
    except ValueError:
        print('Please enter a valid number!')

    if guess == number:
        break

    elif number_of_guesses == 5:
        print('You did not guess the number in ' + str(number_of_guesses) + ' tries! The number was ' + str(number) + '.')
        break
    else:
        print('Try again.')

