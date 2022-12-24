# Write a program to find out whether a given post is talking about "Harry" ot not
l1 =['deepak','mohan','shyam','anjali','radha']

element= input("ENter the element\n")
element = element.lower()
if element in l1:
    print("Yes element is found")
else:
    print("Element is not present")