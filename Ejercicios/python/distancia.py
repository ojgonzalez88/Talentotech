#Distancia: Se desea calcular la distancia recorrida(m) por un móvil que tiene velocidad constante(m/s) durante un tiempo t(s),considera que es MRU(Movimiento rectilíneo uniforme), teniendo en cuenta que la fórmula de V en MRU es V=D/T
velocidad = float(input("a que velocidad va el móvil m/s: "))
tiempo = float(input("cuanto segundos lleva moviendose: "))
Distancia = velocidad*tiempo
print(f'la distancia recorrida es {Distancia} metros')