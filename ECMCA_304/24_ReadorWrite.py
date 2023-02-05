# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello World!\n")
    file.write("This is a sample file.")

# Reading from a file
with open("example.txt", "r") as file:
    contents = file.read()
    print(contents)
