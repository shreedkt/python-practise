# write a program to print multiplication table of n using for loop in reversed order.

num =int(input("Enter Your Multiplication Table Number Required\n"))
for i in range(1,11):
    print(str(num)+ "*" +str(i)+"="+str(i*num))

# Wrong program