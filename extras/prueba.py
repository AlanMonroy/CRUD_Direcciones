from tkinter import *

root = Tk()

red = Entry(root,bg="red")
red.grid(row=0,column=0,padx=10,pady=10)
white = Entry(root,bg="white")
white.grid(row=1,column=0,padx=10,pady=10)
blue = Entry(root, bg="blue")
blue.grid(row=2,column=0,padx=10,pady=10)

def btn_clicked():
    top=Toplevel(root)
    red1 = Entry(top,bg="red")
    red1.grid(row=0,column=0,padx=10,pady=10)
    red1.focus()
    white1 = Entry(top,bg="white")
    white1.grid(row=1,column=0,padx=10,pady=10)
    blue2 = Entry(top, bg="blue")
    blue2.grid(row=2,column=0,padx=10,pady=10)

boton = Button(root,text="Entrar",command=btn_clicked)
boton.grid(row=3,column=0,padx=10,pady=10)


root.mainloop()




