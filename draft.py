import random
import math

deck = ["ace", 2, 3, 4, 5, 6, 7, 8 , 9, 10, "jack", "queen","king", "ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king", "ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king", "ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king"]
deck_values = ["ace_logic", 2, 3, 4, 5, 6, 7, 8 , 9, 10, 10, 10,10,"ace_logic", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, "ace_logic", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, "ace_logic", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game_on = True

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

# def ace_logic(acecard):
#     if acecard == "ace":
#         acecard = int(input("1 or 11: "))
#         if acecard == 1:
#             return 1
#             print("this ace is worth 1")
#         elif acecard == 11:
#             return 11
#             print("this ace is worth 11")
#     else:
        

        
#Round 1 logic
round_1 = True
while round_1 is True:
    num1 = random.randint(0,12)
    num2 = random.randint(1,12)
    card1= deck[num1]
    card2= deck[num2]
    player_value_card1= deck_values[num1]
    player_value_card2= deck_values[num2]
    player_hand =[card1,card2] 
    player_hand_digit= [player_value_card1,player_value_card2]
    player_hand_total = sum(player_hand_digit)
    num3 = random.randint(0,12)
    num4 = random.randint(0,12)
    card3 = deck[num3]
    card4 = deck[num4]
    house_hand=[card3,card4]
    value_card3 = deck_values[num3]
    value_card4= deck_values[num4]
    house_hand_digit = [value_card3,value_card4]
    house_hand_total= sum(house_hand_digit)
    # ace_logic(card1)
    # ace_logic(card2)
    # ace_logic(card3)
    # ace_logic(card4)
    print(f"The player hand is :{player_hand}\n The visible House hand is {card3}")
    round_1 =False


# Player turn
player_turn1 = True
while player_turn1 == True:
    if player_hand_total <= 21:
     print(f"Your hand is worth{player_hand_total}.")
    else:
     print("Bust!")
    
    player_choice= input("Hit or Stand:").lower()

    if player_choice == "hit":
     new_num1 = random.randint(0,13)
     new_card = deck[new_num1]
     player_hand.append(new_card)
     value_new_card= deck_values[new_num1]
     player_hand_digit.append(value_new_card)
     player_hand_1_total = sum(player_hand_digit)
     
     # ace_logic(new_card)
     print(f"You drew a {new_card}!\n Your new hand value is {player_hand_1_total}")
     if player_hand_1_total > 21:
        print("Bust!") 
        break
    elif player_choice == "stand":
     print("You pass the turn to the House.")
    break 
else:
  print("error") #Needs to be fixed



house_turn1 = True
while house_turn1 == True:  
    while house_hand_total <= 16:
     new_house_rannum = random.randint(0,40)
     new_house_card = deck[new_house_rannum]
     new_house_digit =deck_values[new_house_rannum]
     new_house_card_value= deck_values[new_house_rannum]
     house_hand.append(new_house_card)
     house_hand_new_total= sum(new_house_digit)
     print(f"The House drew a {new_house_card}\n The Houses new  known total is:{house_hand_new_total} ")
     