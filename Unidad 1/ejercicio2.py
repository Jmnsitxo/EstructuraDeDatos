# Ejercicio: Matriz de conexiones

pesos = [
    [0.2, 0.8],   
    [0.5, -0.1],  
    [0.9, 0.3]    
]

# Vector de entrada (3 elementos)
entrada = [1.0, 0.5, -0.5]

# Calcular el producto punto: salida = entrada • pesos
salida = [0, 0]  
for j in range(2):  #
    for i in range(3):  
        salida[j] += entrada[i] * pesos[i][j]

# Mostrar resultados
print("Vector de entrada:", entrada)
print("Matriz de pesos:")
for fila in pesos:
    print(fila)
print("Vector de salida:", salida)
