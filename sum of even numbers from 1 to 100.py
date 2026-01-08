#Write a Python program that calculates the sum of all even numbers
#from 1 to 100.


sum_of_even = 0
for num in range(1, 101): 
    if num % 2 == 0:       
        sum_of_even += num    
print("Sum of all even numbers from 1 to 100 is:", sum_of_even)
