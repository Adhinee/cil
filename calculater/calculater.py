
from ctypes import resize
from email.mime import image
from tkinter import *
from tkinter import messagebox
from turtle import end_fill
from PIL import ImageTk, Image


root = Tk()
root.title("calculater (adhinee)")
root.configure(bg="#D1D1D1")
# root['bg']='light green'
root.geometry('500x300')
# photo=PhotoImage(file="DSC_0682.jpg")
img = ImageTk.PhotoImage(Image.open(r"C:\Users\safni\Downloads\beach.jpg"))
imgg = ImageTk.PhotoImage(Image.open(r"C:\Users\safni\Downloads\btn1.jpg"))


def on_enter(e):
    e.widget['background'] = 'green'

def on_leave(e):
    e.widget['background'] = '#2F4F4F'


def on_enter2(e):
    e.widget['background'] = 'green'

def on_leave2(e):
    e.widget['background'] = 'red'

p=Label(root,image=img)
# p = Label(root, text="powered by: Adhinee",font=("arial",10),bg="#2F4F4F",fg="white")
p.bind("<Enter>", on_enter2)
p.bind("<Leave>", on_leave2)
p.pack()
# p.place(x=350,y=270)



# ======================================================================================================================================================================

def add(nmbr):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0 ,str(current) + str(nmbr) )
    
    
def plus():
    global firstnmbr
    first=entry.get()
    firstnmbr=int(first)
    entry.delete(0,END)


def equal():
    second=entry.get()
    global secondnmbr
    secondnmbr=int(second)
    entry.delete(0, END)
    entry.insert(0 , firstnmbr + secondnmbr)

def clear():
    entry.delete(0 , END)


# def delete():
#     entry.delete(END , )







# ===================================================================------------------------------------------

entry=Entry(root,bg="#2F4F4F",font="Georgia 20",fg="white",bd=5)
entry.bind("<Enter>", on_enter)
entry.bind("<Leave>", on_leave)
entry.pack()
entry.place(x = 10,y = 10,width=340,height=50)

btn1=Button(root,text="1",command=lambda : add(1),font="10",padx="45",pady="5",bd=4,bg="#2F4F4F",fg="white",activebackground="#2F4F4F",activeforeground="white")
btn1.bind("<Enter>", on_enter)
btn1.bind("<Leave>", on_leave)
btn1.pack()
btn1.place(x=0,y=100)

btn2=Button(root,text="2",command=lambda : add(2),font="10",padx="45",pady="5",bd=4,bg="#2F4F4F",fg="white",activebackground="#2F4F4F",activeforeground="white")
btn2.bind("<Enter>", on_enter)
btn2.bind("<Leave>", on_leave)
btn2.pack()
btn2.place(x=120,y=100)

btn3=Button(root,text="3",command=lambda : add(3),font="10",padx="45",pady="5",bd=4,bg="#2F4F4F",fg="white",activebackground="#2F4F4F",activeforeground="white")
btn3.bind("<Enter>", on_enter)
btn3.bind("<Leave>", on_leave)
btn3.pack()
btn3.place(x=240,y=100)

btn4=Button(root,text="4",command=lambda : add(4),font="10",padx="45",pady="5",bd=4,bg="#2F4F4F",fg="white",activebackground="#2F4F4F",activeforeground="white")
btn4.bind("<Enter>", on_enter)
btn4.bind("<Leave>", on_leave)
btn4.pack()
btn4.place(x=0,y=150)

btn5=Button(root,text="5",command=lambda : add(5),font="10",padx="45",pady="5",bd=4,bg="#2F4F4F",fg="white",activebackground="#2F4F4F",activeforeground="white")
btn5.bind("<Enter>", on_enter)
btn5.bind("<Leave>", on_leave)
btn5.pack()
btn5.place(x=120,y=150)

btn6=Button(root,text="6",command=lambda : add(6),font="10",padx="45",pady="5",bd=4,bg="#2F4F4F",fg="white",activebackground="#2F4F4F",activeforeground="white")
btn6.bind("<Enter>", on_enter)
btn6.bind("<Leave>", on_leave)
btn6.pack()
btn6.place(x=240,y=150)

btn7=Button(root,text="7",command=lambda : add(7),font="10",padx="45",pady="5",bd=4,bg="#2F4F4F",fg="white",activebackground="#2F4F4F",activeforeground="white")
btn7.bind("<Enter>", on_enter)
btn7.bind("<Leave>", on_leave)
btn7.pack()
btn7.place(x=0,y=200)

