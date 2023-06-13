from replit import clear
from art import logo
print(logo)
bidding_dic={}


should_continue=True
while should_continue==True:
  name=input("What is your name?: ")
  amount=int(input("What's your bid?: $"))
  bidding_dic[name]=amount
  go_on=input("Are there any other bidder? Type 'yes' or 'no'.\n")
  clear()
  if go_on=='no':
    should_continue=False

highest=0
for x in bidding_dic:
  if bidding_dic[x] > highest:
    highest=bidding_dic[x]
    name=x

print(f"The winner is {name} with a bid of ${highest}.")