height=input("Enter the height  : ")
final_height=height.split(" ")
c=0
for height in final_height:
    c=c+1
print(c)
for i in range(0,c):
    final_height[i]=int(final_height[i])
print(final_height)
