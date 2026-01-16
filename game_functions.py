import random

# function to be used by game_1: Guess the Number
def pick_value(poss_values):
    x = random.choice(poss_values)   
    return x

# function to be used in game_2: Higher or Lower
def check_higher_lower(current_val, next_val, user_input):
    return True if ((current_val > next_val and user_input == 'l') or (next_val > current_val and user_input == 'h')) else False

# function to be used in game_3: Hangman
def process_guess(letter, board, word):
    letter_indices = []
    for index, l in enumerate(word):
        if l == letter:
            letter_indices.append(index)
    
    if len(letter_indices) > 0:
        print(f"Well done! {letter} is in the word")
        for index in letter_indices:
            board[index] = letter
        return True
    else:
        print(f"Sorry, {letter} is not in the word")
        return False
