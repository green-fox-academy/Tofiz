from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw a box that has different colored lines on each edge.
teal_line = canvas.create_line(100, 100, 100, 200, fill='red')
teal_line = canvas.create_line(100, 200, 200, 200, fill='green')
teal_line = canvas.create_line(200, 200, 200, 100, fill='blue')
teal_line = canvas.create_line(200, 100, 100, 100, fill='black')
root.mainloop()