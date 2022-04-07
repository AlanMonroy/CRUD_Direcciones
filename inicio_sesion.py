from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
from PIL import ImageTk, Image
from tkinter import messagebox
from interfaz import Interfaz

class Login:
    def __init__(self, window, title, w, h):

        self.w = w
        self.h = h
        self.x = int(window.winfo_screenwidth() / 5)
        self.y = int(window.winfo_screenheight() / 10)
        #self.x = 0
        #self.y = 0 
    
        self.window = window
        self.window.title(title)
        self.window.geometry(f"{self.w}x{self.h}+{self.x}+{self.y}")
        self.window.resizable(False, False)
        #self.window.iconbitmap('images/icono.ico')
        self.window.configure(background = '#ffffff')
        #self.window.wm_attributes("-transparentcolor","#60b26c")
        #self.window.wm_attributes("-alpha",.9)

        def on_closing():
            if messagebox.askokcancel("Salir", "¿Estas seguro que quieres salir?"):
                self.window.destroy()

        self.window.protocol("WM_DELETE_WINDOW", on_closing)

        self.canvas = Canvas(
            self.window,
            bg = "#ffffff",
            height = 550,
            width = 800,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        self.background_img = PhotoImage(file = f"images/bg_sesion.png")
        background = self.canvas.create_image(400.0, 275.0,image=self.background_img)

        self.entry0_img = PhotoImage(file = f"images/img_textBox0.png")

        entry0_bg = self.canvas.create_image(400.0, 220.0,image = self.entry0_img)

        self.nombreIn = Entry(bd = 0,bg = "#c4c4c4",highlightthickness = 0, font = ("Tahoma", 14))
        self.nombreIn.place(x = 320.0, y = 200,width = 160.0,height = 38)
        #self.nombreIn.bind("<Key>", self.key)
        self.nombreIn.bind("<FocusIn>", self.focus)
        self.nombreIn.bind("<FocusOut>", self.sinfocus)

        entry1_bg = self.canvas.create_image(400.0, 315.0,image = self.entry0_img)

        self.passwordIn = Entry(bd = 0,show="•",bg = "#c4c4c4",highlightthickness = 0,font = ("Tahoma", 14))
        self.passwordIn.place(x = 320.0, y = 295,width = 160.0,height = 38)
        #self.passwordIn.bind("<Key>", self.key)
        self.passwordIn.bind("<FocusIn>", self.focus)
        self.passwordIn.bind("<FocusOut>", self.sinfocus)

        #--------------------------Boton---------------------------
        btn_inactive=Image.open(f"images/img1.png")
        btn_active=Image.open(f"images/img0.png")
        self.window.btn_inactive = ImageTk.PhotoImage(btn_inactive)
        self.window.btn_active = ImageTk.PhotoImage(btn_active)

        self.img0 = PhotoImage(file = f"images/img0.png")
        self.b0 = Button(self.window,image=self.window.btn_inactive, activebackground="white",bg="white",borderwidth = 0, highlightthickness = 0,curso="hand2", relief = "flat")
        self.b0.place(x = 300, y = 411,  width = 200, height = 55)
        self.b0.bind("<Enter>",self.on_enter)
        self.b0.bind("<Leave>",self.on_leave)
        self.b0.bind("<ButtonRelease-1>",self.ingreso)

    
    #///////////---------------Funciones visuales--------------//////////////////////////////
    def on_enter(self,event):
            self.b0.config(image=self.window.btn_active)

    def on_leave(self,event):
            self.b0.config(image=self.window.btn_inactive)

    def clear_entry(self, event):
        if event.widget == self.nombreIn:
            self.text1.set("")
        elif event.widget == self.passwordIn:
            self.text2.set("")

    def focus(self, event):
        if event.widget == self.b0:
            self.passwordIn.configure(state = "active")
        else:
            event.widget.configure(foreground = "white")

    def sinfocus(self, event):
        if event.widget == self.b0:
            self.passwordIn.configure(state = "normal")
        else:
            event.widget.configure(foreground = "black")

    def ingreso(self,event):
        NombreUsuarioAdmin = "admin"
        PasswordAdmin = "001"
        if self.nombreIn.get() != "" and self.passwordIn.get() != "":
            if NombreUsuarioAdmin == self.nombreIn.get() and PasswordAdmin == self.passwordIn.get():
                messagebox.showinfo("Bienvenida", f"Bienvenido {self.nombreIn.get()}")
                self.window.destroy()
                window=ThemedTk(theme="adapta")
                entrar_menu=Interfaz(window)
                window.mainloop()
            else:
                messagebox.showinfo("Error", "Usuario o contraseña incorrectos.")
        else:
            messagebox.showinfo("Error", f"Se deben llenar todos los campos")

if __name__ =="__main__":
    window=ThemedTk(theme="adapta")
    iniciar_sesion=Login(window,"Iniciar sesión",800,550)
    window.mainloop()