numero, binario = 0, ""  # Le damos valor a las varibles "numero" y "binario".
if numero == 0: print("0")  # Si "numero" es 0, imprime 0.
while numero > 0: binario,numero = str(numero % 2) + binario, numero // 2  # Mientras "numero" sea mayor que 0, realizará lo siguiente hasta que ya no lo sea -> se suma el residuo de dividir "numero" entre 2 (convertido a texto por el "str") más "binario", y número se divide entre 2 de forma que resulte un número entero.
print(binario)  # Imprime "binario" (el número decimal traducido a binario).