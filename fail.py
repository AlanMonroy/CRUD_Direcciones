# -*- coding: utf-8 -*-

# from tkinter import *
# from tkinter import ttk
# from tkinter import filedialog
# from tkinter import messagebox
# from tkinter.ttk import Combobox
# from Conexion import Conexion
# from datetime import datetime
# from PIL import Image, ImageTk
# import tkinter.font as tkFont
# import tkinter as tk
# import tkinter.ttk as ttk
# import pyodbc
# import hashlib
# import tkinter
# from ttkthemes import ThemedTk
# import ctypes
# import pandas as pd

from tkinter import *
from logger_base import log
from ttkthemes import ThemedTk
from tkinter import Canvas, Entry, messagebox, PhotoImage, Button, Frame, ttk
from PIL import Image, ImageTk

class Interfaz:
    def __init__(self):
        # self.window = window
        # self.window.title(title)
        # self.x = -9; self.y = 0

        self.window = Tk()
        # self.window=ThemedTk(theme="adapta")
        self.window.geometry("500x500")

        # self.w, self.h = self.window.winfo_screenwidth(), self.window.winfo_screenheight() 
        # print(self.window.winfo_screenwidth(),self.window.winfo_screenheight())
        # self.window.geometry("%dx%d+%d+%d" % (self.w, self.h, self.x, self.y))
        # self.window.resizable(False, True)
        self.window.iconbitmap('images/icono.ico')

        #self.window.attributes('-fullscreen', True) 
        #self.window.theme_use("Adapta")
        # self.canvas = Canvas(
        #     self.window,
        #     bg = "#ffffff",
        #     height = self.h,
        #     width = self.w,
        #     bd = 0,
        #     highlightthickness = 0,
        #     relief = "ridge")
        # #self.canvas.place(x = 0, y = 0)
        # self.canvas.pack(side=LEFT, fill=BOTH, expand=1)
        #((((((((((((((((((((((((()))))))))))))))))))))))))
        canvas = Canvas(self.window)
        canvas.pack(side=LEFT,fill=BOTH,expand=1)

        scrollbar = ttk.Scrollbar(self.window, orient=VERTICAL, command=canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind("<Configure>", lambda e: self.canvas.configure(scrollregion = canvas.bbox("all")))

        secondFrame = Frame(canvas)

        canvas.create_window((0,0), window=secondFrame, anchor="nw")
        #(((((((((((((((((((((((())))))))))))))))))))))))

        # self.background_img = PhotoImage(file = f"images/background.png")
        # background = self.canvas.create_image(self.window.winfo_screenwidth()/2, self.window.winfo_screenheight()/2,image=self.background_img)

        # self.img0 = PhotoImage(file = f"images/barra_menu.png")
        # self.b0 = Button(secondFrame,
        #     image = self.img0,
        #     borderwidth = 0,
        #     highlightthickness = 0,
        #     # command = btn_clicked,
        #     relief = "flat", activebackground="#16660A", bg="#16660A")

        # self.b0.grid(row=0, column=0)

        for i in range(100):
            Button(secondFrame, text=f"boton {i}").grid(row=i,column=0, padx=10, pady=10)
        
        self.window.mainloop()

#_____________________-----------------------------____________Constructor____________------------------------------_______________________

if __name__ == "__main__":
    Interfaz()
    # window = Tk()
    # #window=ThemedTk(theme="adapta")
    # interfaz = Interfaz(window, "Interfaz")
    # window.mainloop()
