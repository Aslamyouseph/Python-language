class complex:
    def __init__(self,r,i):
        self.real=r
        self.imaginary=i
    def __add__(self,other): #operator overloading section (self contain real part of c1 ,other conatin real part of c2 )
        print("The out put of complex number is ") #self contain imaginary of c1 and other contain imaginary of c2
        return (f"{self.real + other.real}{self.imaginary + other.imaginary }i")

c1=complex(1,6)
c2=complex(3,2)
print(c1+c2)  #(call line number 7 = operator overloading )(act like a funtion call)
