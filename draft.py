
jack=11
queen=12
king=13
ace = int(input("1 or 11:"))
deck = [ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, jack, queen, king]

import random
def game():
    random.shuffle(deck)
    player_hand = random.random(deck)
