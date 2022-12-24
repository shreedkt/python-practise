# write a program to calculate the grade of a student from his marks from the following scheme:-
# 90-100 ->Excelent
# 80-90 ->A
# 70-80 ->B
# 60-70 ->C
# 50-0 ->D
#<50 ->F

marks = int(input("Enter Your Marks"))

if marks>=90:
    print("Excelent")
elif marks>=80:
    print("A")
elif marks>=70:
    print("B")
elif marks>=60:
    print("C")
elif marks>=50:
    print("D")
elif marks<50:
    print("F")