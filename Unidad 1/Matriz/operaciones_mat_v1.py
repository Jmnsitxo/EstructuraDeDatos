import numpy as np

matriz_A= [ [1,2,3],
            [5,6,7],
            [9,9,9,]]

Matriz_B= [ [1,4,3],
            [1,6,7],
            [9,4,99]]

#Suma de matrices 
suma=np.add(matriz_A, Matriz_B)
print("Suma de matrices", suma)

#Multiplicacion de natrices
multiplicacion= np.dot(matriz_A, Matriz_B)
print("Multiplicacion de matrices", multiplicacion)

#Producto punto de matriz
Vector_E = np.array([1,2,3])
resultado = np.dot(matriz_A, Vector_E)
