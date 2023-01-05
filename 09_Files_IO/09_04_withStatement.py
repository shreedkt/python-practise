with open('another.txt', 'r') as f:
    a =f.read()
with open('another.txt', 'w') as f:
    a = f.write("Hello, I'm Deepak Tiwari")
print(a)

# with statement don't need of close the file....