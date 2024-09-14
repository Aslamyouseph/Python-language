class circle:
    def __init__(self,radious1):
        self.radious=radious1
    def circum(self):
        circums=2*3.14*radious
        print(f"The circumfrance of the circle is {circums}") 
    def area(self):
        area=3.14*radious*radious
        print(f"The radious of the circle is {area} ")
        
        
radious=int(input("Enter the radious of the circle : "))

cir=circle(radious)
cir.circum()
cir.area()
