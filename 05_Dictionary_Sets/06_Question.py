# Write a program to create a dictionary of hindi words with value as their 
# english transilation provide user to look it up..! 

myDict = {
    "pankha":"Fan",
    "dabba": "Box",
    "vastu": "Iteam"
}
print("options are", myDict.keys())
a = input("Enter The Hindi Words \n")
# print("The meaning of word is:", myDict[a])

#Below line of code not throw error if key is not present in the dictonary
print("The meaning of word is:", myDict.get(a))