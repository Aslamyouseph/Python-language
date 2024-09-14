weight=float(input("enter the body weight : "))
height=float(input("enter the body height : "))
body_weight = weight/height**2
if(body_weight<16.0):
    print("Body is underweight  ")
elif(body_weight>16.0 and body_weight<16.9):
    print("body is underweight(Moderate thikness)")
elif(body_weight>17.0 and body_weight<18.4):
    print("body is underweight(Mild thikness)")
elif(body_weight>18.5 and body_weight<24.9):
    print("body is in normal range ")
elif(body_weight>25.0 and body_weight<29.9):
    print("body is overweight(pre-obese)")
elif(body_weight>30.0 and body_weight<34.9):
    print("body is obese (class 1)")
elif(body_weight>35.0 and body_weight<39.9):
    print("body is obese (class 2)")
elif(body_weight>40.0):
    print("body is obese (class 3)")
else:
    print("invalid entry of weight or height ")
