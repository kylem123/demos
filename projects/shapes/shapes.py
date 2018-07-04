'''
Created on 27 Oct 2014

@author: kyle
'''
import turtle, time
from turtle import Screen

window = turtle.Screen()
lil_guy = turtle.Turtle()

DEBUG = True

shapes = [
    {"Name": 'Circle', "Sides": 360},
    {"Name": 'Triangle', "Sides": 3},
    {"Name": 'Square', "Sides": 4},
    {"Name": 'Pentagon', "Sides": 5},
    {"Name": 'Hexagon', "Sides": 6},
    {"Name": 'Septagon', "Sides": 7},
    {"Name": 'Octagon', "Sides": 8},
    {"Name": 'Nonogan', "Sides": 9},
    {"Name": 'Decagon', "Sides": 10}
]

def setup():
    lil_guy.up()
    
    width = window.window_width()
    center = width / 2
    shapes_halved = len(shapes) / 2
    shapes_size = 120
    size = shapes_halved * shapes_size
    #lil_guy.backward(center - size)
    lil_guy.backward(500)

    lil_guy.down()
    lil_guy.speed(0)

def draw_shape(shape):
    if(DEBUG):
        print("A " + shape["Name"] + " has " + str(shape["Sides"]) + " side(s) and rotates at an angle of " + str(calculate_angle(shape["Sides"])) + " degrees")
    
    lil_guy.begin_fill()
    for side in range(shape["Sides"]):
        lil_guy.forward(60 * (3 / shape["Sides"]))
        lil_guy.left(180 - calculate_angle(shape["Sides"]))
    lil_guy.right(90)
    lil_guy.setheading(0)
    lil_guy.up()
    lil_guy.forward(120)
    lil_guy.down()
    lil_guy.end_fill()
    #window.exitonclick()

def draw_shape_sides(sides):
    shape = {"Name": 'Custom Shape', "Sides": sides}
    draw_shape(shape)

def calculate_angle(sides):
    return ((sides - 2) * 180) / sides
      
def check_shape(shape):
    for i in range(len(shapes)):
        if(shapes[i]["Name"] == shape):
            return i
    if(shape != 'All'):
        return -1

looping = True

while(looping):
    setup()

    shape = input("Enter the name of a shape you would like to draw or enter the number of sides you wish to have? ('All' will draw all the shapes from a circle to a decagon)")

    shape_ID = -1
    shape_ID = check_shape(shape)

    if(shape_ID != -1 or shape.isdigit()):
        line_colour = input("What colour do you want the shape's outline to be? ('red', 'blue', 'yellow', 'green', 'black')")
        fill_colour = input("What colour do you want the shape to be filled with? ('red', 'blue', 'yellow', 'green', 'black')")
    
        lil_guy.color(line_colour, fill_colour)
    
        if(shape == 'All'):
            for i in range(len(shapes)):
                draw_shape(shapes[i])
        elif(shape.isdigit()):
            draw_shape_sides(int(shape))
        else:
            draw_shape(shapes[shape_ID])
        
        exit = input("Exit? 'y' or 'n'")
        if(exit == 'y'):
            looping = False
        
    else:
        print("Invalid Shape ('" + shape + "'). Please enter a valid shape")


