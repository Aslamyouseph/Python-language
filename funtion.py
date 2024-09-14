import math
def paint():
    height=int(input("Enter the height of the wall : "))
    width=int(input("Enter the width of the wall : "))
    number=(height*width)/7
    result=(math.ceil(number))
    print(f"You need {result } bakket of paint ")
paint()
paint()
    
