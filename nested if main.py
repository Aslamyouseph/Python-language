name=input("enter the name of ")
height=int(input("enter the height "))
bill=0
if(height>=3):
    age=int(input("enter the age "))
    if(age>=12):
      print("you have able to ride ,and you want pay 150")
      bill=10
    elif(age>=18):
        print("you have able to ride ,and yopu want to pay 300")
        bill=300
    elif(age>=30):
        print("you have able to ride , and you wand to pay 500")
        bill=500
    else:
        print("sorry you cannot able to ride , see you soon ")

    photo=input("Do you wand to take photos (yes or no )")
    if(photo==1):
        bill=bill+50
        print(f"Now your amound is {bill} ")
else:
    print("sorry you cannot able to ride , see you soon ")
