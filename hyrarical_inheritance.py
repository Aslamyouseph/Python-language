class human:

    def eat(self):
        print("I can eat ")

class male(human):
    def __init___(self,name2):
        self.name=name2
    def run(self):
        print("I can run ")

class female(human):
    def __init__(self,name3):
        #def __init__(self,name2):
           # male .__init__(self,name2)
        
        self.name=name3
    def sleep(self):
        print("i an sleep ")


f=female("Afnitha")
f.eat()
f.sleep()
print()
m=male("Aslam")
#m.eat()
#m.run()
print(m.name)
