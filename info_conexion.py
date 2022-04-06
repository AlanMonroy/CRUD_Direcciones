from Conexion import Conexion

class info():
	def __init__(self):
		self.db  = Conexion()
		self.db.conectar()

	def orden_nombres(self):
		info=self.db.cursor.execute(f"SELECT * FROM Direcciones").fetchall()
		info.sort(key = lambda x: x[1])
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
		    for a in i:
		        b=str(a)
		        c=b.lower()
		        objeto=c[:len(valor_busqueda1)].find(valor_busqueda1)
		        if objeto != -1:
		            info1.append(i)
		            break
		
		return info1

	def agregar_elementos(self, nombre, telefono, sucursal, fecha, supervisor, gerente):
		self.db.cursor.execute(f"INSERT INTO Direcciones(nombre, telefono, sucursal, fecha_ingreso, supervisor, gerente) VALUES ('{nombre}', '{telefono}', '{sucursal}','{fecha}','{supervisor}','{gerente}')")
		self.db.cursor.commit()

	def actualizar(self, identificador, nombre, telefono, sucursal, fecha, supervisor, gerente):
		self.db.cursor.execute("UPDATE Direcciones SET nombre = ? WHERE Id = ?",nombre,identificador)
		self.db.cursor.execute("UPDATE Direcciones SET telefono = ? WHERE Id = ?",telefono,identificador)
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

	def checar_nombre(self,nombre):
		info=self.db.cursor.execute(f"SELECT * FROM Direcciones WHERE nombre = ?",nombre).fetchall()
		if len(info) != 0:
			for i in info:
				if nombre == i[1]:
					return f"Si esta"

if __name__ == "__main__":
	objeto=info()
	obj = objeto.orden_nombres()
	#print(objeto.checar_nombre("Alan"))
	objeto.buscar("a")