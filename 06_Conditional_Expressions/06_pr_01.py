#Write a program to find greatest of four number entered by the user
num1 =int(input('Enter First Number \n'))
num2 =int(input('Enter Second Number \n'))
num3 =int(input('Enter Third Number \n'))
num4 =int(input('Enter Forth Number \n'))
if(num1>num2):
    print(num1, 'is greater')
elif(num2>num3):
    print(num2, 'is greater')
elif(num3>num4):
    print(num3,'is greater')
else:
    print(num4, 'is greater')