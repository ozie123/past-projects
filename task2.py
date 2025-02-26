import random
import time

# Function to load words from the dictionary.txt file into a list
def load_words(file_name):
    words_list = []
    try: 
        with open(file_name, "r") as file: # open the file
            for line in file: # read the file line by line
                word = line.strip()
                if len(word) == 5: # only adds a 5-letter words 
                    words_list.append(word)
    except FileNotFoundError:
        print("Error: The dictionary file is missing.")

    return words_list


# Function to select a random word of the specified length from the words_list
def select_random_word(word_length, words_list):
    valid_words = [word for word in words_list if len(word) == word_length]
    if len(valid_words) > 0:
        return random.choice(valid_words)# Return a random word form the list
    else:
        return None

# Function to get the user's guess and ensure it is valid
def get_guess():
    print("You have 30 seconds to guess a 5 letter word:")
    start_time = time.time() # Records the start time
    guessed_word = input("Enter your guess:").strip().lower()
    elapsed_time = time.time() - start_time # Calculates how much time has passed 
    if elapsed_time > 30:
        print("Time's up! You took too loong to guess.")
        return None
    return guessed_word

# Function to check if the guessed word exists in the dictionary
def is_valid_guess(guess, dictionary):
    return guess in dictionary

# Function to provide feedback on the guess (clue generation)
def provide_clue(user_guess, correct_answer):
    clue = []
    for i in range(len(user_guess)):
        if user_guess[i] == correct_answer[i]:
            clue.append("*")# Correct letter in the correct postion
        elif user_guess [i] in correct_answer:
            clue.append("+") # Correct letter in the wrong position
        else:
            clue.append("_") # Incorrect letter
    return " ".join(clue)


# Function to handle the player's turn. It can return if the guess was correct, the clue and previous guesses
def handle_turn(guess, answer, dictionary, past_guesses):
   if not guess:
       return False, "you lost a turn for taking too long."
   if not is_valid_guess(guess, dictionary):
       return False, "Invalid word! Try again."
   
   past_guesses.append(guess) #add the guess to past guesses
   clue = provide_clue (guess, answer)
   if guess == answer:
       return True, f"you guessed it! The word was '{answer}'."
   return False, clue
       

# Function to display the game result (win/loss)
def display_result(is_winner, answer):
    if is_winner:
         print("Congratulations! You won!")
    else:
        print(f"Game over! The correct word was: '{answer}'.")

# Function to handle the player's decision to give up
def give_up(answer): # this function gives the option to give up on the game
    if input("Do you give up? this does not end your turn (y/n): ").lower() == 'y':
        print(f"The correct word was: '{answer}'. Better luck next time!")
        return True
    
# Function to handle the main game loop
def main():
    words_list = load_words("dictionary.txt")

    if not words_list:
        return

    answer = select_random_word(5, words_list)

    if not answer:
        print("Error: No 5-letter words found in the dictionary.")
        return

    past_guesses = []

    is_winner = False

    while not is_winner and len(past_guesses) < 6:
        guess = get_guess()
        is_winner, feedback = handle_turn(guess, answer, words_list, past_guesses)
        print(feedback)
        if is_winner or len(past_guesses) == 6:
            break
            
    if not is_winner:
        display_result(is_winner,answer)
        if give_up(answer):
            return
        
if __name__ == "__main__":
    main()