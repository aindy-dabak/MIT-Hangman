# Problem Set 2, hangman.py


'''
# Name:  Dabak, Aaron Yildong, Salvation, Tiva Katamfw
# Email: dabakaaron@gmail.com
# Phone: +234(9036951421)
'''

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string


#define a variable containing all letters--- This is to be used later
letters = string.ascii_lowercase


WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()




'''
Create function to determine if all the letters of the secret_word are guessed
Returns True if all of them have been guessed
'''
def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"]
    
    
    guess = ''
    guess = guess.join(letters_guessed)
    c = secret_word
    for i in guess:
        if i not in c:
            guess = guess.replace(i, '')
    
    check = []
    for e in secret_word:
        if e in letters_guessed:
            check.append(1)
    if len(check) == len(secret_word):
        return True
        
    
    

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    global display
    letters_correct = ['_ ']*len(secret_word)
    display = ''
    
    
    r = []
    for i in range(len(secret_word)):
        for n in letters_guessed:
            #print(n)
            if secret_word[i] == n:
                r.append(i)
    #print(r)
    p = []            
    for t in r:
        for y in range(len(secret_word)):
            if t == y:
                p = secret_word[t]
                letters_correct[t] = p
                
                
 
    display = display.join(letters_correct)
    print(display)
    
    
    
    



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    remainder = []
    for n in letters:
        if n not in letters_guessed:
            remainder.append(n)
    rem = ''
    rem = rem.join(remainder)
    return rem
    
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long')
    print('_ _ _ _ _ _ _ _ _ _ _ ')

    
    
    letters_guessed = []
    warnings = 4
    count = []
    guesses_left = 6
    
    while guesses_left > 0:
        
        
        
        print()
        print('You have ',guesses_left, ' guesses left ')
        print('available letters: ', get_available_letters(letters_guessed))
        
        
        
        x = input('Please guess a letter: ')
        x = x.lower()
        
        

        
        if x not in letters:
            print('Oops! That is not a valid letter. You have {} warnings left:    '.format(warnings), end ='')
            get_guessed_word(secret_word, letters_guessed)
            warnings -= 1
            if warnings < 0:
                print('You have no more warnings, you have lost a guess ')
                guesses_left -= 1
                warnings = 4
            
            
            
        if x in letters and x not in letters_guessed:
        

            letters_guessed.append(x.lower())
            if x.lower() in secret_word:
                print('Good guess: ', end ='')
                count.append(x)
            else:
                print('Oops! That letter is not in my word: ', end ='')
                guesses_left -= 1
                
        
            
            get_guessed_word(secret_word, letters_guessed)
            
            print('_ _ _ _ _ _ _ _ _ _ _ ')
            
            warnings = 4
            
            if x in ['a','e','i','o','u'] and x not in secret_word:
                guesses_left -= 1

                
        
                
        elif x in letters_guessed:
            if warnings > 1:
                print('Oops! You already guessed that letter. You now have {} warnings: '.format(warnings))
                warnings -= 1
            else:
                print('You have no more warnings, you have lost a guess ')
                guesses_left -= 1
                warnings = 4
                
                
                
        
        
        if is_word_guessed(secret_word, letters_guessed) == True:
            print()
            print('Congratulations you won!')
            break
        if guesses_left < 1:
            print()
            print('Sorry you ran out of guesses')
            print('The  word was {}'.format(secret_word))
        
    c = ''
    c = c.join(count)
    
    score = guesses_left * len(c)
    
    if is_word_guessed(secret_word, letters_guessed) == True:
        print('Your total score for this game is: {}'.format(score))
        

        
    


            
       
        

            
            
    
    
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    

    if len(my_word) != len(other_word):
        return False
    elif len(my_word) == len(other_word):
        reg = []
        count = -1
        for x in my_word:
            
            count += 1
            if x in letters:
                if x == other_word[count]:

                    
                    #print(x)
                    reg.append(1)
                else:
                    reg.append(0)
                    
                    


        check = True
        for x in reg:
            if x == 1:
                if x != reg[0]:
                    check = False
                    break
            else:
                check = False
                
        return check

                
            
            
            
            
        
        
        





def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    for other_word in wordlist:
        if match_with_gaps(my_word, other_word):
            print(other_word)
        


        
        
        
    
    
    
    
    



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long')
    print('_ _ _ _ _ _ _ _ _ _ _ ')

    
    
    letters_guessed = []
    warnings = 3
    count = []
    guesses_left = 6
    
    counting = 0
    other_word = secret_word
    my_word = ''
    unders  = ['_']*len(secret_word)
    empty = ''
    
    while guesses_left > 0:
        
        
        
        print()
        print('You have ',guesses_left, ' guesses left ')
        print('available letters: ', get_available_letters(letters_guessed))
        
        
        if counting == 0:
            print('you have one hint left')
            
        your_letter = input('Please guess a letter: ')
        your_letter = your_letter.lower()
        
        
        if your_letter == '*' and counting == 0:

            
            counting += 1
            r = []
            for i in range(len(secret_word)):
                for n in letters_guessed:
                    #print(n)
                    if secret_word[i] == n:
                        r.append(i)
            #print(r)
            p = []            
            for t in r:
                for y in range(len(secret_word)):
                    if t == y:
                        p = secret_word[t]
                        unders[t] = p
                        
                        
         
            empty = empty.join(unders)
            print(empty)
            my_word = empty
            show_possible_matches(my_word)
            
        elif your_letter == '*' and counting >= 0:
            print('you have used up your hints')

            
            

        elif your_letter != '*':
            if your_letter not in letters:
                print('Oops! That is not a valid letter. You have {} warnings left:    '.format(warnings), end ='')
                get_guessed_word(secret_word, letters_guessed)
                warnings -= 1
                if warnings < 0:
                    print('You have no more warnings, you have lost a guess ')
                    guesses_left -= 1
                    warnings = 4
                
                
                
            if your_letter in letters and your_letter not in letters_guessed:
            
    
                letters_guessed.append(your_letter.lower())
                if your_letter.lower() in secret_word:
                    print('Good guess: ', end ='')
                    count.append(your_letter)
                else:
                    print('Oops! That letter is not in my word: ', end ='')
                    guesses_left -= 1
                    
            
                
                get_guessed_word(secret_word, letters_guessed)
                
                print('_ _ _ _ _ _ _ _ _ _ _ ')
                
                warnings = 4
                
                if your_letter in ['a','e','i','o','u'] and your_letter not in secret_word:
                    guesses_left -= 1
    
    
                    
            
                    
            elif your_letter in letters_guessed:
                if warnings > 1:
                    print('Oops! You already guessed that letter. You now have {} warnings: '.format(warnings))
                    warnings -= 1
                else:
                    print('You have no more warnings, you have lost a guess ')
                    guesses_left -= 1
                    warnings = 4
                    
                    
                    
            
            
            if is_word_guessed(secret_word, letters_guessed) == True:
                print()
                print('Congratulations you won!')
                break
            if guesses_left < 1:
                print()
                print('Sorry you ran out of guesses')
                print('The  word was {}'.format(secret_word))
            
    c = ''
    c = c.join(count)
        
    score = guesses_left * len(c)
        
    if is_word_guessed(secret_word, letters_guessed) == True:
        print('Your total score for this game is: {}'.format(score))
        

    
   
      
    
    
    



    
 



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

    
    ###############--------------------################-------------------
    
    # To test part 3 re-comment out the above lines and 
    
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
