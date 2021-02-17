from tkinter import *
import tkinter as tk
from tkinter import Text
from tkinter import messagebox

wind = Tk()
wind.geometry("700x800")
wind.title("Mobile Registration")

# --variables --
nm = StringVar()
mbn = StringVar()

# --Function to insert data in text file--
def insert():

    k = 0
    name = nm.get()
    number = mbn.get()

    if name == "" or number == "":
        messagebox.showerror("Error", "Please enter info")
    elif len(number) > 10:
        messagebox.showerror("Error", "Invalid Mobile Number")
        inp_mbn.delete(0, 'end')
    else:
        data_file = open("data.txt",'a')
        data_file.close()
        data_file = open("data.txt",'r')
        for val in data_file.readlines():
            if number in val:
                k = 1
                break
        data_file.close()
        if k == 1:
            messagebox.showerror("Error", "Number already exists")
            inp_mbn.delete(0, 'end')
        else:
            data_file = open("data.txt","a")
            str = name +" "+ "--->"+ " " + number + "\n"
            data_file.write(str)
            inp_mbn.delete(0, 'end')
            inp_name.delete(0, 'end')
            messagebox.showinfo("Successfull", "Registered Successfully")
            data_file.close()

# --Function to display data if present--
def check():
    disp_data.delete("1.0","end")
    data_file = open("data.txt","r")
    for val in data_file.readlines():
        disp_data.insert(tk.END,val+"\n")
    if len(disp_data.get("1.0", "end-1c")) == 0:
        messagebox.showerror("Data not found", "No data to show")


# --Function to clear all text fields--
def clear():
    disp_data.delete("1.0","end")
    inp_mbn.delete(0, 'end')
    inp_name.delete(0, 'end')

# --Function to close application--
def close():
    wind.destroy()

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
inp_name.place(x=210,y=10)

lbl_mbn =  Label(f1, font=( 'aria' ,20, ),text="Mobile Number : ",fg="gray45")
lbl_mbn.place(x=0,y=70)

inp_mbn = Entry(f1,font=( 'aria' ,16, ),bg="LightYellow",width=25,textvar=mbn)
inp_mbn.place(x=210,y=80)

btn_insert = Button(f1,text="Insert",width=10, command=insert)
btn_insert.place(x=200,y=130)

# --Print Frame---
f2 = Frame(wind,width = 600,height=400,relief=SUNKEN)
f2.place(x=50,y=380)

lbl_vinf =  Label(f2, font=( 'aria' ,24, ),text="View Information : ")
lbl_vinf.place(x=0,y=0)

disp_data = Text(f2,font=( 'aria' ,16, ), width=59, height=13,bg='AliceBlue')
disp_data.place(x=0,y=40)

btn_Check = Button(f2,text="Check",width=10,command=check)
btn_Check.place(x=350,y=360)

btn_Clear = Button(f2,text="Clear",width=10,command=clear)
btn_Clear.place(x=480,y=360)

btn_Check = Button(f2,text="Exit",width=10,bg="red",command=close)
btn_Check.place(x=200,y=360)

wind.mainloop()
