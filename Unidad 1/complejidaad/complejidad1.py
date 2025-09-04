#Analisis de complejidad de algoritmos

import time

def buscar_elemento(lista, elemento):
    for i in range(len(lista)):
        if lista[1]== elemento:
            return True
        return False
start_Time = time.time()
mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
elemento = 5
encontrado = buscar_elemento(mi_lista, elemento)
endTime = time.time()
if encontrado:
    print(f"Elemento {elemento} encontrado en la lista")
else:
    print(f"Elemento {elemento} no encontrado en la lista")
print(f" Tiempo de ejecucion: {endTime - start_Time}")


