lista = [(1,"Alan","epa","ke onda"),(2,"ana","no ma","chingas")]
valor_busqueda = "a"

for i in lista:
    for a in i:
        b=str(a)
        #objeto = b.find(valor_busqueda)
        objeto=b[:len(valor_busqueda)].find(valor_busqueda)
        if objeto != -1:
            print(i)

"""for i in lista: #la tupla
    for a in i: #la cadena
        b=str(a) #cadena en str
        if incremento != longitud:
            valor2+=b
            print(valor2)
            incremento+=1
        incremento=0
        print("VALOR 1: ",valor_busqueda.lower()); print("VALOR 2: ",valor2.lower())
        if valor_busqueda.lower() == valor2.lower():
            print("encontrado",i)
            print("encontrado",b.lower())
            print("-----------------------------------------------------------------------")
        valor2="""




