from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/purple-steps/r3.png]

def square_drawing(size):
   position = 10
   for i in range(13):
        my_square = canvas.create_rectangle(position, position, position+size*4, position+size*4, fill="purple")
        position += 20

square_drawing(5)

root.mainloop()