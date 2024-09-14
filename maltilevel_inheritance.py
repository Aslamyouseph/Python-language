class grand_father():
    def __init__(self,place1):
        self.place=place1
    def name1(self,name):
        print(f"I am grandfather {name} ")

class father(grand_father):
    def __init__(self,age1):
        self.age=age1
    def name2(self,name):
        print(f"I am father {name} ")

class son(father):
    def __init__(self,place,age,classs1):
        father.__init__(self,age)
        grand_father.__init__(self,place)
        self.classs=classs1
    def name3(self,name):
        super().name2("Youseph")
        print(f"I am son {name}")
        
s=son("Nellimattom",20,"bca")
print(s.age)
print(s.place)
print(s.classs)
#s.name1("Meran")        
#s.name2("Youseph")
#s.name3("Aslam")


