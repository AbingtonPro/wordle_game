# Test program for determining letter colors in a guess
# Incorporates logic from ChatGPT

import os

def clear_console():
    os.system('cls')  


def analyze_wordle_guess(secret_word, guess, guess_colors):
    correct_colors = 0
    correct_positions = 0
    guess_colors = ['B','B','B','B','B']
    # Create a copy of the secret word to keep track of used positions
    secret_word_copy = list(secret_word)

    # Check for correct colors and positions
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            correct_positions += 1
            guess_colors[i] = 'G'
            secret_word_copy[i] = ''  # Mark the position as used

    # Check for correct colors in the wrong position
    for i in range(len(secret_word)):
        if guess[i] != secret_word[i] and guess[i] in secret_word_copy:
            correct_colors += 1
            guess_colors[i] = 'Y'
            # Mark the position as used to avoid double counting
            secret_word_copy[secret_word_copy.index(guess[i])] = ''

    return correct_positions, correct_colors, guess_colors

# Example usage
if __name__ == "__main__":
    clear_console()
    while True:
        print()
        secret_word = input('  Enter secret word  : ')

        while True:

            if secret_word == '':
                break
            else:
                guess =       input('  Enter guess        : ')
                if guess == '':
                    break

                else:
                    results = []
                    correct_positions, correct_colors , results = analyze_wordle_guess(secret_word, guess, results)

                    print(f"    Correct positions: {correct_positions}")
                    print(f"    Correct colors   : {correct_colors}")
                    print("    Letter colors    : ", end='')
                    for k in range(5):
                        print(results[k], end='')
                    print()
                    print()

    print()
    print('  Exiting program')
    print()
    exit()

