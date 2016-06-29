    
import random

def hangman():

    """ A simple python based hangman game that loops over a list of words. The word used
    is selected randomly and the letters are replaced by the .replace() function in 
    python. Would like to incorperate Angular JS. Enjoy!

    """
    
    guess_counter = 0
    fail_counter = 0
    letter_list = []

    
    WORDS = [ "fishsticks", "cartman", "imaginationland", "kenny", "south park", 
            "garrison", "randy", "stan marsh", "new kid", "colorado", 
            "make love not warcraft", "trapped in the closet", "cheesin" ]
    
    word = random.choice(WORDS)
    
    i = 0
    while i < len(word):
        for char in word:
            line = word.replace(word, ' _ ')
            line_spaces = line * len(word)
            
            i += 1
    print line_spaces
    letter = raw_input("Please guess a letter: ")
    
    if len(letter) == 1 and letter.isalpha:
    
    # user inputs letter, check letter
        letter = False
        while not letter:
        
        
            if letter == char in word:
                letter_change = word.replace(char, letter)
                print "Success!"
                correct = True
                letter_list.append(letter)
                guess_counter += 1
            
            else:
                print "Incorrect! Please guess again"
                letter_again = raw_input("Guess: ") 
                fail_counter += 1
            

hangman()
        
        
    