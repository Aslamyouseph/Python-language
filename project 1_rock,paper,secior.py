print("ROCK PAPER SCECORES")
print("1 = rock ")
print("2 = paper ")
print("3 = scesiors ")
import random
for i in range(1,11):
    print()
    select=float(input("Enter user choice : "))
    number=[1,2,3]
    result=random.choice(number)
    print(f"computer selcet {result}")
    print()
    if(select==1 and result==1):
        print("Draw")
    elif(select==1 and result==2):
        print("computer is win ")
    elif(select==1 and result==3):
        print("user is win ")

    elif(select==2 and result==1):
        print("use is win ")
    elif(select==2 and result==2):
        print("Draw")
    elif(select==2 and result==3):
        print("computer is win ")
    elif(select==3 and result==1):
        print("computer is win ")
    elif(select==3 and result==2):
        print("user is win ")
    elif(select==3 and result==3):
        print("Draw")
    else:
        print("Invalid entry")
  
#THIS IS ROCK PAPER SCEASORS PROGRAM
