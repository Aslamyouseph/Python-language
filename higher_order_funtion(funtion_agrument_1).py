def greet():
    print("hi")

def display(other_display_funtion): # "other_display_funtion" is accept the funtion is an agrument (but in here its didnot call the greet funtion ) the funtion is stored in the other_display_funtion argunet 
    print("We are in the display () funtion ")
    other_display_funtion() # if we want to call the greet funtion then the greet stored varible is call like a funtion , then he control will goes to the the line 1 and it start the exectution of the greet funtion 
    
display(greet)   # when we call display the needed funtion is pass as an argument without '()' this bracket 

