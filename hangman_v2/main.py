"""
1, print the log
2, choose a word
3, generate blanks
4, ask user
5, if letter in the word: display the letters, and keep on
6, if letter not in the word: count the lives
"""
import random

from hangman_words import word_list
from hangman_art import stages, logo

print(logo)
word = random.choice(word_list)
wordLenght = len(word)
print(word)

display = []
for _ in range(wordLenght):
    display += "_"

lives = 6
game_over = False

while not game_over:

    letter = input("Guess: ").lower()

    if letter in display:
        print(f"You have guessed the letter: {letter}")

    # update the display list
    for index in range(wordLenght):
        if letter == word[index]:
            display[index] = letter
    print(f'{"".join(display)}')

    # if
    if letter not in word:
        lives -= 1
        if lives == 0:
            print(f"You lose, the word is {word}.")
            game_over = True
        else:
            print(f"Hangman remains {lives} lives.")

    if "_" not in display:
        print(f"You won! the word is {word}.")
        game_over = True
