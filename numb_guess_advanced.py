import random

secret_number=random.randint(1,100)

print('welcome to the number guessing game ')

while True:
    try:
        guess=int(input('guess the number from 1 to 100    '))
        difference=abs(guess-secret_number)
 

        if guess==secret_number:
            print('congratulations you won')
            print(f'the number was--{secret_number}') 
            break
        elif difference<=3:
            print('very close')
        elif difference<=10:
            print('close')       
     
        elif guess<secret_number:
            print('too low')  
        else:
            print('too high')
            
            
        
    except ValueError:
        print('please enter a valid number ')   

