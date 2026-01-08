#Write a Python program that counts down from 10 to 1.
#Modify the countdown timer to break the loop if the number goes below 5.


for i in range(10,0,-1):
    if i<5:
       break
    print (i)
print("countdown stopped before liftoff!")
