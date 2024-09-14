# second  method of accesing the privet decleared values


class student:
    def __init__(self,name):
        self.__name=name;    #privet decleration of attributes
    def __display(self):    #privete deleration of methods 
        print(f"My name is {self.__name}") 


s=student("aslam")
print(dir())  # it is used to find the funtion that can be able to acces
s._student__display()   #  (name maniling)
print(s._student__name) 
