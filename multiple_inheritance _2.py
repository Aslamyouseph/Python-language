class father:
    def __init__(self,age1):
        self.age=age1
    def name(self,name):
        print(f"Father name is {name}")



class mother:
    def __init__(self,place1):
        self.place=place1
    def name(self,name):
        print(f"mother name is {name}")
        



class student(father,mother):
    def __init__(self,country1,place1,age1):
        mother. __init__(self,place1)
        self.country=country1


stu=student("indiaa","Nellimattom",54)
print(stu.place)
#stu.name("Youseph")
#father.name(stu)