btn8=Button(root,text="8",command=lambda : add(8),font="10",padx="45",pady="5",bd=4,bg="#2F4F4F",fg="white",activebackground="#2F4F4F",activeforeground="white")
btn8.bind("<Enter>", on_enter)
btn8.bind("<Leave>", on_leave)
btn8.pack()
btn8.place(x=120,y=200)


btn9=Button(root,text="9",command=lambda : add(9),font="10",padx="45",pady="5",bd=4,bg="#2F4F4F",fg="white",activebackground="#2F4F4F",activeforeground="white")
btn9.bind("<Enter>", on_enter)
btn9.bind("<Leave>", on_leave)
btn9.pack()
btn9.place(x=240,y=200)

btn0=Button(root,text="0",command=lambda : add(0),font="10",padx="45",pady="5",bd=4,bg="#2F4F4F",fg="white",activebackground="#2F4F4F",activeforeground="white")
btn0.bind("<Enter>", on_enter)
btn0.bind("<Leave>", on_leave)
btn0.pack()
btn0.place(x=120,y=250)

btndelt=Button(root,text="DEL",font="10",padx="33",pady="5",bd=4,bg="#2F4F4F",fg="white",activebackground="#2F4F4F",activeforeground="white")
btndelt.bind("<Enter>", on_enter)
btndelt.bind("<Leave>", on_leave)
btndelt.pack()
btndelt.place(x=0,y=250)

btneql=Button(root,command=equal,text="=",font="10",padx="45",pady="5",bd=4,bg="#2F4F4F",fg="white",activebackground="#2F4F4F",activeforeground="white")
btneql.bind("<Enter>", on_enter)
btneql.bind("<Leave>", on_leave)
btneql.pack()
btneql.place(x=240,y=250)

btnpls=Button(root,command=plus,text="+",font="10",padx="45",pady="5",bd=4,bg="#2F4F4F",fg="white",activebackground="#2F4F4F",activeforeground="white")
btnpls.bind("<Enter>", on_enter)
btnpls.bind("<Leave>", on_leave)
btnpls.pack()
btnpls.place(x=360,y=100)

btnmins=Button(root,text="-",font="10",padx="45",pady="5",bd=4,bg="#2F4F4F",fg="white",activebackground="#2F4F4F",activeforeground="white")
btnmins.bind("<Enter>", on_enter)
btnmins.bind("<Leave>", on_leave)
btnmins.pack()
btnmins.place(x=360,y=150)

btnmultpl=Button(root,text="*",font="10",padx="45",pady="5",bd=4,bg="#2F4F4F",fg="white",activebackground="#2F4F4F",activeforeground="white")
btnmultpl.bind("<Enter>", on_enter)
btnmultpl.bind("<Leave>", on_leave)
btnmultpl.pack()
btnmultpl.place(x=360,y=200)

btndvd=Button(root,text="/",font="10",padx="45",pady="5",bd=4,bg="#2F4F4F",fg="white",activebackground="#2F4F4F",activeforeground="white")
btndvd.bind("<Enter>", on_enter)
btndvd.bind("<Leave>", on_leave)
btndvd.pack()
btndvd.place(x=360,y=250)

btnclr=Button(root,text="CLEAR",command=clear,font="10",padx="21",pady="5",bd=4,bg="red",fg="white",activebackground="#2F4F4F",activeforeground="white")
btnclr.bind("<Enter>", on_enter)
btnclr.bind("<Leave>", on_leave2)
btnclr.pack()
btnclr.place(x=360,y=17)

# btn1=Button(root,text="1",font="10",padx="100",pady="5")
# btn1=Button(root,text="1",font="10",padx="100",pady="5")
# btn1=Button(root,text="1",font="10",padx="100",pady="5")





# btn1.place(x=0,y=0)
# btn2.place(x=100,y=0)
# btn3.place(x=200,y=0)
# btn4.place(x=20,y=0)
# btn5.place(x=0,y=0)
# btn6.place(x=20,y=0)
# btn7.place(x=0,y=0 )
# btn8.place(x=20,y=0)
# btn9.place(x=0,y=0)
# btn0.place(x=20,y=0)

# btn3.grid(row=1,column=3)
# btn1.grid(row = 1 , column = 1)

# btn4.grid(row=1,column=1)
# btn5.grid(row=1,column=1)
# btn6.grid(row=1,column=1)


# btn7.grid(row=1,column=1)
# btn8.grid(row=1,column=1)
# btn9.grid(row=1,column=1)

# btn0.btn.place(x=,y=)
#  btn4.pack()
# btn5.pack()
# btn6


root.mainloop()
