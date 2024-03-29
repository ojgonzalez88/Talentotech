#IMC: Escribir un programa que pida al usuario su peso(en kg) y estatura (en metros), calcule el índice de masa corporal(IMC) y muestre en pantalla la frase: Tu índice de masa corporal es: , donde imc es el cálculo realizado. Este imc debe estar redondeado con dos decimales
peso = float(input("Cuál es su peso en kilos: "))
Estatura = float(input("Cuál es su estatura en metros: "))
IMC = peso/(Estatura**2)
IMC = round(IMC, 2)
if IMC <18.6:
    print(f'Su IMC es: {IMC} y corresponde a estar bajo de peso')
elif IMC <25:
    print(f'Su IMC es: {IMC} y corresponde a un peso normal')
elif IMC <30:
    print(f'Su IMC es: {IMC} y corresponde a estar en sobrepeso')
else:
    print(f'Su IMC es: {IMC} y corresponde a estar en obesidad')
if IMC <18.6:
    print(f"Debe subir de peso, su peso ideal es: {round((Estatura**2)*24.9)}")
elif IMC <25:
    print(f"Debe conservar su peso")
elif IMC <30:
    print(f"Debe bajar de peso, su peso ideal es: {round((Estatura**2)*24.9)}")
else:
    print(f"Debe bajar de peso, su peso ideal es: {round((Estatura**2)*24.9)}")
