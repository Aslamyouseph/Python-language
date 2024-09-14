print("  PIZZA ODERING  ")
print(" ENTER WHICH TYPE OF PIZZA YOU WANT ")
print("small_pizza = 100 rupees : ")
print("medium_pizza = 200 rupees : ")
print("lare_pizza = 300 rupees : ")
size=input("which pizza do you want : ")
bill=0
small_pizza=0
medium_pizza=0
large_pizza=0
if(size == small_pizza):
    print("you odder small pizza ")
    bill=bill+100
    print("you want to pay {bill}")
elif(size == medium_pizza):
    print("you oder medium pizza ")
    bill=bill+200
elif(size == large_pizza):
    print("you oder large pizza ")
    bill=bill+300
else:
    print("invalid entry , please chooes correct option ")
    
    
    

   
    
