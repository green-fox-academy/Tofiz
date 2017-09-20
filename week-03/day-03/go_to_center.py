from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# draw 3 lines with that function.
def line_drawing(x, y):
    teal_line = canvas.create_line(x, y, 150, 150,)
        
line_drawing(50, 50)
line_drawing(100, 0)
line_drawing(150, 50)



root.mainloop()