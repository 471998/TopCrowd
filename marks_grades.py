##Student Name    Marks
##David                    80
##Vinoth                  77
##Divya                    88
##Ishitha                 95
##Thomas              68
##The grades are computed as follows :
##
##Range    Grade
##<60            F
##<70            D
##<80            C
##<90            B
##<100          A

student_details={"David": 80, "Vinoth": 77, "Divya":88, "Ishitha":95, "Thomas":68}
for i,j in student_details.items():
    if j < 60:
        print("Grade:F", i,j)
    elif j < 70:
        print("Grade:D", i,j)
    elif j < 80:
        print("Grade:C", i,j)
    elif j < 90:
        print("Grade:B", i,j)
    elif j < 100:
        print("Grade:A", i,j)
        
