from tkinter import *
from tkinter import ttk

ventana = Tk()
ventana.geometry("500x500")

def pop_menu(event):
    menu.tk_popup(event.x_root,event.y_root)

estilo=ttk.Style()
estilo.configure("d.TFrame",background="white",borderwidth=2,relief="ridge")
frame =ttk.Frame(ventana,style="d.TFrame",width=200,height=300)
frame.grid(row=1,column=1)
menu = Menu(frame, tearoff=0, bg="black", fg="white")
menu.add_command(label="Copy")
menu.add_command(label="Cut")
menu.add_separator()
menu.add_command(label="Paste")
menu.add_command(label="Select all")

frame.bind("<Button-3>", pop_menu)
ventana.mainloop()


