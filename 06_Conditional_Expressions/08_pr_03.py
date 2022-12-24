# A spam comment is defined as a text containing following Keywords:-
# "make a lot of money", "buy now", "subscribe this", "click this". 
# write a program to detect these spams

text = input("Enter The Text ")

if("make a lot of money" in text):
    spam= True
elif("buy now" in text):
    spam= True
elif("subscribe this"in text):
    spam= True
elif("click this"in text):
    spam= True
else:
    spam = False
    
if(spam):
    print("This Text Is Spam")
else:
    print("This Is Not Spam")
