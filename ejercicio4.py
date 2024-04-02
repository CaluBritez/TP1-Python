def armar_diccionario(cadena):
    contador_letras = {}
    
    for letra in cadena:
        if letra in contador_letras:
            contador_letras[letra] += 1
        else:
            contador_letras[letra] = 1
    
    return contador_letras
def contadores_son_pares(diccionario):
    for valor in diccionario.values():
        if valor % 2 != 0:
            return False
    return True
def formar_palindromo_par(diccionario):
    medio_palindromo = ""
    
    for letra, contador in diccionario.items():
        medio_palindromo += letra * (contador // 2)
    
    palindromo = medio_palindromo + medio_palindromo[::-1]
    
    return palindromo
def unico_impar(diccionario):
    cont_impar = 0
    
    for valor in diccionario.values():
        if valor % 2 != 0:
            cont_impar += 1
            if cont_impar > 1:
                return False
    
    return cont_impar == 1
def generar_palindromo_impar(diccionario):
    letra_impar = None
    for letra, contador in diccionario.items():
        if contador % 2 != 0:
            letra_impar = letra
            break
    
    if letra_impar is None:
        return None 
    
    palindromo = ""
    palindromo_sin_impar = ""
    
    for letra, contador in diccionario.items():
        palindromo += letra * (contador // 2)
        palindromo_sin_impar += letra * (contador // 2)
        
    palindromo += letra_impar
    
    palindromo += palindromo_sin_impar[::-1]
    
    return palindromo
#FUNCION FINAL
def formar_palindromo(cadena):
    diccionario = armar_diccionario(cadena)
    if (len(cadena) % 2 == 0):
        if (contadores_son_pares(diccionario)):
            resultado = formar_palindromo_par(diccionario)
            return resultado
        else:
            return "No se puede formar un palindromo con estas letras"
    else:
        if (unico_impar(diccionario)):
            resultado = generar_palindromo_impar(diccionario)
            return resultado
        else:
            return "No se puede formar un palindromo con estas letras"

# Probamos la funcion
cadena = "aabbc"
resultado = formar_palindromo(cadena)
print(resultado)

assert formar_palindromo("aabbc") == "abcba", "La funcion es incorrecta"
