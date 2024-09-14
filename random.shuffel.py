name=input("Enter the names : ")
import random
result=name.split(",")
c=1
while(c<=10):
    random.shuffle(result)
    print(f"now {result[0]} want's to pay ")
    c+=1
