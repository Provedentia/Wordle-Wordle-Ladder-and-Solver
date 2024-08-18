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





def get_AI_guess(guesses: list[str], feedback: list[str], secret_words: set[str], valid_guesses: set[str]):
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

    if len(guesses) > 0:
        temp_guess = guesses[-1]
        temp_feedback = feedback[-1]
        temp_secret_words = secret_words.copy()
        for i in range(5):
            if temp_feedback[i] == '-':
                for word in secret_words:
                    if temp_guess[i] in word and word in temp_secret_words:
                        temp_secret_words.remove(word)
            elif temp_feedback[i].islower():
                 for word in secret_words:
                    if (temp_guess[i] not in word or word[i] == temp_guess[i]) and word in temp_secret_words:
                        temp_secret_words.remove(word)
            elif temp_feedback[i].isupper():
                for word in secret_words:
                    if temp_guess[i] != word[i] and word in temp_secret_words:
                        temp_secret_words.remove(word)
            
        secret_words = temp_secret_words
        
       
        
        
        # Use set comprehension to filter secret_words
       
        
    if len(guesses) == 0:
        return 'COALS', secret_words
    elif len(guesses) == 1:
        return 'NITER', secret_words
    else:
        for word in secret_words:
                return word, secret_words
    return 'HUNKY', secret_words

                    

    
    ### END SOLUTION 

# TODO: Define and implement your own functions!

game_count = 0
num_guess_count = 0
incorrect_game = 0 
if __name__ == "__main__":
    # TODO: Write your own code to call your functions here
    secret_word = get_secret_word()
    guess_count = 0
    secret_words = get_secret_words()
    valid_guesses = get_valid_wordle_guesses()

    
    guesses = []
    feedbacks = []
    tf = False
    
    while len(guesses) < 6:
        current_guess, secret_words = get_AI_guess(guesses, feedbacks, secret_words, valid_guesses)
        feedback = get_feedback(current_guess, secret_word)
        guesses.append(current_guess)
        feedbacks.append(feedback)
        print(Back.WHITE + '       ')
        for i in range(len(guesses)):
            print(get_color(guesses[i], feedbacks[i]))
        print(Back.WHITE + '       ')
        if current_guess == secret_word:
            print(f'Congrats! The word was {secret_word}. You had {guess_count} guesses')
            game_count += 1
            guess_count += len(guesses)
            break
        elif current_guess != secret_word and len(guesses) == 6:
            print(f"The word was {secret_word} :(")
            incorrect_game += 1 
            game_count += 1
            guess_count += 6
    print(f'Accuracy: {1 - (incorrect_game / game_count)}')
    print(f'Avg Guesses: {guess_count / game_count}')
    
    
    