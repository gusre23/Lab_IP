operador = input("Inserta un operador (+, -, *, /): ") #ingresamos el signo de la operación

num1 = input("Inserta un primer número: ")  #ingresamos ambos números
num2 = input("Inserta un segundo número: ")

resultado = num1 + operador + num2

resultado = eval(resultado) #eval trata los resultados como una operación con números

print(resultado)