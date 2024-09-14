import statistics
def number(a):
    avg=statistics.mean(a)
    avg2=statistics.median(a)
    avg3=statistics.mode(a)
    return(avg,avg2,avg3)
result1,result2,result3=number([1,3,2,4])
print(result1)
print(result2)
print(result3)
