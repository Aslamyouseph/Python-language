def add(a,b):
    return(a+b)
def subtract(a,b):
    return(a-b)
def multiply(a,b):
    return(a*b)              #This is funtion section 
def divide(a,b):
    return(a/b)
operations_dict={
    "+":add,
    "-":subtract,
    "*":multiply,   #This is the dicctionnay section( + IS THE KEY AND ADD IS THE VALUES ) 
    "/":divide
}
def caculator():
    number1=int(input("Enter the first number : "))
    for i in operations_dict:  #THIS SECTION IS USED TO TAKE  THE VALUES FROM ABOVE DICTIONARY 
        print(i)
    countionu_flage=True
    while countionu_flage:
        op_symbol=input("pick an operation : ")
        number2=int(input("Enter the second number : "))
        calculator_funtion=operations_dict[op_symbol] #IN HERE WE ASSINNG TO THE VARIBLE WICH OPERATIONN IS CHOICE BY THE USER 
        output=calculator_funtion(number1,number2)  #IN HERE CALCULATOR_FUNTION IS CONSIDER AS THE FUNTION CALL (IN THE ABOVE SENTENCE CALCULATOR FUNTION HAVE THE VALUES THAT USER ENTERD ) add(number1,number42)
        print(f"{number1} {op_symbol} {number2} = {output}") 
        should_countionu=input(f"Enter y to calculate with {output} ,or n to start a new calculation , x to  exit ").lower()
        if should_countionu == "y":
            number1=output
        elif should_countionu == "n":
            countionu_flage=False
            caculator()         #THIS IS THE RECURTION  SECTION 
        else:
            countionu_flage=False
            print("Bye......... ")
caculator()
   #THIS IS THE RECURTION SECTION 
   
        
    
    
