
import turtle
colors = ["red", "green","blue"] 
num_circles = 12 
radius = 100
painter = turtle.Turtle()
painter.speed(0) 
painter.pensize(3)
for i in range(num_circles):
    current_color_index = i % len(colors) 
    color = colors[current_color_index]
    painter.pencolor(color)
    painter.circle(radius)
    painter.right(360 / num_circles)   
painter.hideturtle()
