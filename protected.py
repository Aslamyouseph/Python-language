class student:
    def __init__(self,name1):
        self._name=name1;   #declear as protect 
    def display(self):
        print(f"My name is {self._name}") #to display give ( _ ) to name 
class student1(student):
    pass;


s=student1("aslam")
print(s._name)   #calliing  the protected 
s.display()
