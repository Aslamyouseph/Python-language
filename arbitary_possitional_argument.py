#it is mainly used the situation where the programer not know the user pass howmany arguments 
def number(*arg):# able to store large number of arguments 
    total=0
    for i in arg:
        total=total+i
    print(f" sum of number is {total}")

number(1,2)
number(1,2,3)
number(1,2,3,4,5)
number(1,2,3,4,5,6)
