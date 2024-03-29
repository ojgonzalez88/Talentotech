#Buen camino:Escribir un programa que solicite al usuario su nombre y edad, e imprima
#Enunciado
#Buen camino: Escribir un programa que solicite al usuario su nombre y edad, e imprima : “Vas por buen camino[usuario]”
Usuario = str(input("Cuál es tu nombre: "))
edad = int(input("Cuantos años tiene: "))
mensaje = "Vas por buen camino "
print(f"{mensaje}{Usuario} Con {edad} años")