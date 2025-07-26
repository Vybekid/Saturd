import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Yin and Yang")

# Create turtle
t = turtle.Turtle()
t.speed(0)

# Constants
RADIUS = 140

# Draw outer circle
t.penup()
t.goto(0, -RADIUS)
t.pendown()
t.pensize(2)
t.circle(RADIUS)

# Draw black half
t.penup()
t.goto(0, -RADIUS)
t.setheading(0)
t.fillcolor("black")
t.begin_fill()
t.circle(RADIUS, 180)
t.circle(RADIUS / 2, 180)
t.circle(-RADIUS / 2, 180)
t.end_fill()

# Draw white half
t.penup()
t.goto(0, -RADIUS)
t.setheading(0)
t.begin_fill()
t.circle(-RADIUS, 180)
t.circle(-RADIUS / 2, 180)
t.circle(RADIUS / 2, 180)
t.end_fill()

# Small black dot in white area
t.penup()
t.goto(0, RADIUS / 2)
t.setheading(0)
t.fillcolor("black")
t.begin_fill()
t.circle(RADIUS / 10)
t.end_fill()

# Small white dot in black area
t.penup()
t.goto(0, -RADIUS / 2)
t.setheading(0)
t.fillcolor("white")
t.begin_fill()
t.circle(RADIUS / 10)
t.end_fill()

# Add text
t.penup()
t.goto(0, -RADIUS - 40)
t.pencolor("black")
t.write("BY :- amazing_coder007", align="center", font=("Arial", 10, "bold"))

# Finish
t.hideturtle()
turtle.done()
