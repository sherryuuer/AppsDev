# first version
from art import logo, vs
from game_data import data


def print_message(compare_a, against_b):
    print(logo)
    print(f"Compare A: {compare_a['name']}, {compare_a['description']}, from {compare_a['country']}")
    print(vs)
    print(f"Againt B: {against_b['name']}, {against_b['description']}, from {against_b['country']}")


def game():
    couninue_game = True
    score = 0
    while couninue_game is True:
        compare_a = data[score]
        against_b = data[score + 1]
        print_message(compare_a, against_b)
        user_answer = input("Who has more followers? Type 'A' or 'B': ")
        if user_answer == "A":
            if compare_a['follower_count'] > against_b['follower_count']:
                score += 1
                print(f"You're right! Current score: {score}.")
            else:
                print(f"Sorry, that's wrong. Final score: {score}.")
                couninue_game = False
        if user_answer == "B":
            if compare_a['follower_count'] < against_b['follower_count']:
                score += 1
                print(f"You're right! Current score: {score}.")
            else:
                print(f"Sorry, that's wrong. Final score: {score}.")
                couninue_game = False
        else:
            return "Opps!there is something wrong happend."


game()

# second version:bug is so much.horrible!T.T

from art import logo, vs
from game_data import data
import random
# from replit import clear


def print_message(compare_a, against_b):
    # print(logo)
    print(f"Compare A: {compare_a['name']}, {compare_a['description']}, from {compare_a['country']}")
    # print(vs)
    print(f"Againt B: {against_b['name']}, {against_b['description']}, from {against_b['country']}")


def check_answer(compare_a, against_b):
    if compare_a['follower_count'] > against_b['follower_count']:
        right_answer = "A"
    elif compare_a['follower_count'] < against_b['follower_count']:
        right_answer = "B"
    else:
        return
    return right_answer   

def data_choice():
   return random.choice(data)  

def game():
    score = 0
    continue_game = True
    compare_a = data_choice()
    against_b = data_choice()
    while compare_a == against_b:
        against_b = data_choice()
    print_message(compare_a, against_b)
    while continue_game is True:
        user_answer = input("Who has more followers? Type 'A' or 'B': ") 
        # clear()
        if user_answer == check_answer(compare_a, against_b):
            score += 1
            compare_a = against_b
            against_b = data_choice()
            while compare_a == against_b:
                against_b = data_choice()
            print(f"You're right! Current score: {score}.")
            print_message(compare_a, against_b)
        else:
            print(f"Sorry, that's wrong. Final score: {score}.")
            continue_game = False
            

game()





# answer version

from game_data import data
import random
from art import logo, vs
from replit import clear

def get_random_account():
  """Get data from random account"""
  return random.choice(data)

def format_data(account):
  """Format account into printable format: name, description and country"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  # print(f'{name}: {account["follower_count"]}')
  return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
  """Checks followers against user's guess 
  and returns True if they got it right.
  Or False if they got it wrong.""" 
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"


def game():
  print(logo)
  score = 0
  game_should_continue = True
  account_a = get_random_account()
  account_b = get_random_account()

  while game_should_continue:
    account_a = account_b
    account_b = get_random_account()

    while account_a == account_b:
      account_b = get_random_account()

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")
    
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    clear()
    print(logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")

game()




# sth like direction.

'''

FAQ: Why does choice B always become choice A in every round, even when A had more followers? 

Suppose you just started the game and you are comparing the followers of A - Instagram (364k) to B - Selena Gomez (174k). Instagram has more followers, so choice A is correct. However, the subsequent comparison should be between Selena Gomez (the new A) and someone else. The reason is that everything in our list has fewer followers than Instagram. If we were to keep Instagram as part of the comparison (as choice A) then Instagram would stay there for the rest of the game. This would be quite boring. By swapping choice B for A each round, we avoid a situation where the number of followers of choice A keeps going up over the course of the game. Hope that makes sense :-)

'''

# Generate a random account from the game data.

# Format account data into printable format.

# Ask user for a guess.

# Check if user is correct.
## Get follower count.
## If Statement

# Feedback.

# Score Keeping.

# Make game repeatable.

# Make B become the next A.

# Add art.

# Clear screen between rounds.
