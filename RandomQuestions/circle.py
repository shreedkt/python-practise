# import turtle
# import colorsys
# t= turtle.Turtle()
# s=turtle.Screen().bgcolor('black')
# t.speed(0)
# n=70
# h=0
# for i in range(100):
# c=colorays.hav_to_rgb(h, 1, 0.8)
# Python program to demonstrate
# concentric circle drawing


import turtle
	
	
t = turtle.Turtle()

# radius of the circle
r = 10

# Loop for printing concentric circles
for i in range(50):
	t.circle(r * i)
	t.up()
	t.sety((r * i)*(-1))
	t.down()
