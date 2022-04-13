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
			self.desplegable=Frame(self.window, bg="white")
			self.desplegable.place(x=0,y=69)

			canvas = Canvas(self.desplegable)
			canvas.pack(side=LEFT,fill=BOTH, expand=1)

			#Frame horizontal de la interfaz (color negro)
			tercerFrame = Frame(canvas, bg="black", width=250)
			tercerFrame.grid(row=0,column=0, sticky="e")

			boton_desplegable1 = ttk.Button(canvas, text=f"No disponible")
			boton_desplegable1.grid(row=1,column=0, padx=50, pady=10)
			#self.boton_desplegable1.bind("<Button-1>", self.ir_pantalla)

			boton_desplegable2 = ttk.Button(canvas, text=f"No disponible")
			boton_desplegable2.grid(row=2,column=0, padx=50, pady=10)
			#self.boton_desplegable2.bind("<Button-1>", self.ir_pantalla)

			boton_desplegable3 = ttk.Button(canvas, text=f"No disponible")
			boton_desplegable3.grid(row=3,column=0, padx=50, pady=10)
			boton_desplegable3.bind("<Button-1>", self.ir_pantalla)

	#Pantalla MENU
	def menu(self):
		self.window.title("Menú")
		self.mainFrame=Frame(self.window)
		self.mainFrame.pack(fill=BOTH, expand=True)

		canvas = Canvas(self.mainFrame)
		canvas.pack(side=LEFT,fill=BOTH, expand=1)

		"""scrollbar = ttk.Scrollbar(self.mainFrame, orient=VERTICAL, command=canvas.yview)
		scrollbar.pack(side=RIGHT, fill=Y)

		canvas.configure(yscrollcommand=scrollbar.set)
		canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion = canvas.bbox("all")))"""

		secondFrame = ttk.Frame(canvas)
		canvas.create_window((0,0), window=secondFrame, anchor="nw")

		#Frame horizontal de la interfaz (color negro)
		tercerFrame = Frame(secondFrame, bg="black", width=self.w, height=70)
		tercerFrame.grid(row=0,column=0,columnspan=self.w, sticky="e")
		#Frame vertical
		cuartoFrame = Frame(secondFrame, bg="black", height=self.h)
		cuartoFrame.grid(row=1,column=0,rowspan=self.h)

		#Frame separator
		quintoFrame = Frame(secondFrame, bg="#E5E4E4", height=self.h, width=2)
		quintoFrame.grid(row=1,column=2,rowspan=self.h)

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

		#self.b_buscar_001 = ttk.Button(secondFrame, text=f"Buscar", command=self.buscar)
		#self.b_buscar_001.grid(row=1,column=4, padx=10, pady=10)

		self.buscador = ttk.Entry(secondFrame, width=50)
		self.buscador.grid(row=1,column=3, padx=20,pady=10)
		self.buscador.bind("<KeyRelease>",self.buscar)

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

		self.boton_exportar = ttk.Button(secondFrame, text=f"Exportar a Excel",command=self.exportar0)
		self.boton_exportar.grid(row=4,column=1, padx=10, pady=10)

		#--------------------------------------Tabla------------------------------------------------------------#
		style = ttk.Style()
		style.configure("Treeview")
		style.map("Treeview", background=[("selected","#38022D")])

		self.tabla = ttk.Treeview(secondFrame, height=20)
		self.tabla["columns"] = ("ID","No. Empleado","Nombre de empleado","Teléfono","Zona","Sucursal","Fecha de ingreso","Supervisor","Gerente")
		self.tabla.column("#0",width=0,stretch=NO)
		self.tabla.column("ID",anchor=CENTER,width=30)
		self.tabla.column("No. Empleado",anchor=CENTER,width=80)
		self.tabla.column("Nombre de empleado",anchor=CENTER,width=200)
		self.tabla.column("Teléfono",anchor=CENTER,width=100)
		self.tabla.column("Zona",anchor=CENTER,width=100)
		self.tabla.column("Sucursal",anchor=CENTER,width=120)
		self.tabla.column("Fecha de ingreso",anchor=CENTER,width=100)
		self.tabla.column("Supervisor",anchor=CENTER,width=210)
		self.tabla.column("Gerente",anchor=CENTER,width=210)

		self.tabla.heading("#0",text="",anchor=CENTER)
		self.tabla.heading("ID",text="ID",anchor=CENTER)
		self.tabla.heading("No. Empleado",text="No. Empleado",anchor=CENTER)
		self.tabla.heading("Nombre de empleado",text="Nombre de empleado",anchor=CENTER)
		self.tabla.heading("Teléfono",text="Teléfono",anchor=CENTER)
		self.tabla.heading("Zona",text="Zona",anchor=CENTER)
		self.tabla.heading("Sucursal",text="Sucursal",anchor=CENTER)
		self.tabla.heading("Fecha de ingreso",text="Fecha de ingreso",anchor=CENTER)
		self.tabla.heading("Supervisor",text="Supervisor",anchor=CENTER)
		self.tabla.heading("Gerente",text="Gerente",anchor=CENTER)

		self.tabla.grid(row=2,column=3,rowspan=self.h, columnspan=self.w,sticky="nw",padx=10)

		self.scrollvert=Scrollbar(secondFrame,command=self.tabla.yview)
		self.scrollvert.place(in_=self.tabla,relx=1, relheight=1, bordermode="outside")
		self.tabla.config(yscrollcommand=self.scrollvert.set)

		self.leer_info()

	#Pantalla Opcion1
	def opcion1(self): #No sirve, solo crea una nueva pagina
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
		self.boton_registrar_001.focus()
		self.top=Toplevel()
		self.top.grab_set()
		self.top.transient(master=None)
		self.top.resizable(False, True)
		self.top.geometry("450x400")
		self.top.configure(bg = "#ffffff")
		self.canvas = Canvas(self.top,bg = "#ffffff",height = 400,width = 450,bd = 0,highlightthickness = 0,relief = "ridge")
		self.canvas.place(x = 0, y = 0)

		self.background_img01 = PhotoImage(file = f"images/background.png")
		background = self.canvas.create_image(225.0, 200.0,image=self.background_img01)

		self.entry0_img = PhotoImage(file = f"images/img_textBox1.png")

		entry0_bg = self.canvas.create_image(294.5, 34.5,image = self.entry0_img)
		self.registrar_numero = Entry(self.top,bd = 0,bg = "#ffffff",highlightthickness = 0)
		self.registrar_numero.place(x = 189.0, y = 24,width = 211.0,height = 23)
		self.registrar_numero.bind("<Key>",self.mover)
		self.registrar_numero.focus()

		entry1_bg = self.canvas.create_image(294.5, 74.5,image = self.entry0_img)
		self.registrar_nombre = Entry(self.top,bd = 0,bg = "#ffffff",highlightthickness = 0)
		self.registrar_nombre.place(x = 189.0, y = 64,width = 211.0,height = 23)
		self.registrar_nombre.bind("<Key>",self.mover)

		entry2_bg = self.canvas.create_image(294.5, 114.5,image = self.entry0_img)
		self.registrar_telefono = Entry(self.top,bd = 0,bg = "#ffffff",highlightthickness = 0)
		self.registrar_telefono.place(x = 189.0, y = 104,width = 211.0,height = 23)
		self.registrar_telefono.bind("<Key>",self.mover)

		entry3_bg = self.canvas.create_image(294.5, 154.5,image = self.entry0_img)
		self.registrar_zona = Entry(self.top,bd = 0,bg = "#ffffff",highlightthickness = 0)
		self.registrar_zona.place(x = 189.0, y = 144,width = 211.0,height = 23)
		self.registrar_zona.bind("<Key>",self.mover)

		entry4_bg = self.canvas.create_image(294.5, 194.5,image = self.entry0_img)
		self.registrar_sucursal = Entry(self.top,bd = 0,bg = "#ffffff",highlightthickness = 0)
		self.registrar_sucursal.place(x = 189.0, y = 184,width = 211.0,height = 23)
		self.registrar_sucursal.bind("<Key>",self.mover)

		entry5_bg = self.canvas.create_image(294.5, 234.5,image = self.entry0_img)
		self.registrar_fecha = Entry(self.top,bd = 0,bg = "#ffffff",highlightthickness = 0)
		self.registrar_fecha.place(x = 189.0, y = 224,width = 211.0,height = 23)
		self.registrar_fecha.bind("<Key>",self.mover)

		entry6_bg = self.canvas.create_image(294.5, 274.5,image = self.entry0_img)
		self.registrar_supervisor = Entry(self.top,bd = 0,bg = "#ffffff",highlightthickness = 0)
		self.registrar_supervisor.place(x = 189.0, y = 264,width = 211.0,height = 23)
		self.registrar_supervisor.bind("<Key>",self.mover)

		entry7_bg = self.canvas.create_image(294.5, 314.5,image = self.entry0_img)
		self.registrar_gerente = Entry(self.top,bd = 0,bg = "#ffffff",highlightthickness = 0)
		self.registrar_gerente.place(x = 189.0, y = 304,width = 211.0,height = 23)
		self.registrar_gerente.bind("<Key>",self.mover)

		match event.widget:
			case self.boton_registrar_001:
				self.top.title("Registrar")
				self.top.bind("<Return>",self.registrar)

				self.img01 = PhotoImage(file = f"images/r1.png")
				self.b_r001 = Button(self.top,image = self.img01,borderwidth = 0,highlightthickness = 0,relief = "flat",bg="#E5E4E4",
				    activebackground="#E5E4E4", cursor="hand2")
				self.b_r001.place(x = 50, y = 348,width = 140,height = 28)
				self.b_r001.bind("<Button-1>", self.registrar)

				self.img11 = PhotoImage(file = f"images/r2.png")
				self.b_r002 = Button(self.top,image = self.img11,borderwidth = 0,highlightthickness = 0,relief = "flat",bg="#E5E4E4",
				    activebackground="#E5E4E4", cursor="hand2")
				self.b_r002.place(x = 260, y = 348,width = 140,height = 28)
				self.b_r002.bind("<Button-1>", self.registrar)

			case self.ButtonEditar:
				self.top.title("Editar")
				self.top.bind("<Return>",self.actualizar)

				self.img21 = PhotoImage(file = f"images/r3.png")
				self.b_actualizar = Button(self.top,image = self.img21,borderwidth = 0,highlightthickness = 0,relief = "flat",bg="#E5E4E4",
					activebackground="#E5E4E4", cursor="hand2", command=self.actualizar)
				self.b_actualizar.place(x = 155, y = 348,width = 140,height = 28)

				seleccion = self.tabla.focus()
				values = self.tabla.item(seleccion,"values")

				if values =="":
					self.top.destroy()
					messagebox.showinfo("Error","No ha seleccionado un registro")
				else:
					self._valor_id=values[0]
					self.registrar_numero.insert(END,values[1])
					self.registrar_nombre.insert(END,values[2])
					self.registrar_telefono.insert(END,values[3])
					self.registrar_zona.insert(END,values[4])
					self.registrar_sucursal.insert(END,values[5])
					self.registrar_fecha.insert(END,values[6])
					self.registrar_supervisor.insert(END,values[7])
					self.registrar_gerente.insert(END,values[8])

