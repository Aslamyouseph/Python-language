def prim():
    result=true
    number=int(input("Enter the  number : "))
    for i in range(2,number):
        if(number%i==0):
            result=false
            break
        if(result==true):
            print("it is a prime number ")
        else:
            print("it is not a prime number ")
prim()
