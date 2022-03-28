import json

info={"Direcciones":[
		{"nombre":"roberto alan", "telefono": "8111901788",
			"sucursal":"guadalupe", "fecha_ingreso":"17/9/2021",
			"supervisor":"alejandro","gerente":"miguel"},
		{"nombre":"victor monroy", "telefono": "8111901788",
			"sucursal":"guadalupe", "fecha_ingreso":"17/9/2021",
			"supervisor":"alejandro","gerente":"miguel"}
	]
}
with open("datos.json","w") as f:
	json.dump(info,f)

