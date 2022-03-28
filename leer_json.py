import json

class leer():
	def __init__(self):
		with open("datos.json") as f:
			info=json.load(f)
		
		self.data=info["Direcciones"]

"""for i in data:
	print(i["nombre"])
	print(i["telefono"])"""