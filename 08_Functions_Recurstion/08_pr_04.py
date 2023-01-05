# write a recursive function to calculate the sum of first n natural numbers.

def calculate(n):
    if n<=1:
        return n
    else:
        return n+calculate(n-1)
num=int(input("Enter required N number to Add \n"))
if num<0:
    print("Enter a positive Number")
else:
    print("The Sum of N number is ",calculate(num))
# print(calculate)
        