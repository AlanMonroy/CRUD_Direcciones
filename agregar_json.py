import pandas as pd

class leer():
	def __init__(self):
		try:
			self.df = pd.read_excel("datos1.xlsx")
			print(self.df)
		except:		
			df_vacio = pd.DataFrame(columns=["nombre","telefono","sucursal","fecha_ingreso","supervisor","gerente"])
			"""df_vacio = df_vacio.append({"nombre":"Alan",
							"telefono":"811901788",
							"sucursal":"guadalupe",
							"fecha_ingreso":"17/123/123",
							"supervisor":"alejandro",
							"gerente":"roberto"}, ignore_index=True)"""

			df_vacio.to_excel("datos1.xlsx")
			return 0

	def ordernar_por_nombre(self):
		ordenado = dict(self.df.sort_values("nombre",ascending="True"))
		return ordenado


if __name__ == "__main__":
	objeto=leer()
	datos=objeto.ordernar_por_nombre()
	print(datos)
	print(len(datos))

