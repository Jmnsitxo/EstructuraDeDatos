pesos = [
    [4, 1, 5, 6],
    [4, 1, 5, 6],
    [3, 1, 1 ,6],
]

salida = [0, 0, 0, 0]
start_time = time.time()

for j in range(len(pesos[0])):  # columnas de la matriz de pesos
    for i in range(len(pesos)):  # filas (entradas)
        salida[j] += entrada[i] * pesos[i][j]

end_time = time.time()

print("inicio:", start_time)
print("fin:", end_time)
print("duración:", end_time - start_time)
