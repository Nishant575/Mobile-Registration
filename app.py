from tkinter import *
from tkinter import Text

wind = Tk()
wind.geometry("700x800")
wind.title("Mobile Registration")

# --variables --
nm = StringVar()
mbn = StringVar()

# --Design --
lbl_head = Label(wind, font=( 'aria' ,28, 'bold' ),text="Mobile Registration",fg="steel blue",bd=10)
lbl_head.place(x=230,y=0)



lbl_inf = Label(wind, font=( 'aria' ,24, ),text="Enter Information : ",fg="Black")
lbl_inf.place(x=60,y=110)

# --Input Frame--
f1 = Frame(wind,width = 550,height=220,relief=SUNKEN)
f1.place(x=130,y=190)

lbl_name =  Label(f1, font=( 'aria' ,20, ),text="Name : ",fg="gray45")
lbl_name.place(x=80,y=0)

inp_name = Entry(f1,font=( 'aria' ,16, ),bg="LightYellow",width=25,textvar=nm)
inp_name.place(x=170,y=0)

lbl_mbn =  Label(f1, font=( 'aria' ,20, ),text="Mobile Number : ",fg="gray45")
lbl_mbn.place(x=0,y=70)

inp_mbn = Entry(f1,font=( 'aria' ,16, ),bg="LightYellow",width=25,textvar=mbn)
inp_mbn.place(x=170,y=70)

btn_insert = Button(f1,text="Insert",width=10,bg="red")
btn_insert.place(x=200,y=130)

# --Print Frame---
f2 = Frame(wind,width = 600,height=400,relief=SUNKEN)
f2.place(x=50,y=380)

lbl_vinf =  Label(f2, font=( 'aria' ,24, ),text="View Information : ")
lbl_vinf.place(x=0,y=0)

disp_data = Text(f2,font=( 'aria' ,16, ), width=59, height=13,bg='AliceBlue')
disp_data.place(x=0,y=40)

btn_Check = Button(f2,text="Check",width=10)
btn_Check.place(x=350,y=300)

btn_Clear = Button(f2,text="Clear",width=10)
btn_Clear.place(x=480,y=300)



wind.mainloop()
