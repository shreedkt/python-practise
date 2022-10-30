from re import U


myDict={
    "fast": "In a Quick Manner",
    "deepak":"A Coder",
    "marks":[15,42,56],
    "anotherDict":{'Harry':'Player'},
    1: 15
}

#Dictionary Methods
# print(myDict.keys()) #print the keys of the dictionary 
# print(type(myDict.keys())) #print the key value of dictionary
# print(list(myDict.values())) #prints the value of dictionary
# print(myDict.items()) #print the (key, value) for all contents of the dictionary


# print(myDict)
# updateDict ={
#     "Dikshu":"Friend",
#     "Sushil":"Brother"
# }
# myDict.update(updateDict)
# print(myDict)

print(myDict.get("deepak")) #print value associated with "deepak"
print(myDict['deepak']) #print value associated with "deepak"

  #the difference b/w .get and [] syntex in dictionary
# print(myDict.get("deepak2")) #Returns NONE as deepak2 is not present in dictionary
# print(myDict['deepak2']) #it throw error deepak2 is not present in dictionary