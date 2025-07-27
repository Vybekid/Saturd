import turtle

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle
pen = turtle.Turtle()
pen.speed(0) # Set the drawing speed to the fastest
pen.hideturtle()
pen.width(2)

# Define two contrasting colors
colors = ["white", "cyan"]

# Drawing loop
for i in range(180):
    pen.pencolor(colors[i % 2]) # Alternate between the two colors
    pen.circle(150)             # Draw the outer circle
    pen.circle(i / 2)           # Draw an inner, growing circle
    pen.left(2)                 # Rotate by 2 degrees

# Keep the window open until it's closed
turtle.done()