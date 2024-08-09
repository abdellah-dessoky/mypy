gpa = float(input("Enter your GPA :" ))
if gpa>=3.75 and gpa <= 4.0:
    print('A+')
elif gpa>=3.5 and gpa<=3.75:
    print('A')
elif gpa>=3.25 and gpa<=3.5:
    print('A-')
elif gpa>=3.0 and gpa<=3.25:
    print('B+')
elif gpa>=2.0 and gpa<=3.0:
    print('B-')
elif gpa<2.0 and gpa>=0:
    print("F")
else:
    print('Enter a valid gpa')