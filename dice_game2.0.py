#two player dice game

import random

def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)
    
rounds_played=0 

while True: 
    choice = input("Please roll the dice (y/n): ").lower().strip()

    if choice == "y":
        rounds_played+=1
        # Player 1 rolls
        player1_dice1, player1_dice2 = roll_dice()
        player1_total = player1_dice1 + player1_dice2
        print(f"Player 1 rolls {player1_dice1}, {player1_dice2} → Total = {player1_total}")

        # Player 2 rolls
        player2_dice1, player2_dice2 = roll_dice()
        player2_total = player2_dice1 + player2_dice2
        print(f"Player 2 rolls {player2_dice1}, {player2_dice2} → Total = {player2_total}")

        # Compare the results
        if player1_total > player2_total:
            print("Player 1 wins")
        elif player1_total < player2_total:
            print("Player 2 wins")
        else:
            print("Match tied")

        print(f'rounds played so far--{rounds_played}')

    

    elif choice=='n':
        print(f'game over hope you had fun!!! total rounds played={rounds_played}')
        break 
    else:
        print('invalid choice please enter y or n ')      
        





    

