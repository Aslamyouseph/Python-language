name=input("Enter the names: ")
import random
result_name=name.split(",")
for i in range(1,5):
    result_ran=random.choices(result_name)
    print(result_ran)
    name=input("Enter the names: ")
    

#this program is desingned to ask the user to input the name for 5 times
