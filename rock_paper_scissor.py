import random

print('welcome to rock paper scissor hope you will have fun')
choices=["rock","paper","scissor"]

computer_choice=random.choice(choices)

while True:

    player_choice=input('please choose rock,paper,scissor(R,P,S)').lower().strip()

    if player_choice==quit:
        print('have a nice day hope you had fun')
        break

    if player_choice  not in choices:
        print('please enter a valid input ')
        continue

    if player_choice=="rock"and computer_choice=="scissor" or \
       player_choice=="scissor" and computer_choice=="rock":
        print('you won')
        
        print('congratulations you won')
    
    



