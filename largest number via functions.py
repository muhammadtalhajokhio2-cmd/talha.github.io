num1=int(input("Enter any number1:"))
num2=int(input("Enter any number2:"))
num3=int(input("Enter any number3:"))
def large(a,b,c):
    if(a >= b and a >= c):
        print("The largest number is:",num1)
    elif(b >= c ):
        print("The largest number is:",num2)
    else:
        print("The largest number is:",num3)
large(num1,num2,num3)
