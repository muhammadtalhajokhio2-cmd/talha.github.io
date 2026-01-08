i=1
while i<=3:
    
    pin =int(input('enter your pin='))
    if(pin==2040):
        print('your put correct pin')
        print ("wellcome Talha")
        break
    else:
        print('wrong pin')
    i+=1
if (pin!=2040):
    print ("attempts are over try again after 30 seconds")
        

