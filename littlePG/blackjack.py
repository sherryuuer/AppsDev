############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt



import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
users = [random.choice(cards), random.choice(cards)]
computers = [random.choice(cards), random.choice(cards)]

print(f"your_cards:{users}, computer's cards:{computers[0]}.")

def check_score():
    user_score = sum(users)
    computer_score = sum(computers)

    if user_score == 21:
        print(f"your_cards:{users}, computer's cards:{computers[0]}.")
        print("You win!")
    elif computer_score == 21:
        print(f"your_cards:{users}, computer's cards:{computers}.")
        print("You lose!")
    elif user_score > 21:
        if 11 in users:
            if sum(users) - 10 > 21:
                print("You lose!")
            else:
                print("You have an 'A' as 1.")
                another_card()
        else:
            print("You lose!")
    else:
        another_card()

def another_card():
    draw_cards = input("Do you want another cards? Type 'y' or 'n': ")
    if draw_cards == 'y':
        users.append(random.choice(cards))
        print(f"your_cards:{users}, computer's cards:{computers[0]}.")
        check_score()
    else:
        computers.append(random.choice(cards))
        user_score = sum(users)
        computer_score = sum(computers)
        while computer_score < 17:
            computers.append(random.choice(cards))
            computer_score = sum(computers)
        if computer_score > 21:
            print(f"your_cards:{users}, computer's cards:{computers}.")
            print("You win!")
        else:
            if user_score > computer_score:
                print(f"your_cards:{users}, computer's cards:{computers}.")
                print("You win!")
            elif computer_score > user_score:
                print(f"your_cards:{users}, computer's cards:{computers}.")
                print("You lose.")
            else:
                print(f"your_cards:{users}, computer's cards:{computers}.")
                print("Draw.")

check_score()

#↑Did without the hits.
#↓Did with the hits.

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

import random
from art import logo

def deal_card():
    """
    Deal a new card and add it in to a list.
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] 
    card = random.choice(cards)
    return card

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)  
    return sum(cards)


#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It is a draw~~"
    elif computer_score == 0:
        return "Opponent is a blackjack, you lose.T.T"
    elif user_score == 0:
        return "You got a blackjack, you win!"
    elif user_score > 21:
        return "You got over 21, you lose..."
    elif computer_score > 21:
        return "Opponent got over 21, you win.ww"
    elif user_score > computer_score:
        return "You big you win."
    else:
        return "Unlucky, you lose....." 

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []
def play_game():
    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

    #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

    #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
    is_game_over = False

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    Your cards: {user_cards}, your current score: {user_score}.")
        print(f"    Computer's first card: {computer_cards[0]}.")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card,type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)



    print(f"    Your final hand: {user_cards}, your final score: {user_score}.")
    print(f"    Computer final hand: {computer_cards}, computer final score: {computer_score}.")    
    print(compare(user_score, computer_score))

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

while input("Do you want to play a game of Blackjack?Type 'y' or 'n': ") == 'y':
    print(logo)
    play_game()