def lista_ordenada_hasta_n(n):
    return list(range(1, n+1))

def encontrar_faltante(lista_evaluar, lista_referencia):
    bandera = False
    for elemento in lista_referencia:
        if elemento not in lista_evaluar:
            faltante = elemento
            bandera = True
    if bandera == False:
        faltante = "No existe un valor faltante en la lista ingresada"
    return faltante

def ejercicio2(cant_elem, lista):
    lista_referencia = lista_ordenada_hasta_n(cant_elem)
    valor_faltante = encontrar_faltante(lista, lista_referencia)
    return valor_faltante

print(ejercicio2(5, [1, 2, 4, 5]))

assert ejercicio2(5, [1, 2, 4, 5]) == 3, "La funcion es incorrecta"




