letter =''' Dear <|Name|>
You are Selected
Date :- <|Date|>
'''
name = input("Enter Your Name\n")
date = input("Enter Date\n")

letter= letter.replace("<|Name|>",name)
letter=letter.replace("<|Date|>",date)
print(letter)