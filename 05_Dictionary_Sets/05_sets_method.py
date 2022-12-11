# Createing an empty set
b= set()
print(type(b))
b.add(4)
b.add(5)
b.add(89)
print(b)

## Accessing Elements
# b.add({4:5})  #can't add list or dictionary to sets
# print(b) 

##Length of the set
print(len(b))

# Removal of an Item
# b.remove(5)
# b.remove(89)
print(b)

print(b.pop())