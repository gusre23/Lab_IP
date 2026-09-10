# Solicita el total de la cuenta, el porcentaje de propina y el número de personas. Muestra el total con propina y cuánto paga cada persona.
# Convertir total y propina con float()
# Convertir personas con int()
# Calcular propina, total final y pago individual
# Mostrar cantidades con dos decimales

cuentatotal = float(input("Ingrese la cuenta total: "))

porcentaje = float(input("Ingrese porcentaje de propina (sin %): "))

personas = int(input("Ingrese número de personas: "))

print("-----------------------------------------------------")

propina = cuentatotal * (porcentaje / 100)
totalconpropina = float(cuentatotal + propina) 
print("La propina serán: $", propina)
print("En total con propina serán: $", cuentatotal, "+ $", propina, "= $", totalconpropina)

cuentaind = float(totalconpropina / personas)
print("Cada persona pagará: $", cuentaind)

print("-----------------------------------------------------")