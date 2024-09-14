def hello(name):
    print("We are in the hello block ")
    def funtion_1():
        print("Aslam youseph ")
    def funtion_2():
        print("Afnitha youseph ")

    if(name=="appu"):
        return funtion_1
    else:
        return funtion_2
    

returning_value=hello("appu")  # when hello calls the cntrol goes to the 1 line ,and also in here the returning funtion is stored in a varible
returning_value() # then call the varible name for accesing the particular funtion 
print("\n")
returning_value=hello("anu")
returning_value()