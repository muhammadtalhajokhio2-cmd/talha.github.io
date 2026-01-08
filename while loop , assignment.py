#Write a python code USING WHILE LOOP to modify the countdown
#timer to break the loop if the number goes below 5

num=int(input('enter a number='))
while num>=0:
    print(num)
    num-=1
    if num<5:
        print('loop is ended')
        break
    
