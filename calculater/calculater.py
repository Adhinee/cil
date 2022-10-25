
from ctypes import resize
from email.mime import image
from tkinter import *
from tkinter import messagebox
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
    e.widget['background'] = '#2F4F4F'

p=Label(root,image=img)
# p = Label(root, text="powered by: Adhinee",font=("arial",10),bg="#2F4F4F",fg="white")
p.bind("<Enter>", on_enter2)
p.bind("<Leave>", on_leave2)
p.pack()
# p.place(x=350,y=270)




entry=Entry(root,bg="#E5E5E5",font="Georgia 20",fg="black",bd=5)
# entry.bind("<Enter>", on_enter)
# entry.bind("<Leave>", on_leave)
entry.pack()
entry.place(x = 10,y = 10,width=340,height=50)




btn1=Button(root,text="1",font="10",padx="45",pady="5",bd=4,bg="#2F4F4F",fg="white")
btn1.bind("<Enter>", on_enter)
btn1.bind("<Leave>", on_leave)
btn1.pack()
btn1.place(x=0,y=100)

btn2=Button(root,text="2",font="10",padx="45",pady="5",bd=4,bg="#2F4F4F",fg="white")
btn2.bind("<Enter>", on_enter)
btn2.bind("<Leave>", on_leave)
btn2.pack()
btn2.place(x=120,y=100)

btn3=Button(root,text="3",font="10",padx="45",pady="5",bd=4,bg="#2F4F4F",fg="white")
btn3.bind("<Enter>", on_enter)
btn3.bind("<Leave>", on_leave)
btn3.pack()
btn3.place(x=240,y=100)

btn4=Button(root,text="4",font="10",padx="45",pady="5",bd=4,bg="#2F4F4F",fg="white")
btn4.bind("<Enter>", on_enter)
btn4.bind("<Leave>", on_leave)
btn4.pack()
btn4.place(x=0,y=150)

btn5=Button(root,text="5",font="10",padx="45",pady="5",bd=4,bg="#2F4F4F",fg="white")
btn5.bind("<Enter>", on_enter)
btn5.bind("<Leave>", on_leave)
btn5.pack()
btn5.place(x=120,y=150)

btn6=Button(root,text="6",font="10",padx="45",pady="5",bd=4,bg="#2F4F4F",fg="white")
btn6.bind("<Enter>", on_enter)
btn6.bind("<Leave>", on_leave)
btn6.pack()
btn6.place(x=240,y=150)

btn7=Button(root,text="7",font="10",padx="45",pady="5",bd=4,bg="#2F4F4F",fg="white")
btn7.bind("<Enter>", on_enter)
btn7.bind("<Leave>", on_leave)
btn7.pack()
btn7.place(x=0,y=200)

btn8=Button(root,text="8",font="10",padx="45",pady="5",bd=4,bg="#2F4F4F",fg="white")
btn8.bind("<Enter>", on_enter)
btn8.bind("<Leave>", on_leave)
btn8.pack()
btn8.place(x=120,y=200)


btn9=Button(root,text="9",font="10",padx="45",pady="5",bd=4,bg="#2F4F4F",fg="white")
btn9.bind("<Enter>", on_enter)
btn9.bind("<Leave>", on_leave)
btn9.pack()
btn9.place(x=240,y=200)

btn0=Button(root,text="0",font="10",padx="45",pady="5",bd=4,bg="#2F4F4F",fg="white")
btn0.bind("<Enter>", on_enter)
btn0.bind("<Leave>", on_leave)
btn0.pack()
btn0.place(x=120,y=250)

# btn1=Button(root,text="1",font="10",padx="100",pady="5")
# btn1=Button(root,text="1",font="10",padx="100",pady="5")
# btn1=Button(root,text="1",font="10",padx="100",pady="5")





# btn1.place(x=0,y=0)
# btn2.place(x=100,y=0)
# btn3.place(x=200,y=0)
# btn4.place(x=20,y=0)
# btn5.place(x=0,y=0)
# btn6.place(x=20,y=0)
# btn7.place(x=0,y=0)
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