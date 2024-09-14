class number():
    def __init__(self,num1,num2,name1): #name1 is used to collect the name 
        self.num1=num1
        self.num2=num2
        self.name=name1   #assing the value
    def addition(self):
        add=self.num1+self.num2
        print(f"Addition of two numbers is {add}")
    def subtraction(self):
        sub=self.num1-self.num2
        print(f"subtraction of two numbers is {sub}")
    def multiplication(self):
        mul=self.num1*self.num2
        print(f"multiplication  of two numbers is {mul}")
    def divition(self):
        div=self.num1/self.num2
        print(f"divition of two number is {div}")

        
        
class operation(number):      
    def __inti__(self,name):    #in here we create a argument (name) to get the value from base class
        super().__init__(name)     # give same arument as the above one

        
op=operation(8,2,"Aslam")  #pass aslam as an argument to base class 
op.addition()
op.subtraction()
op.multiplication()
op.divition()
print(op.name)
