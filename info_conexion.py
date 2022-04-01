from Conexion import Conexion

class info():
	def __init__(self):
		self.db  = Conexion()
		self.db.conectar()

	def orden_nombres(self):
		info=self.db.cursor.execute(f"SELECT * FROM Direcciones").fetchall()
		return info

	def agregar_elementos(self, nombre, telefono, sucursal, fecha, supervisor, gerente):
		self.db.cursor.execute(f"INSERT INTO Direcciones(nombre, telefono, sucursal, fecha_ingreso, supervisor, gerente) VALUES ('{nombre}', '{telefono}', '{sucursal}','{fecha}','{supervisor}','{gerente}')")
		self.db.cursor.commit()

if __name__ == "__main__":
	objeto=info()
	print(objeto.orden_nombres())