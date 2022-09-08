import random
from turtle import Turtle, Screen
screen = Screen()
patrick_the_turtle = Turtle()
patrick_the_turtle.shape('turtle')
patrick_the_turtle.color('blue')
'''
import colorgram

# Extract 108 colors from an image.
colors = colorgram.extract('/Users/german/Documents/Python projects/My coding projects/Hirst Painting/image.jpg', 108)

# colorgram.extract returns Color objects, which let you access
# RGB, HSL, and what proportion of the image was that color.
rgb_colors = []
for color in colors:
	r = color.rgb.r
	g = color.rgb.g
	b = color.rgb.b
	tuple = (r, g, b)
	rgb_colors.append(tuple)
'''    
rgb_colors = [(34, 108, 167), (245, 77, 36), (112, 163, 211), (153, 57, 85), (219, 156, 94), 
			  (201, 60, 27), (24, 133, 55), (246, 204, 84), (190, 151, 47), 
			  (225, 119, 152), (46, 53, 121), (221, 68, 97), (113, 199, 156), (147, 37, 30), 
			  (253, 202, 0), (91, 113, 192), (74, 40, 32), (248, 153, 143), (111, 41, 49), 
			  (155, 212, 203), (53, 174, 163), (38, 31, 67), (154, 210, 219), (43, 33, 45), 
			  (35, 55, 46), (99, 93, 2), (43, 151, 190), (10, 111, 51), (228, 169, 182), (177, 186, 217)
			]     
def random_color():
	screen.colormode(255)
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	patrick_the_turtle.pencolor((r, g, b))
	patrick_the_turtle.color((r, g, b))
	
def next_row():
	patrick_the_turtle.penup()
	patrick_the_turtle.sety(250)
	xcor = patrick_the_turtle.xcor()
	new_xcor = xcor - 60
	patrick_the_turtle.setx(new_xcor)
	patrick_the_turtle.pendown()
	
def next_dot():
	patrick_the_turtle.penup()  
	ycor = patrick_the_turtle.ycor()
	new_ycor = ycor - 60
	patrick_the_turtle.sety(new_ycor)
	patrick_the_turtle.pendown()  
def hirst_painting():
	patrick_the_turtle.speed(0)
	patrick_the_turtle.penup()
	patrick_the_turtle.goto(350, 300)
	patrick_the_turtle.pendown()
	for x in range(11):
		next_row()
		for i in range(10):
			random_color()
			patrick_the_turtle.begin_fill()
			patrick_the_turtle.circle(20)
			patrick_the_turtle.end_fill()
			patrick_the_turtle.penup()
			next_dot()
			patrick_the_turtle.pendown()
			
	
hirst_painting()    
screen.exitonclick()            