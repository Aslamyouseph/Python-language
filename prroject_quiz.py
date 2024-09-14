
print()
print("*************************************************")
print()
print("WELCOME TO MY QUIZ ................")
print()
print("***************************************************")
print()

def operation(choice,correct):
    if(choice==correct):
        print("You enterd the correct answer , congratulation  ! ")
        return 1 
    else:
        print("You enterd wrong answer ")
        
score=0
points=0

print("which is the first letter of alphabet ")
print("""
1 = R
2 = O
3 = A
4 = P"""
)
choice=int(input("Enter your choice "))
correct=3
print()
num=operation(choice,correct)
if (num ==1):
    score=score+1
    points=points+10
    print(f"your score is {score}/5")
print()

print("Name of our country ")
print("""
1 = usa
2 = canada
3 = india
4 = chaina """)
choice=int(input("Enter your choice "))
correct=3
print()
num=operation(choice,correct)
if(num==1):
    score=score+1
    points=points+10
    print(f"your score is {score}/5")
print()

print("What is (3+4)")
print("""
1 = 3
2 = 7
3 = 4
4 = 1 """)
choice=int(input("Enter your choice "))
correct=2
print()
num=operation(choice,correct)
if  (num==1):
    score=score+1
    points=points+10
    print(f"your score is {score}/5")
print()

print("when the independences  day ")
print("""
1 = june 23
2 = feb 4
3 = agu 15
4 = dec 9""")
choice=int(input("Enter your choice "))
correct=3
print()
num=operation(choice,correct)
if(num==1):
    score=score+1
    points=points+10
    print(f"your score is {score}/5")
print()

print("which is the first digit in number system ")
print("""
1 = 3
2 = 1
3 = 7
4 = 0""")
choice=int(input("Enter your choice "))
correct=4
print()
num=operation(choice,correct)
if(num==1):
    score=score+1
    points=points+10
    print(f"your score is {score}/5")
print(f"Now you got {points} points ")


    
