class student:
    def __init__(self,name1,name2):
        self.name1=name1
        self.name2=name2
    def details(self,course):
        print(f"my name is {self.name1} {self.name2} and i am staded in {course}")
stu=student("Aslam","Youseph")
stu.details("Bca")

