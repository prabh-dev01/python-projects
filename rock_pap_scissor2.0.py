import random

choice = ['r','p','s']
emojis = {'r':'🪨','p':'📃','s':'✂️'}



print('welcome to the rock paper scissor game hope you will have fun')

def get_user_choice():
    while True:
        
     player_choice=input('please choose your input (r,p,s)')
    

     if player_choice  in choice:
        return player_choice
     else:
        print('please enter a valid choice')

def display_choices():
    print(f'you chose {emojis[player_choice]}')
    print(f'you chose {emojis[computer_choice]}')
def winner_decider():
   

   
   


      

player_score=0
computuer_score=0

while True:
   player_choice= get_user_choice()
   
    

   computer_choice=random.choice(choice)

   display_choices()


   should_continue= input('you want to continue(y,n)') 
   if should_continue=='n':
        print('thanks for playing hope you had fun')
        break 
    

