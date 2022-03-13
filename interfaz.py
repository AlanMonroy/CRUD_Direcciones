from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk

class Interfaz:
	def __init__(self, window):
		self.window = window
		self.conteo_menu = 0
		self.x = 0; self.y = 0
		self.w, self.h = self.window.winfo_screenwidth(), self.window.winfo_screenheight() 
		self.window.geometry("%dx%d+%d+%d" % (self.w, self.h, self.x, self.y))
		self.window.state("zoomed")

		self.menu()

	#Enlaces para acceder a las pantallas
	def regresar_menu(self):
		self.conteo_menu=0
		self.mainFrame.destroy()
		self.menu()

	def ir_pantalla(self, event):
		self.conteo_menu=0
		match event.widget:
			case self.boton1 | self.boton_desplegable1: 
				self.mainFrame.destroy()
				self.opcion1()

			case self.boton2: 
				self.mainFrame.destroy()
				self.menu()

	#Menu desplegable
	def menu_desplegable(self):
		self.conteo_menu += 1
		if self.conteo_menu %2 == 0:
			self.desplegable.destroy()
		else:
			self.desplegable=Frame(self.window, bg="black")
			self.desplegable.place(x=0,y=69)

			canvas = Canvas(self.desplegable)
			canvas.pack(side=LEFT,fill=BOTH, expand=1)

			#Frame horizontal de la interfaz (color negro)
			tercerFrame = Frame(canvas, bg="black", width=250)
			tercerFrame.grid(row=0,column=0, sticky="e")

			#ttk.Style().configure("TButton", padding=6, relief="flat",background="black")
			self.boton_desplegable1 = ttk.Button(canvas, text=f"Opcion1")
			self.boton_desplegable1.grid(row=1,column=0, padx=10, pady=10)
			self.boton_desplegable1.bind("<Button-1>", self.ir_pantalla)

			self.boton_desplegable2 = ttk.Button(canvas, text=f"Opcion1")
			self.boton_desplegable2.grid(row=2,column=0, padx=10, pady=10)
			self.boton_desplegable2.bind("<Button-1>", self.ir_pantalla)

			self.boton_desplegable3 = ttk.Button(canvas, text=f"Opcion1")
			self.boton_desplegable3.grid(row=3,column=0, padx=10, pady=10)
			self.boton_desplegable3.bind("<Button-1>", self.ir_pantalla)

	#Pantalla MENU
	def menu(self):
		self.window.title("Menú")
		self.mainFrame=Frame(self.window)
		self.mainFrame.pack(fill=BOTH, expand=True)

		canvas = Canvas(self.mainFrame)
		canvas.pack(side=LEFT,fill=BOTH, expand=1)

		scrollbar = ttk.Scrollbar(self.mainFrame, orient=VERTICAL, command=canvas.yview)
		scrollbar.pack(side=RIGHT, fill=Y)

		canvas.configure(yscrollcommand=scrollbar.set)
		canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion = canvas.bbox("all")))

		secondFrame = ttk.Frame(canvas)
		canvas.create_window((0,0), window=secondFrame, anchor="nw")

		#Frame horizontal de la interfaz (color negro)
		tercerFrame = Frame(secondFrame, bg="black", width=self.w, height=70)
		tercerFrame.grid(row=0,column=0,columnspan=self.w, sticky="e")
		#Frame vertical
		cuartoFrame = Frame(secondFrame, bg="black", height=self.h)
		cuartoFrame.grid(row=1,column=0,rowspan=self.h)

		#label1 = Label(tercerFrame,text="Menú").pack()
		self.img0 = PhotoImage(file = f"images/barra_menu.png")
		self.boton_menu = Button(secondFrame,
            image = self.img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.menu_desplegable,
            relief = "flat", activebackground="black", bg="black", curso="hand2")
		self.boton_menu.grid(row=0,column=1)

		self.boton1 = ttk.Button(secondFrame, text=f"Opcion1")
		self.boton1.grid(row=1,column=1, padx=10, pady=10)
		self.boton1.bind("<Button-1>", self.ir_pantalla)

		def pop_menu(event):
			menu.tk_popup(event.x_root,event.y_root)

		#Seccion de diseño
		estilo=ttk.Style()
		estilo.configure("d.TFrame",background="white",borderwidth=2,relief="ridge")
		frame_dis =ttk.Frame(secondFrame,style="d.TFrame",width=self.w*.80,height=self.h*.70)
		frame_dis.grid(row=1,column=2,columnspan=self.w, rowspan=self.h, sticky="n",pady=30,padx=5)

		menu = Menu(frame_dis, tearoff=0, bg="black", fg="white")
		menu.add_command(label="Copy")
		menu.add_command(label="Cut")
		menu.add_separator()
		menu.add_command(label="Paste")
		menu.add_command(label="Select all")

		frame_dis.bind("<Button-3>", pop_menu)


	#Pantalla Opcion1
	def opcion1(self):
		self.window.title("Opcion1")
		self.mainFrame=Frame(self.window)
		self.mainFrame.pack(fill=BOTH, expand=1)

		canvas = Canvas(self.mainFrame)
		canvas.pack(side=LEFT,fill=BOTH, expand=1)

		scrollbar = ttk.Scrollbar(self.mainFrame, orient=VERTICAL, command=canvas.yview)
		scrollbar.pack(side=RIGHT, fill=Y)

		canvas.configure(yscrollcommand=scrollbar.set)
		canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion = canvas.bbox("all")))

		secondFrame = ttk.Frame(canvas)
		canvas.create_window((0,0), window=secondFrame, anchor="nw")

		for i in range(5):
			ttk.Button(secondFrame, text=f"boton {i}").grid(row=i+1,column=1, padx=10, pady=10)

		#Frame horizontal de la interfaz (color negro)
		tercerFrame = Frame(secondFrame, bg="black", width=self.w, height=70)
		tercerFrame.grid(row=0,column=0,columnspan=self.w, sticky="e")

		cuartoFrame = Frame(secondFrame, bg="white", height=self.h)
		cuartoFrame.grid(row=1,column=0,rowspan=self.h)
		
		#Button(tercerFrame, text="boton").pack()
		label = Label(secondFrame,text="Label", bg="black",foreground="white").grid(row=99, column=3)

		self.boton2 = ttk.Button(secondFrame, text=f"Regresar", command=self.regresar_menu)
		self.boton2.grid(row=5,column=1, padx=10, pady=10)
		self.boton2.bind("<Button-1>", self.ir_pantalla)

if __name__ == "__main__":
	window=ThemedTk(theme="adapta")
	entrar_menu=Interfaz(window)
	window.mainloop()