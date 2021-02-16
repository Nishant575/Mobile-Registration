from tkinter import *

wind = Tk()
wind.geometry("700x700")
wind.title("Mobile Registration")

lbl1 = Label(wind, font=( 'aria' ,24, 'bold' ),text="Mobile Registration",fg="steel blue",bd=10,anchor=W)
lbl1.grid(row=1,column=5)
lbl2 = Label(wind, font=( 'aria' ,18, ),text="Enter Information ",fg="Black",anchor=W)
lbl2.grid(row=3,column=0)

wind.mainloop()