#Funciones
	def exportar0(self):
		objeto=info()
		objeto.exportar_archivo()

	def mover(self, event):
		widgets=[self.registrar_numero,self.registrar_nombre,self.registrar_telefono,self.registrar_zona,self.registrar_sucursal,
		self.registrar_fecha,self.registrar_supervisor, self.registrar_gerente]
		if event.keysym == "Down":
			try:
				x=widgets.index(event.widget)
				c=widgets[x+1]
				c.focus()
			except IndexError:
				pass
		elif event.keysym == "Up":
			try:
				x=widgets.index(event.widget)
				c=widgets[x-1]
				c.focus()
			except IndexError:
				pass


	def buscar(self, event):
		objeto=info()
		self.tabla.delete(*self.tabla.get_children())
		data = objeto.buscar(self.buscador.get())

		if len(data) !=0:
			for i in data:
				self.tabla.insert(parent="",index="end", text="", values=(i[0],i[1],
					i[2],i[3],i[4],i[5],i[6],i[7],i[8]))

	def leer_info(self):  #Leer la base de datos y actualizar el treeview
		self.tabla.delete(*self.tabla.get_children())
		objeto=info()
		data = objeto.orden_nombres()

		if len(data) !=0:
			for i in data:
				self.tabla.insert(parent="",index="end", text="", values=(i[0],i[1],
					i[2],i[3],i[4],i[5],i[6],i[7],i[8]))

	def registrar(self, event): #Realiza el registro hacia la base de datos
		if self.registrar_nombre.get() != "" and self.registrar_telefono.get() !="" and self.registrar_sucursal != "" and self.registrar_fecha.get() != "" and self.registrar_supervisor.get() != "" and self.registrar_gerente.get() != "" and self.registrar_numero.get() != "" and self.registrar_zona.get() != "":
			objeto=info()
			compromar_001 = objeto.checar_nombre(self.registrar_numero.get(),self.registrar_nombre.get())
			if compromar_001:
				messagebox.showinfo("Error","El empleado ya esta registrado en la base de datos.")
			else:
				objeto.agregar_elementos(self.registrar_numero.get(),self.registrar_nombre.get(),self.registrar_telefono.get(),
					self.registrar_zona.get(),self.registrar_sucursal.get(),self.registrar_fecha.get(),
					self.registrar_supervisor.get(),self.registrar_gerente.get())

				self.registrar_nombre.delete(0, END); self.registrar_telefono.delete(0, END)
				self.registrar_sucursal.delete(0, END); self.registrar_fecha.delete(0, END)
				self.registrar_supervisor.delete(0, END); self.registrar_gerente.delete(0, END)
				self.registrar_numero.delete(0,END); self.registrar_zona.delete(0,END)
				messagebox.showinfo("Completado","Registro de datos completado.")
				self.leer_info()
		else:
			messagebox.showinfo("Error","Debe llenar todos los apartados.")

		match event.widget:
			case self.b_r001: #En el caso de que solo quiera registrar y cerrar
				self.top.destroy()
			case self.b_r002: #En el caso de que quiera continuar registrando
				pass

	def eliminar_registro(self): #Elimina registro
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
				
	def actualizar(self, event=0): #Realiza la actualizacion de datos
		seleccion = self.tabla.focus()
		values = self.tabla.item(seleccion,"values")
		if self.registrar_nombre.get() != "" and self.registrar_telefono.get() !="" and self.registrar_sucursal != "" and self.registrar_fecha.get() != "" and self.registrar_supervisor.get() != "" and self.registrar_gerente.get() != "" and self.registrar_numero.get() != "" and self.registrar_zona.get() != "":
			objeto=info()
			compromar_001 = objeto.checar_actualizacion(self._valor_id,self.registrar_numero.get(),self.registrar_nombre.get())
			#values[1] != self.registrar_numero.get()
			#if values[2] != self.registrar_nombre.get() or values[1] != self.registrar_numero.get():
			print(compromar_001)
			if compromar_001:
				messagebox.showinfo("Error","El empleado ya esta registrado en la base de datos.")
			else:
				objeto.actualizar(self._valor_id,self.registrar_numero.get(),self.registrar_nombre.get(),self.registrar_telefono.get(),
					self.registrar_zona.get(),self.registrar_sucursal.get(),self.registrar_fecha.get(),
					self.registrar_supervisor.get(),self.registrar_gerente.get())

				self.registrar_nombre.delete(0, END); self.registrar_telefono.delete(0, END)
				self.registrar_sucursal.delete(0, END); self.registrar_fecha.delete(0, END)
				self.registrar_supervisor.delete(0, END); self.registrar_gerente.delete(0, END)
				self.registrar_numero.delete(0,END); self.registrar_zona.delete(0,END)
				self.top.destroy()
				messagebox.showinfo("Completado","Actualizacion de datos completada.")
				self.leer_info()
		else:
			messagebox.showinfo("Error","Debe llenar todos los apartados.")

if __name__ == "__main__":
	window=ThemedTk(theme="adapta")
	entrar_menu=Interfaz(window)
	window.mainloop()