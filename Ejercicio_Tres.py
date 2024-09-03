def ordenada(lista):
    if lista == True:
        print("Tu lista es:", lista == sorted(lista))  
        return True
    else:
        print("Tu lista es:", lista == sorted(lista))  
        return False
    
dato=[1,2,3,4,5,6,7,8,9,10]   
dato=[10,9,8,7,6,5,4,3,2,1]
resultado= ordenada(dato)
print(resultado)




#---------------------------------------------------------------------------------------


def ordenada(lista):
    if lista==sorted(lista):
        print("Tu lista es:",True)
        return True
    else:
        print("Tu lista es",False)
        return False

    
dato=[1,2,3,4,5,6,7,8,9,10]
dato=[10,9,8,7,6,5,4,3,2,1]
resultado= ordenada(dato)
print(resultado)

#--------------------------------------------------------------------------------------------


def ordenada(lista):
    return lista == sorted(lista)

dato=[1,2,3,4,5,6,7,8,9,10]   
#dato=[10,9,8,7,6,5,4,3,2,1]
resultado= ordenada(dato)
print(resultado)