import random
number =random.randint(1,100)
print('i have slected a number between 1 and 100.can you guess it')
i=1
while i<=3:
    i+=1
    guess=int(input('enter your guess:'))
    if guess < number:
        print('too low!Try again')
    elif guess > number:
        print('too high!Try again')
    else:
        print('congrats your guess is correct')
        break
if (number != guess ):
    print ("your attempts are ended the correct number was :",number)
