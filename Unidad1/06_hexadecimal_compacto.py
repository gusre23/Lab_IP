numero, hexa = 987654321, ""  # Se inicializa hexa en "" para poder concatenar texto dentro del ciclo.

if numero == 0: hexa = "0"  # Si el número es 0, asigna "0" directamente.
while numero > 0: hexa, numero = "0123456789ABCDEF"[numero % 16] + hexa, numero // 16  # Toma el carácter correspondiente al residuo, lo agrega a la izquierda y divide el número entre 16.

print(hexa)  # Imprime el resultado final en hexadecimal.