from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# draw 3 squares with that function.

def square_drawing(size):
    my_square = canvas.create_rectangle(150, 150, 150+size, 150+size, fill="black")

square_drawing(9)

root.mainloop()