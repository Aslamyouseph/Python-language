class employee:
    def __init__(self,name,addres):
        self.name=name
        self.addres=addres
    def display(self,age):    #in here the member funtion decleare
        age1=age
        print(f"my name is {self.name} and i am comming from {self.addres} and i have {age1} years old ")

emp=employee("Aslam","Nellimattom")
print(emp.name)
print(emp.addres)
emp.display(21)    #in here he mebber funtion i s called



        
        
