class father:
    def __init__(self,age):
        self.age=age
    def name1(self):    #1
        print("Father name is youseph   ")
    

class mother:
    def __init__(self,place):
        self.place=place
    def name1(self):       #1
        print("MOthher name is Aseena ")
    


class son(mother,father):             #1
    def __init__(self,age,place, ):     #3
     mother.__init__(self,place)   
    def mark(self,mark):
        print(f"i have{mark}")


s=son(25,"nellimattom")
s.name1()
print(s.place)
s.mark(50)
mother.name1(s)     #2
