name1=input("Enter the first name : ")
name2=input("Enter the second name : ")
low1=(name1.lower())
low2=(name2.lower())
low3=(low1+low2)
c1=low3.count("t")
c2=low3.count("u")
c3=low3.count("r")
c4=low3.count("e")
r1=(c1+c2+c3+c4)
t1=low3.count("l")
t2=low3.count("o")
t3=low3.count("v")
t4=low3.count("e")
r2=(t1+t2+t3+t4)
score=str(r1) +str(r2)
print(f"{score}%")


