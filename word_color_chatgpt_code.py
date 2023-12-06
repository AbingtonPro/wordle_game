import os

def clear_console():
    os.system('cls')  


def analyze_wordle_guess(secret_word, guess):
    correct_colors = 0
    correct_positions = 0

    # Create a copy of the secret word to keep track of used positions
    secret_word_copy = list(secret_word)

    # Check for correct colors and positions
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            correct_positions += 1
            secret_word_copy[i] = ''  # Mark the position as used

    # Check for correct colors in the wrong position
    for i in range(len(secret_word)):
        if guess[i] != secret_word[i] and guess[i] in secret_word_copy:
            correct_colors += 1
            # Mark the position as used to avoid double counting
            secret_word_copy[secret_word_copy.index(guess[i])] = ''

    return correct_positions, correct_colors

# Example usage

while True:

    #if __name__ == "__main__":

    secret_word = input('  Enter secret word: ')
    guess =       input('  Ennter guess     : ')
    #secret_word = "python"
    #guess = "typhon"

    correct_positions, correct_colors = analyze_wordle_guess(secret_word, guess)

    print(f"Correct positions: {correct_positions}")
    print(f"Correct colors   : {correct_colors}")
    