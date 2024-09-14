# this progrm is used to add a new dictionary to a existing list
#reffer this program to how to add a set of new information of the student 
def details(name1,roll_no1,age1,cource1):
    student_data=[
        {"Name":"Ram",
         "Roll_no":10,
         "Age":20,
         "Cource":"Python"},
        {"Name":"Mohan",
         "Roll_no":20,
         "Age":22,
         "Cource":"Java"}
        ]                       
    new_student={}              #in hhere we create a empty dictionary
    new_student["Name"]=name1    #And we assum the values to the dictionary
    new_student[ "Roll_no"]=roll_no1 #one by one (In this method only we can insert)
    new_student ["Age"]=age1        #then we use a appand fution to join the dictionary to list
    new_student["Cource"]=cource1   #now the new dictionary is joined to main dictionary
    student_data.append(new_student)#then just print it
    print(student_data) 
name=input("Enter the name of the student : ")
roll_no=int(input("Enter the roll_numner of the student : "))
age=int(input("Enter the age of the student : "))
cource=input("Enter the cource name : ")
details(name,roll_no,age,cource)

