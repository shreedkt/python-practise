# n!= 1* 2* 3* 4* 5.....n


# n=5
# product=1
# for i in range(n):
#     product= product *(i+1)
# print(product)


def factorial1_iter(n):
    product=1
    n=5
    for i in range(n):
     product= product *(i+1)
    return product
 


# Example of function :--
# def mySum(num1, num2):
#     return num1+num2
# s=mySum(8,32)
# print(s)

