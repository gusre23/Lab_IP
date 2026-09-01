numero = 30

if numero == 0:
    hexa = "0"  #si el número es 0, se arroja 0
else:
    hexa = ""
    while numero > 0:
        residuo = numero % 16
        
        if residuo < 10:
            caracter = str(residuo) #si el residuo es menor a diez, convertimos el número a texto
        elif residuo == 10:
            caracter = "A"  #de aquí a abajo se asigna su letra a los residuos desde 10 hasta 15
        elif residuo == 11:
            caracter = "B"
        elif residuo == 12:
            caracter = "C"
        elif residuo == 13:
            caracter = "D"
        elif residuo == 14:
            caracter = "E"
        elif residuo == 15:
            caracter = "F"
        
        hexa = caracter + hexa  #colocamos el nuevo caracter a la izquierda
        
        numero = numero // 16  #dividimos el número entre 16 en bucle mientras sea mayor que 0 (sólo números enteros)

print(hexa) #resultado de la conversión