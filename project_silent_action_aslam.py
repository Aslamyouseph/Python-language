print("        silent action program ")
import os
again=True
higest=0
winner=""
result={}
while again:
    name=input("Enter the name : ")
    amount=int(input("Enter the bid amound : "))
    result[name]=amount
    more=int(input("Are there any another bidders , 1=yes , 2=no"))
    if(more==2):
        again=False
        for i in result:   
            actual_result=result[i]   #abstract  the value  from the dictionary  
            if(actual_result>higest):   #comparing the values and assingnig itt 
                higest=actual_result   #if it is large the  interchanging he values 
                winner=i
        print(f"The full list is {result}")
        print(f"The winner is {winner} with {higest} bid")
    else:
        os.system("clr")
        
            
        
        
