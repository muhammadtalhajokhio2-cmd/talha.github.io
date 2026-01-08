import random
number =random.randint(1,100)
print('i have slected a number between 1 and 100.can you guess it')
while True:
    guess=int(input('enter your guess:'))
    if guess<number:
        print('too low!Try again')
    elif guess>number:
        print('too high!Try again')
    else:
        print('congrats your guess is correct')
        break
