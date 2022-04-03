from tkinter import *
from tkinter import ttk, messagebox
from ttkthemes import ThemedTk
from info_conexion import info
import pyodbc

class Interfaz:
	def __init__(self, window):
		self.window = window
		self.conteo_menu = 0  #Importante, no que hace exactamente pero es para control de pantallas
		self.x = 0; self.y = 0
		self.w, self.h = self.window.winfo_screenwidth(), self.window.winfo_screenheight() 
		self.window.geometry("%dx%d+%d+%d" % (self.w, self.h, self.x, self.y))
		self.window.state("zoomed")
		self.window.iconbitmap('images/icono.ico')

		self.menu()

	#Enlaces para acceder a las pantallas
	def regresar_menu(self):
		self.conteo_menu=0
		self.mainFrame.destroy()
		self.menu()

	def ir_pantalla(self, event):
		self.conteo_menu=0
		match event.widget:
			case self.boton_desplegable1: 
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

		#secondFrame.columnconfigure(0, weight=1)
		#secondFrame.rowconfigure(0, weight=1)

		#label1 = Label(tercerFrame,text="Menú").pack()
		self.img0 = PhotoImage(file = f"images/barra_menu.png")
		self.boton_menu = Button(secondFrame,
            image = self.img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.menu_desplegable,
            relief = "flat", activebackground="black", bg="black", curso="hand2")
		self.boton_menu.grid(row=0,column=1)

		self.boton_registrar_001 = ttk.Button(secondFrame, text=f"Registrar")
		self.boton_registrar_001.grid(row=1,column=1, padx=10, pady=10)
		self.boton_registrar_001.bind("<Button-1>", self.pantalla_registro)

		self.img_ButtonEditar = PhotoImage(file = f"images/img_editar.png") #Boton editar
		self.ButtonEditar = Button(secondFrame,
			image = self.img_ButtonEditar, curso= "hand2",
			borderwidth = 0,highlightthickness = 0, relief = "flat", bg="white", activebackground="white")
		self.ButtonEditar.grid(row=2,column=1, padx=10, pady=10)
		self.ButtonEditar.bind("<Button-1>", self.pantalla_registro)

		self.img_ButtonEliminarRegistro = PhotoImage(file = f"images/img_eliminar.png") #Boton Eliminar
		self.ButtonEliminarRegistro = Button(secondFrame,
			image = self.img_ButtonEliminarRegistro, command=self.eliminar_registro, curso= "hand2",
			borderwidth = 0, highlightthickness = 0, relief = "flat", bg="white", activebackground="white")
		self.ButtonEliminarRegistro.grid(row=3,column=1, padx=10, pady=10)

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

		self.tabla.grid(row=2,column=2,rowspan=self.h, sticky="n")

		self.leer_info()

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

	#Pantalla TopLevel Registro	
	def pantalla_registro(self, event):
		self.top=Toplevel()
		self.top.grab_set()
		self.top.transient(master=None)
		self.top.resizable(False, True)
		self.top.geometry("450x350")
		self.top.configure(bg = "#ffffff")
		self.canvas = Canvas(
		    self.top,
		    bg = "#ffffff",
		    height = 350,
		    width = 450,
		    bd = 0,
		    highlightthickness = 0,
		    relief = "ridge")
		self.canvas.place(x = 0, y = 0)

		self.background_img01 = PhotoImage(file = f"images/background.png")
		background = self.canvas.create_image(225.0, 175.0,image=self.background_img01)

		self.entry0_img = PhotoImage(file = f"images/img_textBox1.png")

		entry4_bg = self.canvas.create_image(294.5, 34.5,image = self.entry0_img)
		self.registrar_nombre = Entry(self.top,bd = 0,bg = "#ffffff",highlightthickness = 0)
		self.registrar_nombre.place(x = 189.0, y = 24,width = 211.0,height = 23)

		entry5_bg = self.canvas.create_image(294.5, 74.5,image = self.entry0_img)
		self.registrar_telefono = Entry(self.top,bd = 0,bg = "#ffffff",highlightthickness = 0)
		self.registrar_telefono.place(x = 189.0, y = 64,width = 211.0,height = 23)

		entry3_bg = self.canvas.create_image(294.5, 114.5,image = self.entry0_img)
		self.registrar_sucursal = Entry(self.top,bd = 0,bg = "#ffffff",highlightthickness = 0)
		self.registrar_sucursal.place(x = 189.0, y = 104,width = 211.0,height = 23)

		entry0_bg = self.canvas.create_image(294.5, 154.5,image = self.entry0_img)
		self.registrar_fecha = Entry(self.top,bd = 0,bg = "#ffffff",highlightthickness = 0)
		self.registrar_fecha.place(x = 189.0, y = 144,width = 211.0,height = 23)

		entry1_bg = self.canvas.create_image(294.5, 194.5,image = self.entry0_img)
		self.registrar_supervisor = Entry(self.top,bd = 0,bg = "#ffffff",highlightthickness = 0)
		self.registrar_supervisor.place(x = 189.0, y = 184,width = 211.0,height = 23)

		entry2_bg = self.canvas.create_image(294.5, 236.5,image = self.entry0_img)
		self.registrar_gerente = Entry(self.top,bd = 0,bg = "#ffffff",highlightthickness = 0)
		self.registrar_gerente.place(x = 189.0, y = 224,width = 211.0,height = 23)

		match event.widget:
			case self.boton_registrar_001:
				self.top.title("Registrar")
				self.img01 = PhotoImage(file = f"images/r1.png")
				self.b_r001 = Button(self.top,image = self.img01,borderwidth = 0,highlightthickness = 0,relief = "flat",bg="#E5E4E4",
				    activebackground="#E5E4E4", cursor="hand2")
				self.b_r001.place(x = 50, y = 297,width = 140,height = 28)
				self.b_r001.bind("<Button-1>", self.registrar)

				self.img11 = PhotoImage(file = f"images/r2.png")
				self.b_r002 = Button(self.top,image = self.img11,borderwidth = 0,highlightthickness = 0,relief = "flat",bg="#E5E4E4",
				    activebackground="#E5E4E4", cursor="hand2")
				self.b_r002.place(x = 260, y = 297,width = 140,height = 28)
				self.b_r002.bind("<Button-1>", self.registrar)

			case self.ButtonEditar:
				self.top.title("Editar")
				self.img21 = PhotoImage(file = f"images/r3.png")
				self.b_actualizar = Button(self.top,image = self.img21,borderwidth = 0,highlightthickness = 0,relief = "flat",bg="#E5E4E4",
					activebackground="#E5E4E4", cursor="hand2")
				self.b_actualizar.place(x = 155, y = 297,width = 140,height = 28)

