# easy level :10 attempts;hard level: 5 attempts.
# You have {attempts} attempts remaining to guess the number.
# Make a guess:

# To high.
# Guess again.
# You've run out of guesses, you lose.
# You got it! The answer was {answer}.

#Number Guessing Game Objectives:
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

# This is a great progress for me ! feel so happy.20230822

import random
# from art import numberguesslogo
# print(numberguesslogo)

def level_index(level):
    if level == 'easy':
        attempts = 10
    else:
        attempts = 5
    return attempts

def check_guess(user_guess, answer, attempt):
    if user_guess > answer and attempt != attempts:
        print("Too high.")
        print("Guess again.")
    elif user_guess < answer and attempt != attempts:
        print("Too low.")
        print("Guess again.")
    elif user_guess > answer and attempt == attempts:
        print("Too high.")
        print("You've run out of guesses, you lose.")
    elif user_guess < answer and attempt == attempts:
        print("Too low.")
        print("You've run out of guesses, you lose.")
    else:
        print(f"You got it! The answer was {answer}.")

def number_guess(attempts):
    print(f"You have {attempts} attempts remaining to guess the number.")
    answer = random.randint(1,101)
    user_guess = int(input("Make a guess: "))

    # loop while user have attempts and the guess is not correct. 
    attempt = 1
    while attempt < attempts and user_guess != answer:
        check_guess(user_guess, answer, attempt)
        print(f"You have {attempts-attempt} attempts remaining to guess the number.")
        attempt += 1
        user_guess = int(input("Make a guess: "))
    return check_guess(user_guess, answer, attempt)


print("Welcome to the Number Gussing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = level_index(level)
number_guess(attempts = attempts)



