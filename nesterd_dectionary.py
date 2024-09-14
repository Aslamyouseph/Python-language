student_details={"Aslam":{"Roll_no":23,"Class":"Bca","Age":21,},
                "Afnitha":{"Roll_no":21,"Class":"Plus one","Age":16}}
print(student_details)
print(student_details["Afnitha"])
print(student_details["Afnitha"]["Roll_no"])
student_details["Afnitha"]["phone_no"]=9018384789
print(student_details)
print(student_details["Aslam"].pop("Roll_no"))
print(student_details)



