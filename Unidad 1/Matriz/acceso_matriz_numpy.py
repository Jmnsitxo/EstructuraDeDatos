#creacion de una matriz 3x3
import numpy as np

matriz_A = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

for fila in matriz_A:
    for elemento in fila:
        print(elemento, end=" ")
    print()



print("**********")

matriz_B = np.zeros((2,3))

for fila in matriz_A:
    for elemento in fila:
        print(elemento, end=" ")
    print()

