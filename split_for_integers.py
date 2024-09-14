num=input("Enter the numbers : ")
result=num.split(" ")
count=0
summ=0
avg=0
for i in result:
    count=count+1
print(f"count = {count}")
for i in range(count):
    result[i]=int(result[i])
    summ=summ+result[i]
avg=summ//count
print(f"sum = {summ}")
print(f"average = {avg}")

    
