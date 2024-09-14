flage=False
number=int(input("Enter the number : "))
for i in range(2,number):
    if(number%i==0):
        flage=True
        break
if(flage==True):
    print("It is not a prime number  ")
else:
    print("It is  a prime number ")
    
