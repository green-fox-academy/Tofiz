from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw four different size and color rectangles.

dif_size_color_rectangles = canvas.create_rectangle(50, 50, 70, 70, fill="black")
dif_size_color_rectangles = canvas.create_rectangle(100, 50, 150, 100, fill="grey")
dif_size_color_rectangles = canvas.create_rectangle(200, 50, 230, 80, fill="dark grey")
dif_size_color_rectangles = canvas.create_rectangle(20, 150, 80, 230, fill="light grey")

root.mainloop()