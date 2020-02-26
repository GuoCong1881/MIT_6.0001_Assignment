# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

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


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    splited_word = list(secret_word)
    splited_word_copy = splited_word[:]
    for a in splited_word_copy:
        if a in letters_guessed:
            splited_word.remove(a)
    return splited_word == []
    

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    splited_word = list(secret_word)
    known_word_list = []
    for a in splited_word:
        if a in letters_guessed:
            known_word_list.append(a)
        else:
            known_word_list.append('_ ')
    known_word = ''.join(known_word_list)
    return known_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letter_list = list(string.ascii_lowercase)
    letter_list_copy = letter_list[:]
    for a in letters_guessed:
        letter_list_copy.remove(a)
    available_letter = ''.join(letter_list_copy)
    return available_letter


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
    secret_word_list = list(secret_word)
    secret_word_list_copy = secret_word_list[:]
    count_unique = []
    letters_guessed = []
    guesses_remaining = 6
    warnings_remaining = 3
    for a in secret_word_list:
        if a in count_unique:
            secret_word_list_copy.remove(a)
        else:
            count_unique.append(a)
    unique_no = len(count_unique)
    print ("Welcome to the game Hangman!\nI am thinking of a word that is",\
           len(secret_word_list),\
           "letters long.\nYou have",warnings_remaining,"warnings left."\
           "\n----------------")
    while guesses_remaining > 0:
        print ("\nYou have", guesses_remaining, "guesses left." \
               "\nAvailable letters:", get_available_letters(letters_guessed))
        guess_input = input ("Please guess a letter: ")
        if warnings_remaining > 0:
            if str.isalpha(guess_input) == True:
                if str.lower(guess_input) in letters_guessed:
                    warnings_remaining-=1
                    print("Oops! You've already guessed that letter. You have", \
                          warnings_remaining, "warnings left: ", \
                          get_guessed_word(secret_word, letters_guessed), \
                          "\n----------------")
                else:
                    letters_guessed.append(str.lower(guess_input))
                    if str.lower(guess_input) in secret_word_list:
                        print("Good guess: ", get_guessed_word(secret_word, letters_guessed), \
                              "\n----------------")
                    else:
                        print("Oops! That letter is not in my word." \
                              "\nPlease guess a letter: ", \
                              get_guessed_word(secret_word, letters_guessed), \
                              "\n----------------")
                        if str.lower(guess_input) in ['a','e','i','o']:
                            guesses_remaining -= 2
                        else:
                            guesses_remaining -= 1
            else:
                warnings_remaining-=1
                print("Oops! That is not a valid letter. " \
                      "You have", warnings_remaining, "warnings left:", \
                      get_guessed_word(secret_word, letters_guessed), \
                      "\n----------------")
        else:
            if str.isalpha(guess_input) == True:
                if str.lower(guess_input) in letters_guessed:
                    guesses_remaining-=1
                    print("Oops! You've already guessed that letter. You have no warning left. " \
                          "so you lose one guess: ", \
                          get_guessed_word(secret_word, letters_guessed), \
                          "\n----------------")
                else:
                    letters_guessed.append(str.lower(guess_input))
                    if str.lower(guess_input) in secret_word_list:
                        print("Good guess: ", get_guessed_word(secret_word, letters_guessed))
                    else:
                        print("Oops! That letter is not in my word. " \
                              "Please guess a letter: ", \
                              get_guessed_word(secret_word, letters_guessed), \
                              "\n----------------")
                        if str.lower(guess_input) in ['a','e','i','o']:
                            guesses_remaining -= 2
                        else:
                            guesses_remaining -= 1
            else:
                guesses_remaining-=1
                print("Oops! That is not a valid letter. " \
                      "You have no warnings left. " \
                      "\nso you lose one guess: ", \
                      get_guessed_word(secret_word, letters_guessed), \
                      "\n----------------")
        if is_word_guessed(secret_word, letters_guessed)==True:
            print("Congratulations, you won!" \
                  "\nYour total score for this game is:",\
                  guesses_remaining*unique_no)
            break
    if guesses_remaining == 0:
        print("sorry, you ran out of guesses. The word was", secret_word)

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
    trimmed_word = my_word.replace(' ','')
    trimmed_word_list = list(trimmed_word)
    other_word_list = list(other_word)
    i = 0
    if len(trimmed_word_list) == len(other_word_list):
        while i < len(trimmed_word_list):
            if trimmed_word_list[i] == '_':
                if other_word_list[i] in trimmed_word_list:
                    match = False
                    break
                else:
                    i += 1
            else:
                if trimmed_word_list[i] == other_word_list[i]:
                    i += 1
                else:
                    match = False
                    break  
            if i == len(trimmed_word_list)-1:
                match = True
    else:
        match = False
    return match


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
    match_wordlist=[]
    for word in wordlist:
        if match_with_gaps(my_word, word):
            match_wordlist.append(word)
    if len(match_wordlist) == 0:
        print("No matches found")
    else:
        print(match_wordlist)
    return match_wordlist


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
    secret_word_list = list(secret_word)
    secret_word_list_copy = secret_word_list[:]
    count_unique = []
    letters_guessed = []
    guesses_remaining = 6
    warnings_remaining = 3
    for a in secret_word_list:
        if a in count_unique:
            secret_word_list_copy.remove(a)
        else:
            count_unique.append(a)
    unique_no = len(count_unique)
    print ("Welcome to the game Hangman!\nI am thinking of a word that is",\
           len(secret_word_list),\
           "letters long.\nYou have",warnings_remaining,"warnings left."\
           "\n----------------")
    while guesses_remaining > 0:
        print ("\nYou have", guesses_remaining, "guesses left." \
               "\nAvailable letters:", get_available_letters(letters_guessed))
        guess_input = input ("Please guess a letter: ")
        if warnings_remaining > 0:
            if str.isalpha(guess_input) == True:
                if str.lower(guess_input) in letters_guessed:
                    warnings_remaining-=1
                    print("Oops! You've already guessed that letter. You have", \
                          warnings_remaining, "warnings left: ", \
                          get_guessed_word(secret_word, letters_guessed), \
                          "\n----------------")
                else:
                    letters_guessed.append(str.lower(guess_input))
                    if str.lower(guess_input) in secret_word_list:
                        print("Good guess: ", get_guessed_word(secret_word, letters_guessed), \
                              "\n----------------")
                    else:
                        print("Oops! That letter is not in my word." \
                              "\nPlease guess a letter: ", \
                              get_guessed_word(secret_word, letters_guessed), \
                              "\n----------------")
                        if str.lower(guess_input) in ['a','e','i','o']:
                            guesses_remaining -= 2
                        else:
                            guesses_remaining -= 1
            else:
                if guess_input == '*':
                    print("Possible word matches are: ", \
                          show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
                else:
                    warnings_remaining-=1
                    print("Oops! That is not a valid letter. " \
                          "You have", warnings_remaining, "warnings left:", \
                          get_guessed_word(secret_word, letters_guessed), \
                          "\n----------------")
        else:
            if str.isalpha(guess_input) == True:
                if str.lower(guess_input) in letters_guessed:
                    guesses_remaining-=1
                    print("Oops! You've already guessed that letter. You have no warning left. " \
                          "so you lose one guess: ", \
                          get_guessed_word(secret_word, letters_guessed), \
                          "\n----------------")
                else:
                    letters_guessed.append(str.lower(guess_input))
                    if str.lower(guess_input) in secret_word_list:
                        print("Good guess: ", get_guessed_word(secret_word, letters_guessed))
                    else:
                        print("Oops! That letter is not in my word. " \
                              "Please guess a letter: ", \
                              get_guessed_word(secret_word, letters_guessed), \
                              "\n----------------")
                        if str.lower(guess_input) in ['a','e','i','o']:
                            guesses_remaining -= 2
                        else:
                            guesses_remaining -= 1
            else:
                if guess_input == '*':
                    print("Possible word matches are: ", \
                          show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
                    guesses_remaining-=1
                    print("Oops! That is not a valid letter. " \
                          "You have no warnings left. " \
                          "\nso you lose one guess: ", \
                          get_guessed_word(secret_word, letters_guessed), \
                          "\n----------------")
        if is_word_guessed(secret_word, letters_guessed)==True:
            print("Congratulations, you won!" \
                  "\nYour total score for this game is:",\
                  guesses_remaining*unique_no)
            break
    if guesses_remaining == 0:
        print("sorry, you ran out of guesses. The word was", secret_word)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


#if __name__ == "__main__":
#    # pass
#
#    # To test part 2, comment out the pass line above and
#    # uncomment the following two lines.
#    
#secret_word = choose_word(wordlist)
#hangman(secret_word)


###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
secret_word = choose_word(wordlist)
hangman_with_hints(secret_word)
