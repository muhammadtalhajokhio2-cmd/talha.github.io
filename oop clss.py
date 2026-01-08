class student:
    Name=input('Enter your name=')
    Age=int(input('Enter your age='))
    def introduce(self):
        print('Hello',self.Name,self.Age)
ob=student()
ob.introduce()
