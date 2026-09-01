n = int(input("Introduce un número: "))
i=2

es_primo = True

if n <= 1:
    es_primo = False
else:
    while i < n:
        if n % i == 0:
            es_primo = False
            break
        i = i + 1

if es_primo == True:
    print ("Es primo")

    a = 0
    b = 1

    while a < n:
        siguiente = a + b
        a = b
        b = siguiente
    
    if a == n:
        print ("Está en Fibonacci")
    else:
        print ("No está Fibonacci")
else:
    
    print("No es primo")
