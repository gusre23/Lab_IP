numero = 450

if numero == 0:
    print("0")

hexa = ""
if numero > 0:
    while numero > 16:
        residuo = numero % 16
        if residuo == 10: letra = "A"
        if residuo == 11: letra = "B"
        if residuo == 12: letra = "C"
        if residuo == 13: letra = "D"
        if residuo == 14: letra = "E"
        if residuo == 15: letra = "F"
        hexa = str(residuo) + hexa
        residuo = numero % 16 

print(hexa)