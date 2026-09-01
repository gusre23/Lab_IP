numero, hexa = 987654321, ""  # ingresamos el número decimal a convertir
if numero == 0: hexa = "0"  # si el número es 0, imprime "0".
while numero > 0:
    residuo = numero % 16   
    if residuo < 10: caracter = str(residuo) # Asignamos caracteres según el residuo:
    elif residuo == 10: caracter = "A"
    elif residuo == 11: caracter = "B"
    elif residuo == 12: caracter = "C"
    elif residuo == 13: caracter = "D"
    elif residuo == 14: caracter = "E"
    elif residuo == 15: caracter = "F"
    hexa, numero = caracter + hexa, numero // 16  # acumula el resultado y divide entre 16.
print(hexa)  # imprime el resultado en hexa