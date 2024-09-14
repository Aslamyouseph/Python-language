print("PIZZA ODERING PROGRAM ")
print()
print("1:small pizza=100$")
print("2:Medium pizza=200$")
print("3:Large pizza=300")
print()
bill1=100
bill2=200
bill3=300
choice=int(input("Enter your choise "))
print()
if(choice==1):
    print(f"You select small pizza,you want to pay {bill1}")
elif(choice==2):
    print(f"You select medium pizza,you want to pay {bill2}")
elif(choice==3):
    print(f"You select large pizza,you want to pay {bill3}")
else:
    print("Invalid entry")
print()
print("1:Pepperoni for small pizza = extra pay 30$")
print("2:Pepperoni for medium pizza = extra pay 50$ ")
print("3:pepperoni for large pizza = extra pay 50$")
print("4:No need any kind of additional things ")
print()
final=int(input("Enter your choice "))
print()
if(final==1):
    amount1=bill1+30
    print(f"You select peperoni for small pizza,you want to pay {amount1}")
elif(final==2):
    amount2=bill2+50
    print(f"You select pepperoni for medium pizza,you wnat to pay{amount2}")
elif(final==3):
    amount3=bill3+50
    print(f"You select pepperoni for large pizza,you want to pay {amount3}")
elif(final==4):
    print("Not need additional thinks")
else:
    print("Invalid entry")
print()
print("1=yes//2=no::Extra chees for any pizza = extra pay 20$")
print()
extra=int(input("Enter your choice "))
print()
if(final==1 and extra==1  ):
    print(f"Final amamount = {bill1+30+20}")
elif(final==2 and extra==1  ):
    print(f"Finl amamount = {bill2+50+20}")
elif(final==3 and extra==1 ):
    print(f"Finl amamount = {bill3+50+20}")
elif(extra==2):
    print(f"You not select any extra chees ")
else:
    print("Invalid entry ")
print("THANK YOU HAVE A NICE DAY")





















