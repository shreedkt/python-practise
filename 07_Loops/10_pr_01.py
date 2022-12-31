#write a program to print multiplication table of a given number using for loops
num =int(input("Enter Your Multiplication Table Number Required\n"))
for i in range(1,11):
    print(str(num)+ "*" +str(i)+"="+str(i*num))