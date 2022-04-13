from Conexion import Conexion
import pandas as pd
from tkinter import filedialog, messagebox

class info():
	def __init__(self):
		self.db  = Conexion()
		self.db.conectar()

	def orden_nombres(self):
		info=self.db.cursor.execute(f"SELECT * FROM Direcciones").fetchall()
		info.sort(key = lambda x: x[2])
		"""info=[]
		for i in range(50):
			valor=(i,"Alan","8111901788","guadalupe","12/23/23","roberto","victor")
			info.append(valor)"""
		return info

	def buscar(self, valor_busqueda):
		info=self.db.cursor.execute(f"SELECT * FROM Direcciones").fetchall()
		info1=[]
		valor_busqueda1=valor_busqueda.lower()

		if valor_busqueda =="":
			return info

		for i in info:
			cadena_nombre = i[2].split(" ")
			cadena_supervisor = i[7].split(" ")
			cadena_gerente = i[8].split(" ")
			lista = [cadena_nombre,cadena_supervisor,cadena_gerente]

			for a in i:
				b=str(a)
				c=b.lower()
				objeto=c[:len(valor_busqueda1)].find(valor_busqueda1)
				if objeto != -1:
					info1.append(i)
					break
					
			for leer_cadena in lista:
				for a1 in leer_cadena:
					b1=str(a1)
					c1=b1.lower()
					objeto1=c1[:len(valor_busqueda1)].find(valor_busqueda1)
					if objeto1 != -1 and i not in info1:
						info1.append(i)
						break
		
		return info1

	def agregar_elementos(self, numero,nombre, telefono, zona,sucursal, fecha, supervisor, gerente):
		self.db.cursor.execute(f"INSERT INTO Direcciones(numero_empleado,nombre,telefono,zona,sucursal,fecha_ingreso,supervisor,gerente) VALUES ('{numero}','{nombre}', '{telefono}', '{zona}','{sucursal}','{fecha}','{supervisor}','{gerente}')")
		self.db.cursor.commit()

	def actualizar(self, identificador, numero,nombre, telefono, zona,sucursal, fecha, supervisor, gerente):
		print(numero)
		self.db.cursor.execute("UPDATE Direcciones SET numero_empleado = ? WHERE Id = ?",numero,identificador)
		self.db.cursor.execute("UPDATE Direcciones SET nombre = ? WHERE Id = ?",nombre,identificador)
		self.db.cursor.execute("UPDATE Direcciones SET telefono = ? WHERE Id = ?",telefono,identificador)
		self.db.cursor.execute("UPDATE Direcciones SET zona = ? WHERE Id = ?",zona,identificador)
		self.db.cursor.execute("UPDATE Direcciones SET sucursal = ? WHERE Id = ?",sucursal,identificador)
		self.db.cursor.execute("UPDATE Direcciones SET fecha_ingreso = ? WHERE Id = ?",fecha,identificador)
		self.db.cursor.execute("UPDATE Direcciones SET supervisor = ? WHERE Id = ?",supervisor,identificador)
		self.db.cursor.execute("UPDATE Direcciones SET gerente = ? WHERE Id = ?",gerente,identificador)
		self.db.cursor.commit()

	def eliminar(self,valor):
		self.infoC=self.db.cursor.execute(f"SELECT * FROM Direcciones").fetchall()
		if len(self.infoC) != 0:
			self.db.cursor.execute(f"DELETE FROM Direcciones WHERE Id = ?", valor)
			self.db.cursor.commit()

	def checar_nombre(self,numero,nombre,):
		info=self.db.cursor.execute(f"SELECT * FROM Direcciones WHERE numero_empleado = ?",numero).fetchall()
		info2=self.db.cursor.execute(f"SELECT * FROM Direcciones WHERE nombre = ?",nombre).fetchall()
		
		if len(info) != 0 or len(info2) != 0:
			return f"Si esta"
		"""if len(info) != 0:
			for i in info:
				print(i[1],i[2])
				print(type(i[1]))
				if nombre == i[2] or numero == i[1]:
					return f"Si esta"""

	def checar_actualizacion(self,identificador,numero,nombre,):
		info=self.db.cursor.execute(f"SELECT * FROM Direcciones").fetchall()
		identificador1 = int(identificador)

		diccionario = {}
		for i in info:
			if i[0] != identificador1:
				diccionario[f"{i[0]}"] = {"id":i[0],
					"numero":i[1],
					"nombre":i[2],
					"telefono":i[3],
					"zona":i[4],
					"sucursal":i[5],
					"fecha":i[6],
					"supervisor":i[7],
					"gerente":i[8],
					}

		for x in diccionario.values():
			if nombre == x["nombre"]:
				return f"Si esta {nombre}"
			elif numero == x["numero"]:
				return f"Si esta {numero}"

	def exportar_archivo(self):
		data_null={}
		df_null = pd.DataFrame(data_null)
		a = filedialog.asksaveasfilename(title="Abrir", initialdir = "C:/",filetypes = [("Archivo excel","*.xlsx")])

		if a != "":
			df_vacio = pd.DataFrame(columns=["Id","Número empleado","Nombre","Teléfono","Zona","Sucursal","Fecha de ingreso","Supervisor","Gerente"])
			valores_to_excel2=self.db.cursor.execute(f"SELECT * FROM Direcciones").fetchall()
			for i in valores_to_excel2:
				df_vacio = df_vacio.append({"Id": i[0],
								"Número empleado":i[1],
								"Nombre": i[2],
								"Teléfono":i[3],
								"Zona":i[4],
								"Sucursal":i[5],
								"Fecha de ingreso":i[6],
								"Supervisor":i[7],
								"Gerente":i[8]}, ignore_index=True)

			df_vacio.to_excel(f"{a}.xlsx",index=False)

			messagebox.showinfo("Completado","Excel creado.")

if __name__ == "__main__":
	objeto=info()
	obj = objeto.orden_nombres()
	print(objeto.checar_actualizacion(16,"333","jose"))
	objeto.buscar("ro")