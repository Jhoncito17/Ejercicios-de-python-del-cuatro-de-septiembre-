def suma_acumulada(lista):
    suma = 0
    milista = []
    for n in lista:
        suma += n
        milista.append(suma)
    return milista

dato=[1,2,3]
resultado= suma_acumulada(dato)
print(resultado)


def suma_acum(lista):
    suma=0
    milista=[suma := suma + n for n in lista]
    return milista


dato=[1,2,3]
resultado= suma_acumulada(dato)
print(resultado)

