limit=int(input("Enter the limit "))
for i in range(1,limit):
    if(i%2==0):
        print(i)
else:
    print("This are the even numbers")

#This is the for else
    # the else block is not work when we force fully exit from the loop
    # force fully means (break also include )
    #when we use break the else block is not work
