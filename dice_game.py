#dice roll game

import random

while True:
   choice=input('please roll the dice (y/n)').lower()
   if choice=='y':
      dice1=random.randint(1,6)
      dice2=random.randint(1,6)
      print(f'{dice1},{dice2}')
       
   elif choice=='n':
      print('thanks for playing')
      break
   else:
      print('invalid choice')
