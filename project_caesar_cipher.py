print("                 caesar cipher ")
alpha=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
def conti(Encrypt_list,shift):
    result1=""
    for i in Encrypt_list:
        result=alpha.index(i)
        new_possition=(result+shift)%26
        result1+=alpha[new_possition]
        return(result1)

def con(decrypt_list,shift):
    result2=""    
    for i in decrypt_list:
        result=alpha.index(i)
        new_possition=(result-shift)%26
        result2+=alpha[new_possition]
        return(result2)
again=True
list1=[]
while again:
    ED=input("Type E for Encryption , Type d for decription :")
    message=input("Enter your message : ").upper()
    shift=int(input("Enter the shift key : "))
    if(ED =="E" or ED =="e"):
        aresult=conti(message,shift)
        print(f"here your encrypt text {aresult} ")
    elif(ED =="D" or ED =="d"):
        bresult= con(message,shift)
        print(f"here your decrypt message {bresult}")
    else:
        print("Invalid entry  ")


















