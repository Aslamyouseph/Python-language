eassy_attempt=10
import random
result=random.randint(1,50)      #IN HERE WE USE THE RANDIN FUNTION IT IS USED TO TAKE THE NUMBER UPTO A LIMIT 
print("           GUESS THE NUMBER : ")
print("LET ME THING OF THE NUMBER BETWEEN 1 TO 50 : ")
choice=input("Choose the level of difficulty type : HARD / EASSY : ").lower()
#print(result)
print()
if(choice=="eassy"):
    for i in range(0,9):
        eassy_attempt=eassy_attempt-1
        print()
        guess=int(input("Guess the number : "))
        if(guess > result):
            print("Your guess is too long ")
            print(f"you have only {eassy_attempt} attempt only ")
            print()
        elif(guess < result):
            print("Your guess is too short ")
            print(f"you have only {eassy_attempt} attempt only ")
            print()
        elif(guess == result):
            print(" congratualtion ! you win ")
            break
       
hard_attempt=5
if(choice=="hard"):
    for i in range(0,5):
        hard_attempt=hard_attempt-1
        guess=int(input("Guess the number : "))
        if(guess > result):
            print("Your guess is too long ")
            print(f"you have only {hard_attempt} attempt only ")
            print()
        elif(guess < result):
            print("Your guess is too short ")
            print(f"you have only {hard_attempt} attempt only ")
            print()
        elif(guess == result):
            print("congratualtion ! you win")
            break









    
