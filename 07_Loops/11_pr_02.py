# write a program to greet all the person names stored in a list l1 and which starts with S.
# l1 =["harry","sohan","sachin","rahul"]
l1 =["harry","sohan","sachin","rahul"]
for name in l1:
    if name.startswith("s"):
        print("Hello "+name)