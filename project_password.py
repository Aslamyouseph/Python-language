print("PASSWORD GENERATING PROGRAM ")
letters=int(input("Howmany letters you wand to your password : "))
numbers=int(input("Howmany numbers you wand your password : "))
symbols=int(input("Howmany symbols are you wand your passwors : "))
list_letters=["a","b","c","d","e","f","g","A","B","C","D","E","F","G","h","i","j","k","l","m","n","o","p","q","r","s","H","I","J","K","L","N","M","O","P","Q","R","S"]
list_numbers=["1","2","3","4","5","6","7","8","9","10","0"]
list_symbols=["!","@","$","%","^","&","*","(",")","/"]
import random
random.shuffle(list_letters)
random.shuffle(list_numbers)
random.shuffle(list_symbols)
password_list=[]                #check here onwards 
for i in range(1,letters+1):
    result=random.choice(list_letters)
    password_list+=result
for i in range(1,numbers+1):
    result=random.choice(list_numbers)
    password_list+=result 
for i in range(1,symbols+1):
    result=random.choice(list_symbols)
    password_list+=result
random.shuffle(password_list)
password=""
for i in password_list:
    password += i
print()
print(f"YOUR PASSWORD IS : {password}")

#in tere we create a empty list
#then take another varible(result) and and assing the result into this varible
#this second varible (result)is assingned to our empty list
#then we shuffle this list
#the we create a empty string(password)
#by using for loop we assing our list into the string
#at this time out output is in the form of a string
#the we print our string(password)
