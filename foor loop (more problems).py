number=int(input("Enter the number  "))
flage == 0
for i in range(2,100):
    if number%i==0:
        flage=1
        break;
if flage==0:
     print("The  number is  prime")
else:
    print("The number is not prime")
