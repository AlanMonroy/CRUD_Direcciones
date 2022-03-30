from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
from leer_json import leer

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
			self.boton_desplegable1 = ttk.Button(canvas, text=f"Registrar")
			self.boton_desplegable1.grid(row=1,column=0, padx=10, pady=10)
			self.boton_desplegable1.bind("<Button-1>", self.ir_pantalla)

			self.boton_desplegable2 = ttk.Button(canvas, text=f"leer_info", command=self.leer_info)
			self.boton_desplegable2.grid(row=2,column=0, padx=10, pady=10)
			#self.boton_desplegable2.bind("<Button-1>", self.ir_pantalla)

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

		self.boton1 = ttk.Button(secondFrame, text=f"Registrar", command=self.pantalla_registro)
		self.boton1.grid(row=1,column=1, padx=10, pady=10)

		#--------------------------------------Tabla------------------------------------------------------------#
		style = ttk.Style()
		style.configure("Treeview")
		style.map("Treeview", background=[("selected","#38022D")])

		self.tabla = ttk.Treeview(secondFrame)
		self.tabla["columns"] = ("Nombre de empleado","Teléfono","Sucursal","Fecha de ingreso","Supervisor","Gerente")
		self.tabla.column("#0",width=0,stretch=NO)
		self.tabla.column("Nombre de empleado",anchor=CENTER,width=200)
		self.tabla.column("Teléfono",anchor=CENTER,width=100)
		self.tabla.column("Sucursal",anchor=CENTER,width=200)
		self.tabla.column("Fecha de ingreso",anchor=CENTER,width=200)
		self.tabla.column("Supervisor",anchor=CENTER,width=200)
		self.tabla.column("Gerente",anchor=CENTER,width=200)

		self.tabla.heading("#0",text="",anchor=CENTER)
		self.tabla.heading("Nombre de empleado",text="Nombre de empleado",anchor=CENTER)
		self.tabla.heading("Teléfono",text="Teléfono",anchor=CENTER)
		self.tabla.heading("Sucursal",text="Sucursal",anchor=CENTER)
		self.tabla.heading("Fecha de ingreso",text="Fecha de ingreso",anchor=CENTER)
		self.tabla.heading("Supervisor",text="Supervisor",anchor=CENTER)
		self.tabla.heading("Gerente",text="Gerente",anchor=CENTER)

		self.tabla.grid(row=2,column=2,padx=20,pady=20,rowspan=self.h, sticky="n")

		self.leer_info()

		"""def pop_menu(event):
			menu.tk_popup(event.x_root,event.y_root)

		#Seccion de diseño (cuadro de diseño)
		estilo=ttk.Style()
		estilo.configure("d.TFrame",background="white",borderwidth=2,relief="ridge")
		self.frame_dis =ttk.Frame(secondFrame,style="d.TFrame",width=self.w*.80,height=self.h*.70)
		self.frame_dis.grid(row=1,column=2,columnspan=self.w, rowspan=self.h, sticky="n",pady=30,padx=5)
		self.frame_dis.grid_propagate(False)
		#self.canvas_div = Frame(frame_dis)
		#self.canvas_div.pack()

		menu = Menu(self.frame_dis, tearoff=0, bg="black", fg="white")
		menu.add_command(label="Agregar", command=self.agregar)
		menu.add_command(label="Copy")
		menu.add_command(label="Cut")
		menu.add_separator()
		menu.add_command(label="Paste")
		menu.add_command(label="Select all")

		self.frame_dis.bind("<Button-3>", pop_menu)"""


	#Pantalla Opcion1
	def opcion1(self):
		self.window.title("Registro")
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

	def pantalla_registro(self):
		self.top=Toplevel()
		self.top.grab_set()
		self.top.transient(master=None)
		self.top.title("Registrar")
		self.top.resizable(False, True)
		self.top.configure(bg="#ECE7EB")

		estilo = ttk.Style()
		estilo.configure("1.TLabel",foreground="black",font = ("Tahoma", 12),background="#ECE7EB")
		label1 = ttk.Label(self.top,text="Nombre de empleado",style="1.TLabel").grid(row=0, column=0,padx=10,pady=10)
		self.registrar_nombre = ttk.Entry(self.top, style="d.TEntry", width=40)
		self.registrar_nombre.grid(row=0,column=1, padx=10,pady=10)

		label2 = ttk.Label(self.top,text="Teléfono",style="1.TLabel").grid(row=1, column=0,padx=10,pady=10)
		self.registrar_telefono = ttk.Entry(self.top, style="d.TEntry", width=40)
		self.registrar_telefono.grid(row=1,column=1, padx=10,pady=10)

		label3 = ttk.Label(self.top,text="Sucursal",style="1.TLabel").grid(row=2, column=0,padx=10,pady=10)
		self.registrar_sucursal = ttk.Entry(self.top, style="d.TEntry", width=40)
		self.registrar_sucursal.grid(row=2,column=1, padx=10,pady=10)

		label4 = ttk.Label(self.top,text="Fecha de ingreso",style="1.TLabel").grid(row=3, column=0,padx=10,pady=10)
		self.registrar_fecha = ttk.Entry(self.top, style="d.TEntry", width=40)
		self.registrar_fecha.grid(row=3,column=1, padx=10,pady=10)

		label5 = ttk.Label(self.top,text="Supervisor",style="1.TLabel").grid(row=4, column=0,padx=10,pady=10)
		self.registrar_supervisor = ttk.Entry(self.top, style="d.TEntry", width=40)
		self.registrar_supervisor.grid(row=4,column=1, padx=10,pady=10)

		label6 = ttk.Label(self.top,text="Gerente",style="1.TLabel").grid(row=5, column=0,padx=10,pady=10)
		self.registrar_gerente = ttk.Entry(self.top, style="d.TEntry", width=40)
		self.registrar_gerente.grid(row=5,column=1, padx=10,pady=10)

		sep = ttk.Separator(self.top,orient="horizontal")
		sep.grid(row=6,column=0,columnspan=2, padx=20, sticky="ew")

		boton1 = ttk.Button(self.top, text="Registrar y terminar")
		boton1.grid(row=7,column=0, padx=10, pady=10)

		boton2 = ttk.Button(self.top, text="Continuar registrando")
		boton2.grid(row=7,column=1, padx=10, pady=10)

	def leer_info(self):
		objeto=leer()
		data = objeto.ordernar_por_nombre()

		if len(data) != 0:
			for i in data:
				self.tabla.insert(parent="",index="end", text="", values=(i["nombre"],i["telefono"],
					i["sucursal"],i["fecha_ingreso"],i["supervisor"],i["gerente"]))


if __name__ == "__main__":
	window=ThemedTk(theme="adapta")
	entrar_menu=Interfaz(window)
	window.mainloop()