#Funciones
	def leer_info(self):
		self.tabla.delete(*self.tabla.get_children())
		objeto=info()
		data = objeto.orden_nombres()

		if len(data) !=0:
			for i in data:
				self.tabla.insert(parent="",index="end", text="", values=(i[1],
					i[2],i[3],i[4],i[5],i[6]))

	def registrar(self, event):
		if self.registrar_nombre.get() != "" and self.registrar_telefono.get() !="" and self.registrar_sucursal != "" and self.registrar_fecha.get() != "" and self.registrar_supervisor.get() != "" and self.registrar_gerente.get() != 0:
			objeto=info()
			compromar_001 = objeto.checar_nombre(self.registrar_nombre.get())
			if compromar_001:
				messagebox.showinfo("Error","El empleado ya esta registrado en la base de datos.")
			else:
				objeto.agregar_elementos(self.registrar_nombre.get(),self.registrar_telefono.get(),
					self.registrar_sucursal.get(),self.registrar_fecha.get(),
					self.registrar_supervisor.get(),self.registrar_gerente.get())

				self.registrar_nombre.delete(0, END); self.registrar_telefono.delete(0, END)
				self.registrar_sucursal.delete(0, END); self.registrar_fecha.delete(0, END)
				self.registrar_supervisor.delete(0, END); self.registrar_gerente.delete(0, END)
				messagebox.showinfo("Completado","Actualizacion de datos  completada.")
				self.leer_info()
		else:
			messagebox.showinfo("Error","Debe llenar todos los apartados.")

		match event.widget:
			case self.b_r001:
				self.top.destroy()
			case self.b_r002:
				pass

	def eliminar_registro(self):
		seleccion = self.tabla.focus()
		values = self.tabla.item(seleccion,"values")

		if values =="":
			messagebox.showinfo("Error","No ha seleccionado un registro")
		else:
			decision2=messagebox.askquestion("Confirmar","¿Seguro que quieres eliminar el registro?")
			if decision2 == "yes":
				valor_eliminar = values[0]
				objeto=info()
				objeto.eliminar(valor_eliminar)
				messagebox.showinfo("Completado","Registro eliminado.")
				self.leer_info()


if __name__ == "__main__":
	window=ThemedTk(theme="adapta")
	entrar_menu=Interfaz(window)
	window.mainloop()