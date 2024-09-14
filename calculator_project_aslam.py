def add(a,b):
    return(a+b)
def subtract(a,b):
    return(a-b)
def multiply(a,b):
    return(a*b)
def divide(a,b):
    return(a/b)

calculator_operation={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calculator():
    number1=int(input("Enter the first number : "))
    for i in calculator_operation:
        print(i)
    again=True
    while again:
        operation=input("pick an operaion : ")
        number2=int(input("Enter the second number : "))
        actual_operation=calculator_operation[operation]
        result=actual_operation(number1,number2)
        print(f"{number1} {operation} {number2} = {result}")
        should_countionu=int(input(f"Enter 1 to calculate with {result} ,or 2 to start a new calculation , 3 to  exit "))
        if(should_countionu==1):
            number1=result
        elif(should_countionu==2):
            again=False
            calculator()
        else:
            print()
            print("BYE.......")
calculator()

            
        
 
    
    












        
    
