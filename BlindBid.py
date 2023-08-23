from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)
print("Welcome to the secret ouction program.")

other_exsits = True
biders = {}

while other_exsits:
    name = input("What is your name? ")
    bid = float(input("What's your bid? $"))
    other = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    if other == 'no':
        other_exsits = False
    else:
        clear()
    biders[name] = bid

clear()
max_name, max_bid = max(bidders.items())
print(f"The winner is {max_name} with a bid of ${max_bid}.")


# or create a function to get the max value.as the answer told us.
def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")


