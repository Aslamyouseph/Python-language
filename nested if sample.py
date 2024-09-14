height=input("enter the height of the student ")
if(height>3):
  bill=0  
age=input("enter the age of the student ")
photo=input("Do you want to take photos - yes or no ")
 if(age<18):
     print("ticket priceis 150")
     bill=150
 elif(age>=18):
       print("ticket price is 300")
       bill=300
 else:
     print("ticket price is 500")
     bill=500
 if(photo == yes ):
    print(f"your amound is {bill+50}")
 if(photo == no):
    print(f"your amound is {bill}")
else:
    print("you can't ride ")
    print("sorry  see you soon  ")
