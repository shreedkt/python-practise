# write a program to calculatte the factorial of a given number using for loop.
num = int(input("Enter Number for factorial\n"))
factorial=1
for i in range(1, num+1):
    factorial=factorial*i
print(f"The Factorial of {num} is {factorial}")