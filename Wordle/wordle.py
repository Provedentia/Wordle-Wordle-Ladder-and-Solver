import random
# To install colorama, run the following command in your VS Code terminal:
# python3 -m pip install colorama
from colorama import Fore, Back, Style, init
init(autoreset=True) #Ends color formatting after each print statement

from wordle_secret_words import get_secret_words
from valid_wordle_guesses import get_valid_wordle_guesses

def get_secret_word():
    secret_word = random.choice(list(get_secret_words()))
    return secret_word


def get_guess(secret_word, guess_count):
    guess = input("What is your guess: ").upper()
    while guess not in get_valid_wordle_guesses():
        guess = input("Invalid guess, try again (must be 5 letters and no special characters or numbers): ").upper()
    guess_count += 1
    if guess == secret_word:
        tf = True
    else:
        tf = False
    return guess, guess_count, tf
# print(get_guess())

def get_color(guess: str, feedback: str):
    color_string = Back.WHITE + ' '
    for i in range(5):
        if feedback[i] == '-':
            color_string += (Back.BLACK + guess[i])
        elif feedback[i].islower():
            color_string += (Back.YELLOW + guess[i])
        else:
            color_string += (Back.GREEN + guess[i])
    color_string += Back.WHITE + ' '
    return color_string


def get_feedback(guess: str, secret_word: str) -> list:
    '''Generates a feedback string based on comparing a 5-letter guess with the secret word. 
       The feedback string uses the following schema: 
        - Correct letter, correct spot: uppercase letter ('A'-'Z')
        - Correct letter, wrong spot: lowercase letter ('a'-'z')
        - Letter not in the word: '-'

        Args:
            guess (str): The guessed word
            secret_word (str): The secret word

        Returns:
            str: Feedback string, based on comparing guess with the secret word
    
        Examples
        >>> get_feedback("lever", "EATEN")
        "-e-E-"
            
        >>> get_feedback("LEVER", "LOWER")
                "L--ER"
            
        >>> get_feedback("MOMMY", "MADAM")
                "M-m--"
            
        >>> get_feedback("ARGUE", "MOTTO")
                "-----"

    
    '''
    ### BEGIN SOLUTION
    return_list = ['-'] * 5
    list_guess = list(guess.lower())
    list_secret_word = list(secret_word.lower())
    if guess.lower() == secret_word.lower():
        return secret_word.upper()
    for i in range(5):
        if guess[i].lower() == secret_word[i].lower():
            return_list[i] = secret_word[i].capitalize()
            list_guess[i] = ''
            list_secret_word[i] = '?'
    for i in range(5):
        if list_guess[i] in list_secret_word:
            return_list[i] = list_guess[i]
            list_secret_word[list_secret_word.index(list_guess[i])] = '?'
    
    return ''.join(return_list)
   
    ### END SOLUTION 





def get_AI_guess(guesses: list[str], feedback: list[str], secret_words: set[str], valid_guesses: set[str]) -> str:
    '''Analyzes feedback from previous guesses/feedback (if any) to make a new guess
        
        Args:
         guesses (list): A list of string guesses, which could be empty
         feedback (list): A list of feedback strings, which could be empty
         secret_words (set): A set of potential secret words
         valid_guesses (set): A set of valid AI guesses
        
        Returns:
         str: a valid guess that is exactly 5 uppercase letters
    '''
    ### BEGIN SOLUTION

    ### END SOLUTION 

# TODO: Define and implement your own functions!


if __name__ == "__main__":
    # TODO: Write your own code to call your functions here
    secret_word = get_secret_word()
    guess_count = 0
    
    guesses = []
    feedbacks = []
    tf = False
    while tf == False and guess_count < 6:
        current_guess, guess_count, tf = get_guess(secret_word, guess_count)
        feedback = get_feedback(current_guess, secret_word)
        guesses.append(current_guess)
        feedbacks.append(feedback)
        print(Back.WHITE + '       ')
        for i in range(len(guesses)):
            print(get_color(guesses[i], feedbacks[i]))
        print(Back.WHITE + '       ')
    if tf == True:
        print(f'Congrats! The word was {secret_word}. You had {guess_count} guesses')
    else:
        print(f"The word was {secret_word} :(")
    
    