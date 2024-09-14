class father():
    def __init(self):
        self.eye=2
        self.nose=2
    def addres(self):
        print("Thelyil")
    def colour(self):
        print("White")
    def name1(self):
        print("my ame is youseph ")
            

class son(father):
    def name(self):
        super().name1()
        print("My name is Aslam ")

son1=son()
son1.addres()
son1.colour()
son1.name()
