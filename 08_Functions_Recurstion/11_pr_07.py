# write a python function to remove a given word from a string and strip it at the same time.

# def remove_and_split(string, word):
#     newStr = string.replace(word, "")
#     return newStr.strip()

# that = "    Deepak is also known as shreedkt"
# n= remove_and_split(that, "Deepak")    
# print(n)



def remove(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()
this ="   Hello, How are you"
m = remove(this, "Hello")
print(m)