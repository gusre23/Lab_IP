numero, octal = 8, ""  # Le damos valor a las varibles "numero" y "octal".
if numero == 0: print("0")  # Si "numero" es 0, imprime 0.
while numero > 0: octal,numero = str(numero % 8) + octal, numero // 8  # Mientras "numero" sea mayor que 0, realizará lo siguiente hasta que ya no lo sea -> se suma el residuo de dividir "numero" entre 8 (convertido a texto por el "str") más "octal", y número se divide entre 8 de forma que resulte un número entero.
print(octal)  # Imprime "octal" (el número decimal traducido a octal).