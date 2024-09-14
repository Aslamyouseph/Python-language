stud_result={"Jenny":92,"Harry":78,"Dimpy":56,"Rahul":41,"Aniket":99,"pream":34}
values=(stud_result.values())
result={}
for i in values:
   # print(i)
    if(i>=91 and i<=100):
        result[i]="A+"
    elif(i>=81 and i<=90):
        result[i]="A"
    elif(i>=71 and i<=80):
        result[i]="B+"
    elif(i>=61 and i<=70):
        result[i]="B"
    elif(i>=51 and i<=60):
        result[i]="C"
    elif(i>=41 and i<=50):
        result[i]="D"
    else:
        result[i]="F"
print(result)       
         
 #In here we take an empty dictionary in 3 line then we assing the result into
#the empty dectionary , at last we print that empty dictionary


