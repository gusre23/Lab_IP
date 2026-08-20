numero = 8

if numero == 0:
    print("0")

binario = ""
while numero > 0:
    residuo = numero % 16
    binario = str(residuo) + binario
    numero = numero // 16

print(binario)