import turtle

window = turtle.Screen()

drawer = turtle.Turtle()

lines = int(input("How many lines do you want to be drawn?"))
line_spacing = int(input("How much spacing (pixels) do you want between lines?"))

length = 0
for i in range(lines):
    drawer.forward(10 + length)
    drawer.right(90)
    length += line_spacing


