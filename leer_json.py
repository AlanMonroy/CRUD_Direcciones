import json

class leer():
	def __init__(self):
		with open("datos.json") as f:
			info=json.load(f)
		
		self.data=info["Direcciones"]

	def ordernar_por_nombre(self):
		self.data.sort(key=lambda p:p["nombre"])
		return self.data

"""for i in data:
	print(i["nombre"])
	print(i["telefono"])"""

if __name__ == "__main__":
	objeto=leer()
	print(objeto.ordernar_por_nombre())