from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/purple-steps-3d/r4.png]

def square_drawing(size):
    x = 0
    y = 0
    
    for i in range(5):
        size += 10
        x_v = x + size
        y_v = y + size
        my_square = canvas.create_rectangle(x, y, x_v, y_v, fill="purple")
        x = x_v
        y = y_v
        
square_drawing(10)


root.mainloop()