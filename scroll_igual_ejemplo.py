from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("500x400")

mainFrame=Frame(root)
mainFrame.pack(fill=BOTH, expand=True)

canvas = Canvas(mainFrame)
canvas.pack(side=LEFT, fill=BOTH, expand=True)

scrollbar= ttk.Scrollbar(mainFrame, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

secondFrame=Frame(canvas)

canvas.create_window((0,0), window=secondFrame, anchor="nw")

for i in range(5):
	Button(secondFrame,text=f"Boton {i}").grid(row=i,column=0,padx=10,pady=10)



root.mainloop()