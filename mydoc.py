import turtle

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle
pen = turtle.Turtle()
pen.speed(0) # Set the drawing speed to the fastest
pen.hideturtle()

# Define a list of rainbow colors
colors = ["red", "orange", "yellow", "green", "blue", "indigo"]

# Main loop to rotate the squares
for i in range(72):
    pen.pencolor(colors[i % 6]) # Cycle through the colors
    
    # Draw a single square
    for _ in range(4):
        pen.forward(200)
        pen.right(90)
        
    pen.right(5) # Tilt the turtle by 5 degrees for the next square

# Keep the window open until it's closed
turtle.done()