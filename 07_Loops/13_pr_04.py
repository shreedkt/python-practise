# # write a program to find whether a given number is prime or not
num = int(input("Enter a number \n"))
prime = True

for i in range(2, num):
    if(num%i==0):
        prime= False
        break
if prime:
    print("Number is prime")
else:
    print("Number is not prime")



########### Problem in below code #############

# num = int(input("Enter a  number\n"))

# for number in range(2, num):
#     if(num%number==0):
#         print("Number is Not Prime")
#     else:
#         print("Number is prime")
        


















