def duplica(lista):
    if len(lista)==len(set(lista)):
        return False
    else:
        return True
    
dato=[1,2,3]
resultado= duplica(dato)
print(resultado)
    

import random
def numeros_random():
    lista_random = random.choices(range(1,100),k=23)
    return lista_random
    
    
lista = numeros_random()
resultado = duplica(lista)
print(lista)
print(resultado)


