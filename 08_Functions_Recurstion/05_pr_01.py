# write a program to useing function find the greatest of three number 
def maximum(num1, num2, num3):
    if(num1>num2):
        if(num1>num3):
            return num1
    else:
        if(num2>num3):
            return num2
        else:
            return num3

d= maximum(21,22,23)
print("The Maximum number is", str(d))