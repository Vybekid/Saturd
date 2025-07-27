import turtle

screen = turtle.Screen()
screen.bgcolor("black")

pen = turtle.Turtle()
pen.speed(0) 
pen.hideturtle()
pen.width(2)

colors = ["#FF00FF", "#00FFFF", "#FAED27", "#FF0054"] 

for i in range(200):
    pen.pencolor(colors[i % 4])
    pen.forward(i * 2)          
    pen.left(170)               


turtle.done()