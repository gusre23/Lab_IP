n = int(input("Introduce un número: "))
i=2

if n <= 1:
    print("No es primo")
else:
    while i * i <= n:
        if n % i == 0:
            print("No es primo")
            break
        i = i + 1
    else:
        print("Es primo")