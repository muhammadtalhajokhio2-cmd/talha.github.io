#Create a simple calculator that can add, subtract, multiply, and divide
#two numbers based on the user’s choice.
#The calculator should keep asking for new operations until
#the user decides to quit by entering 'q'.  

while True:
    operation=input("enter the operation(+,-,*,/)or 'q' to quit:")
    if operation =='q':
        print('calculator closed')
        break
    a=float(input('enter first number='))
    b=float(input('enterk second number='))
    if operation=='+':
        print('result=',a+b)
    elif operation=='-':
            print('result=',a-b)
    elif operation=='*':
                print ('result=',a*b)
    elif operation=='/':
                    if b==0:
                        print("Error: Cannot divide by zero!")
                    else:
                        print('result=',a/b)
    else:
        print("Invalid operation! Please try again.")
                
