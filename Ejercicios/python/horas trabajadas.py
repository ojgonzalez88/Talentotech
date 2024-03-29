#Horas trabajadas: Escribir un programa que pregunte al usuario por el número de horas trabajadas y el costo por hora. Después muestre en pantalla el pago que le corresponde
horas = int(input("Señor usuario cuandos horas ha trabajado: "))
costo = int(input("Cuánto cuesta la hora de trabajo: "))
pago = horas * costo
print(f'Le corresponde un pago de {pago} pesos')