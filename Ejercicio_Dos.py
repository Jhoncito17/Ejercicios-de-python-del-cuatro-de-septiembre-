def elimina(lista):
    len(lista)
    lista.pop(0)
    lista.pop(-1)
    return lista


def salida(lista):
    print("La lista original es:",lista)
    lista_nueva= elimina(lista.copy())
    print("La lista modificada es:",lista_nueva)
    
    
    
dato=["Hola",1,2,3,"Adios"]
salida(dato)

#----------------------------------------------------------------------------------------

def media(lista):
    return lista[1:-1]

dato=["Hola",1,2,3,"Adios"]
resultado= media(dato)
salida=("la lista original es:", dato)
salidita=("la lista modificada es:", resultado)
print(salida)
print(salidita)