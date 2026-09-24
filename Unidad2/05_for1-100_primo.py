for numero in range(2, 101):
    for divisor in range(2, numero):
        if numero % divisor == 0: #divide cada número entre los números que van antes de él, si el residuo es 0 termina en break, si no lo es lo imprime
            break
    else: print(numero)
