def ejercicio1(n):
    if (n>1 and n<(10**6)):
        valores_parciales = [n]
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = n * 3 + 1
            valores_parciales.append(n)
        
        return valores_parciales
    else:
        return "El numero ingresado no es mayor a 1 y no es menor a 10^6"

resultado = ejercicio1(3)
print(resultado)

assert ejercicio1(3) == [3, 10, 5, 16, 8, 4, 2, 1], "La funcion es incorrecta"
