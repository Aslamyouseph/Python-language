#when user enter some numbers and print this number in dessending oder
num=input("Enter the number : ")
result=num.split(" ")
count=0
sum=0
for i in result:
    count=count+1
print(count)
for i in range(count):
    result[i]=int(result[i])
    sum=sum+result[i]
print(f"before sorting {result}")    
print(f"sum = {sum}")
for i in range(count):
    result.sort()    
print(f"After sort {result}")

