class student:
    def __init__(self,m1,m2,m3):
        self.mark1=m1
        self.mark2=m2
        self.mark3=m3
    def name(self):
        print("My name is aslam")
    def rno(self,rno):
        print(f"MY roll_numbe is {rno}")
    def course(self,course):
        print(f"I am studed in {course}")

class mark(student):
    def marks(self):
        total=self.mark1+self.mark2+self.mark3
        print(f"my total mark is {total}")
    def age(self,age):
        print(f"I have {age} years old")
    def work(self):
        super().name()
        print("I can able to work")

        
mark1=mark(56,58,57)
mark1.name()
mark1.rno(23)
mark1.course("Bca")
mark1.marks()
mark1.age(20)
mark1.work()

