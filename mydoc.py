import turtle

def draw_yin_yang(radius):
    """
    Draws a corrected Yin and Yang symbol with the specified radius.

    Args:
        radius: The radius of the main circle.
    """
    # --- Setup ---
    screen = turtle.Screen()
    screen.title("Yin and Yang - Corrected")
    screen.setup(width=radius*2 + 50, height=radius*2 + 50)
    
    t = turtle.Turtle()
    t.speed(0)  # Set speed to fastest for instant drawing
    t.hideturtle()

    # --- Drawing Logic ---
    
    # 1. Draw the black half and the white half's outline
    t.fillcolor("black")
    t.begin_fill()
    
    # Draw the S-shaped dividing line
    t.circle(radius / 2, 180)
    t.circle(radius, 180)
    t.left(180)
    t.circle(-radius / 2, 180)
    
    t.end_fill()

    # 2. Draw the small black dot in the white area
    t.penup()
    t.goto(0, (radius / 2) - (radius / 8)) # Position the turtle for the dot
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    t.circle(radius / 8)
    t.end_fill()

    # 3. Draw the small white dot in the black area
    t.penup()
    t.goto(0, -(radius / 2) - (radius / 8)) # Position the turtle for the dot
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    t.circle(radius / 8)
    t.end_fill()

    # --- Finalization ---
    # Keep the window open until it is clicked
    screen.exitonclick()

# --- Main Execution ---
if __name__ == "__main__":
    draw_yin_yang(200)