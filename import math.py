import math
from turtle import *

# Parametric equations for heart shape
def heart(k):
    return 15 * math.sin(k) ** 3

def heart1(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

# Setup turtle environment
speed(1000)  # Fast drawing
bgcolor('black')  # Set background color
penup()  # Lift pen to move without drawing

# Draw heart shape with 6000 points
for i in range(6000):
    x = heart(i) * 20  # X position using heart equation
    y = heart1(i) * 20 # Y position using heart1 equation
    goto(x, y)         # Move to calculated position
    pendown()          # Start drawing at the position
    color('pink')      # Set drawing color to pink

done()  # Finish drawing
