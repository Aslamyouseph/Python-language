print("      COFFIE MECHAINE ")

water=1000
milk=1000
coffe_powder=100

def lattel():
    if(water < 100 and milk < 100 and coffe_powder < 10):
        print("Sorry not enough increadeance are avilable ")
    else:
        amount=100
        given_amount=orginal_five+orginal_ten+orginal_twenty
        if(given_amount > amount):
            balance=given_amount-amount
            print("Here is your lattel ")
            print(f"you have {balance} balance ")
            return amount
        elif(given_amount < amount):
            print("You have not safficent money ")
            print("sorry !")
        
def espessy():
    if(water < 200 and milk < 200 and coffe_powder < 20):
        print("Sorry not enough increadeance are avilable ")
    else: 
       amount=200
       given_amount=orginal_five+orginal_ten+orginal_twenty
       if(given_amount > amount):
           balance=given_amount-amount
           print("Here is your espessy ")
           print(f"you have {balance} balance ")
           return amount
       elif(given_amount < amount):
           print("You have not safficent money ")
           print("Sorry ! ")
        
def cappichino():
    if(water < 300 and milk < 300 and coffe_powder < 30):
        print("Sorry not enough increadeance are avilable ")
    else:
        amount=300
        given_amount=orginal_five+orginal_ten+orginal_twenty
        if(given_amount > amount):
            balance=given_amount-amount
            print("Here is your cappichino ")
            print(f"you have {balance} balance ")
            return amount
        elif(given_amount < amount):
            print("You have not safficent money ")
            print("Sorry !")
            
def report():
    print(f"water: {water} ml")
    print(f"milk: {milk} ml")
    print(f"coffe_powder: {coffe_powder} gm")
    print(f"Total amount : {final_amount}")

again=True
while again:
    choice=input("What would like to have (lattel/espessy/cappichino)  : ").lower()

    if(choice=="report"):
        report()
        continue
    print("Pleas enter the coins ")
    five=int(input("Enter hou much 5 ruppes coins : "))
    ten=int(input("Ente how much 10 ruppes coins :  "))
    twenty=int(input("Enter how much  20 ruppes coins : "))

    orginal_five=5*five
    orginal_ten=10*ten
    orginal_twenty=20*twenty

    if(choice=="lattel"):
        orginal_amount=lattel()
        water=water-100
        milk=milk-100
        coffe_powder=coffe_powder-10
    final_amount=0
    final_amount=final_amount+orginal_amount
    if(choice=="espessy"):
        orginal_amount=espessy()
        water=water-200
        milk=milk-200
        coffe_powder=coffe_powder-20
    final_amount=0
    final_amount=final_amount+orginal_amount
    if(choice=="cappichino"):
        orginal_amount=cappichino()
        water=water-300
        milk=milk-300
        coffe_powder=coffe_powder-30
    final_amount=0
    final_amount=final_amount+orginal_amount
    if(choice=="off"):
        again=False

    
    
    


















