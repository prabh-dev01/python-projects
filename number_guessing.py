import random

secret_number=random.randint(1,100)

print('welcome to the number geussing game!!')
print('lets beginn')

while True:
    guess=int(input('please guess the number'))

    if guess>secret_number:
        print('too high ')
    elif guess<secret_number:
        print('too low') 

    else:
        print(f'conrgatulations you guessed it correctly the number was{secret_number}')
        break
    