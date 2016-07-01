"""Hangman"""

import random

guesses_allowed = 8
fail_counter = 0
letter_list = []


def hangman():
    global fail_counter
    global letter_list

    dead = '''
      _______
     |\      |
     |      (_)
     |      \|/
     |       |
     |      L L
     |
 jgs_|___
 '''

    WORDS = ["fishsticks", "cartman", "imaginationland", "kenny", "garrison", "randy", "colorado", "cheesin"]
    word = random.choice(WORDS)
    finished = printit(word, '')

    while finished is not True:

        is_a_letter = False
        letter = ''
        while is_a_letter is False:
            letter = raw_input("Please guess a letter: ")
            is_a_letter = len(letter) == 1 and letter.isalpha

        letter_list.append(letter)

        finished = printit(word, letter)
        print " "
        print "Failed guesses: ", fail_counter

        if fail_counter == guesses_allowed:
            print dead
            break

    if finished:
        print "You win!!"
    else:
        print "You lost! The word was: " + word

    again = raw_input("Do you want to play again? (y/n) ")
    if again == 'y':
        fail_counter = 0
        letter_list = []
        hangman()


def printit(word, guess):
    global fail_counter
    finished = True
    letter_failed = True
    result = ''
    for letter in word:
        if guess == letter or guess == '':
            letter_failed = False
        if letter in letter_list:
            result += " " + letter + " "
        else:
            finished = False
            result += " _ "
    if letter_failed:
        fail_counter += 1

    print result
    return finished


hangman()
        
        
    