# one method of accesing the privet decleared values


class student:
    def __init__(self,name):
        self.__name=name;    #privet decleration of attributes
    def __display1(self):    #privete deleration of methods 
        print(f"MY name is {self.__name} ")
    def display3(self):  #privetly declered is defined inside in a public section to access the values 
        self.__display1()  #call the privet section 

class student1(student):
    def display2(self):
        print(f"It is not possible to call privet in here ")


s=student1("aslam")
s.display3()
s.display2()
