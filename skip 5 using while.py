#Write a Python program that skips printing the number 5 in a countdown from 10

num=10
while num>=0:      #using while because for loop it is already submitted
    if num==5:
        num-=1
        continue   
    print(num)
    num -= 1
