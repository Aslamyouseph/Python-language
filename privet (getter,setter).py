class student:
    def __init__(self,age):
        self.__age=age

    def get_age(self):   # (getter) this block for accessing the privet data 
        return self.__age

    def set_age(self,age):   # (setter)  it is used to modefing the prvet dicleared data
        if(age < 19):
            print("You would note able to vote ")

        else:
            self.__age=age  #modefing the privet data 


s=student(23)
print(s.get_age())  # accesing the privet data
s.set_age(25)  # modefing the privet data 
print(s.get_age())  #accesing the modefing datat 
