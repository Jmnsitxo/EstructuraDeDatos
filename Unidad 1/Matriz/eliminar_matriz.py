import numpy as np

datos= np.array([
    [10, 20, 30, 40],
    [15, 20, 35, 45],
    [25, 20, 45, 55]
])

print("Matriz original:\n", datos)

datos_limpios = np.delete(datos, 2, axis=0)

print(" conjunto de daots limpio")
print(datos_limpios)