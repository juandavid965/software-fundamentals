#game 2 

import os
from random import randint
lives = 3 
status = True
tiros = 0 

def roll_dice():
    dad1 = randint(1,6)
    dad2 = randint(1,6)
    return dad1 , dad2
##########
#print (roll_dice())
while True: 
    key = input("press any key to roll dices:")
    tiros += 1
    dices = roll_dice() 
    print(f"dice 1: {dices[0]}")
    print(f"dice 2: {dices[1]}")
    if (dices [0] + dices [1]) % 2 == 0:
        lives += 1 
    else:
        lives -= 1 
        print (f"tus vidas son", lives)

    if dices [0] == 6 and dices [1] == 6:
        print("you won the roll", tiros,(":)"))
        break
    if lives == 0:
        print("you lose the roll",tiros,(":("))
        break        