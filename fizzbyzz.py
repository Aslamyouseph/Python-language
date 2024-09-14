limit=int(input("Enter the limit : "))
for i in range(1,limit+1):
    if(i%3==0 and i%5==0):
        print("FizzByzz")
    elif(i%3==0):
        print("Fizz")
    elif(i%5==0):
        print("Byzz")
    else:
        print(i)
       
