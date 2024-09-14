def result(year1,month1):
    flage=0
    if(year1%4==0):
        if(year1%100==0):
            if(year1%400==0):
                flage=True
            else:
                flage=False
        else:
            flage=True
    else:
        flage=False
    if(flage==True and month1==2):
        print("You select februvary and it has 29 days (it is a leap year) ")
    elif(flage==False and month1==1):
        print("You select januvary and it has 31 days ")
    elif(flage==False and month1==2):
        print("You select februvary and it has 28 days ")
    elif(flage==False and month1==3):
        print("You select march and it has 31 days ")
    elif(flage==False and month1==4):
        print("You select April and it has 30 days ")
    elif(flage==False and month1==5):
        print("You select May and it has 31 days ")
    elif(flage==False and month1==6):
        print("You select june and it has 30 days ")
    elif(flage==False and month1==7):
        print("You select June and it has 31 days ")
    elif(flage==False and month1==8):
        print("You select Agust and it has 30 days ")
    elif(flage==False and month1==9):
        print("You select September and it has 31 days ")
    elif(flage==False and month1==10):
        print("You select october and it has 31 days ")
    elif(flage==False and month1==11):
        print("You select november and it has 30 days ")
    elif(flage==False and month1==12):
        print("You select december and it has 31 days ")
    else:
        print("Invalid enter" )
        print()
limit=int(input("Enter the limit of numbers you want : "))
for i in range(0,limit):
    year=int(input("Enter the year : "))
    print()
    print("1=januvary ")
    print("2=februvary")
    print("3=march")
    print("4=april")
    print("5=may")
    print("6=june")
    print("7=julay")
    print("8=aguste")
    print("9=september")
    print("10=october")
    print("11=november")
    print("12=december")
    print()
    month=int(input("Enter the month : "))
    result(year,month)
 
 
 
 
  
 
 
 
 
 
  
 
 
 
 
 
