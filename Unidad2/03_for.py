# Trabajando con rangos en "for"

for numero in range(0, 7, 2): #el 2 hace avanzar los números de dos en dos
    cuadrado = numero ** 2
    print(numero, cuadrado) #imprime el cuadrado de los números pares del 0 al 6

# Trabajando con listas en "for"

materias = ["Python", "Linux", "Interfaces"]

for posicion, materia in enumerate(materias, start=1):
    print(f"{posicion}, {materia}") #imprime las materias enlistadas por números


for materia in materias:
    print(materia) #imprime las materias


cadena = "Peter"

for letra in cadena:
    print(letra) #imprime cada letra de "Peter" por separado


cadena2 = "0123456789ABCDEF"

for letra in cadena2:
    print(letra) #imprime "0123456789ABCDEF" por separado


for i in range(len(cadena)):
    print(cadena[i])