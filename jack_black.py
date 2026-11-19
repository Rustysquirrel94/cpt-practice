import random
import math
import time

def hand_value(values):
    total = sum(values)
    aces = values.count(11)
    while total >21 and aces > 0:
        total -= 10
        aces -=1
    return total





deck = ["Ace of hearts", "2 of hearts", "3 of hearts","4 of hearts","5 of hearts", "6 of hearts", "7 of hearts", "8 of hearts", "9 of hearts", "10 of hearts","Jack of hearts", "Queen of hearts","King of hearts", "Ace of spades","2 of spades","3 of spades", "4 of spades","5 of spades","6 of spades","7 of spades","8 of spades","9 of spades","10 of spades", "Jack of spades", "Queen of spades", "King of spades", "Ace of clubs","2 of clubs","3 of clubs","4 of clubs", "5 of clubs","6 of clubs","7 of clubs","8 of clubs","9 of clubs","10 of clubs", "Jack of clubs", "Queen of clubs", "King of clubs", "Ace of diamonds", "2 of diamonds", "3 of diamonds", "4 of diamonds", "5 of diamonds", "6 of diamonds", "7 of diamonds", "8 of diamonds", "9 of diamonds", "10 of diamonds", "Jack of diamonds", "Queen of diamonds","King of diamonds"]
deck_values = [11, 2, 3, 4, 5, 6, 7, 8 , 9, 10, 10, 10,10,11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game_on = True

# def random_card():
#   num = random.randint(0,40)
#   ncard = deck[num]
#   return random_card

#   print(random_card())

# def drawplayercard(newcard):
#     while game_on == True:
#         if sum(player_hand) + newcard > 21:
#             game_on = False
#             return "game over, house wins"
#             print("game over, house wins")

# def drawhousecard(hnewcard):
#     while game_on == True:
#         if sum(house_hand) + hnewcard > 21:
#             game_on = False
#             return "game over, player wins"
#             print("game over, player wins")

# ace_card= []




# def ace_logic(acecard):
#   for card in acecard:
#     if card == "ace":
#       ace_card.append(card)
#       print(ace_card)
#   for ace in ace_card:
#     ace = int(input("1 or 11: "))
#     if ace == 1:
#       print("this ace is worth 1") 
#     elif ace == 11:
#       print("this ace is worth 11")


print("===================== JACK BLACK =====================")
preamble = input("Would you like to listen to the Preamble?\n If so please print YES: ").upper()
if preamble == "YES":
  print("This is a varation of the game 21, created by Caleb Loenser and Callen Priest.\nIt is designed as a quick-play blackjack simulator\n Aces are not featured in this version\n\n\n")
else:
  print(":p")
time.sleep(1)
#Round 1 logic
round_1 = True
while round_1 is True:
    num1 = random.randint(0,40)
    num2 = random.randint(0,40)
    card1= deck[num1]
    card2= deck[num2]
    player_value_card1= deck_values[num1]
    player_value_card2= deck_values[num2]
    player_hand =[card1,card2] 
    player_hand_digit= [player_value_card1,player_value_card2]
    player_hand_total = hand_value(player_hand_digit)
    num3 = random.randint(0,12)
    num4 = random.randint(0,12)
    card3 = deck[num3]
    card4 = deck[num4]
    house_hand=[card3,card4]
    value_card3 = deck_values[num3]
    value_card4= deck_values[num4]
    house_hand_digit = [value_card3,value_card4]
    house_hand_total= hand_value(house_hand_digit)
  
    print(f"The player hand is :{player_hand}\n The visible House hand is {card3}")
    time.sleep(1)
    if player_hand_total <= 21:
     print(f"Your hand is worth: {player_hand_total}.")
    else:
     print("Bust!")
     round_1 = False
    
    player_choice= input("Hit or Stand:").lower()

    if player_choice in ("hit","h"):
     new_num1 = random.randint(0,24)
     new_card = deck[new_num1]
     player_hand.append(new_card)
     value_new_card= deck_values[new_num1]
     player_hand_digit.append(value_new_card)
    
     time.sleep(1)
     print(f"You drew a {new_card}!\n Your new hand value is {hand_value(player_hand_digit)}")
     if hand_value(player_hand_digit) > 21:
        print("Bust!")
        print("You lost!")
        round_1 = False
     time.sleep(1)

    elif player_choice == "stand":
     print("You pass the turn to the House.")
    else:
     print("Player forfeit Turn") #Needs to be fixed
    house_hand_new_total = house_hand_total
    if  house_hand_total <= 16:
     new_house_rannum = random.randint(0,40)
     new_house_card = deck[new_house_rannum]
     new_house_digit =deck_values[new_house_rannum]
     house_hand_digit.append(new_house_digit)
     house_hand_new_total= hand_value(house_hand_digit)
     print(f"\n\n\n\nThe House drew a {new_house_card}\n The Houses new  known total is:{house_hand_new_total} ")
    if house_hand_new_total > 21:
        print("The House Busted!\n You Win!")
    elif house_hand_new_total <= hand_value(player_hand_digit):
        print("You have the higher hand!\n You Win!")
    elif house_hand_new_total >= hand_value(player_hand_digit):
        print("House has higher hand!\n You Lose!")
    
    player_repeat = input("  Type YES if you want to play again:").upper()
    if player_repeat == "YES":
      round_1 = True
    else:
      print("GOODBYE!")
      round_1= False
        
