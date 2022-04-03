from Conexion import Conexion

class info():
	def __init__(self):
		self.db  = Conexion()
		self.db.conectar()

	def orden_nombres(self):
		info=self.db.cursor.execute(f"SELECT * FROM Direcciones").fetchall()
		info.sort(key = lambda x: x[1])
		return info

	def agregar_elementos(self, nombre, telefono, sucursal, fecha, supervisor, gerente):
		self.db.cursor.execute(f"INSERT INTO Direcciones(nombre, telefono, sucursal, fecha_ingreso, supervisor, gerente) VALUES ('{nombre}', '{telefono}', '{sucursal}','{fecha}','{supervisor}','{gerente}')")
		self.db.cursor.commit()

	def eliminar(self,valor):
		self.infoC=self.db.cursor.execute(f"SELECT * FROM Direcciones").fetchall()
		if len(self.infoC) != 0:
			self.db.cursor.execute(f"DELETE FROM Direcciones WHERE nombre = ?", valor)
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
	print(objeto.checar_nombre("Alan"))