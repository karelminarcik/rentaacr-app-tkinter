from tkinter import *

window = Tk()
window.title("Renta AČR")
window.geometry("700x500")

# canvas = Canvas(window, height=200, width=400, bg="black")
# money_image = PhotoImage(file="money.png")
# canvas.create_image(100, 100, anchor=NW, image=money_image)
# canvas.grid(row=3, column=0, columnspan=3)

my_img = PhotoImage(file='money.png')
my_img.img = my_img
 
resized_img = my_img.subsample(2,2)
canvas = Canvas()
canvas.create_image(window.winfo_reqwidth(), window.winfo_reqheight()/2, image=resized_img)
canvas.pack()

window.mainloop()