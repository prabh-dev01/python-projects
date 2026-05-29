import random

secret_number=random.randint(1,100)

print('welcome to the number guessing game ')

while True:
    try:
        guess=int(input('guess the number from 1 to 100    '))
 

        if guess>secret_number:
            print('too highh')
        elif guess<secret_number:
            print('too low')  
        else:
            print('congratulationss')
            print(f'the number was--{secret_number}') 
            break
    except ValueError:
        print('please enter a valid number ')   



   

     