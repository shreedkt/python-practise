f = open('poem.txt')
data=f.read()
if 'twinkle' in data:
    print("twinkle is present")
else:
    print("twinkle is not present")
    
f.close()
