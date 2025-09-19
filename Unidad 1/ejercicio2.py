# Ejercicio: Matriz de conexiones para una red neuronal simple

# Matriz de pesos (3x2)
# 3 neuronas de entrada -> 2 de salida
pesos = [
    [0.2, 0.8],   # conexiones de la neurona 1
    [0.5, -0.1],  # conexiones de la neurona 2
    [0.9, 0.3]    # conexiones de la neurona 3
]

# Vector de entrada (3 elementos)
entrada = [1.0, 0.5, -0.5]

# Calcular el producto punto: salida = entrada • pesos
salida = [0, 0]  # inicializamos con dos salidas
for j in range(2):  # columnas de la matriz de pesos
    for i in range(3):  # filas (entradas)
        salida[j] += entrada[i] * pesos[i][j]

# Mostrar resultados
print("Vector de entrada:", entrada)
print("Matriz de pesos:")
for fila in pesos:
    print(fila)
print("Vector de salida:", salida)
