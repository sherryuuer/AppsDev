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
