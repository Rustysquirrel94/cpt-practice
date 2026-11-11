import random
import math
jack=11
queen=12
king=13
ace = int(input("1 or 11:"))
deck = [ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, jack, queen, king]
game_on = True

def drawplayercard(newcard):
    while game_on == True:
        if sum(player_hand) + newcard > 21:
            game_on = False
            print("game over")

def drawhousecard(hnewcard):
    while game_on == True:
        if sum(house_hand) + hnewcard > 21:
            game_on = False
            print("game over")


        


while game_on is True:
    num1 = random.randint()
    num2 = random.randint()
    card1= deck[num1]
    card2= deck[num2]
    player_hand =[card1,card2] 