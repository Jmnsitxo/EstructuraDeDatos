# Matriz 4x4 para almacenar intensidades de luz
matriz_luz = []

# Captura de intensidades
print("Ingresa las intensidades de luz para cada sensor (4x4):")
for i in range(4):
	fila = []
	for j in range(4):
		valor = float(input(f"Intensidad en posición [{i}][{j}]: "))
		fila.append(valor)
	matriz_luz.append(fila)

# Imprimir la matriz completa
print("\nMatriz de intensidades de luz:")
for fila in matriz_luz:
	print(fila)

# Consultar la intensidad en una posición específica
fila_consulta = int(input("\nFila a consultar (0-3): "))
col_consulta = int(input("Columna a consultar (0-3): "))
if 0 <= fila_consulta < 4 and 0 <= col_consulta < 4:
	print(f"Intensidad en [{fila_consulta}][{col_consulta}]: {matriz_luz[fila_consulta][col_consulta]}")
else:
	print("Posición fuera de rango.")

# Modificar el valor en una posición específica
modificar = input("¿Deseas modificar alguna intensidad? (s/n): ").lower()
if modificar == 's':
	fila_mod = int(input("Fila a modificar (0-3): "))
	col_mod = int(input("Columna a modificar (0-3): "))
	if 0 <= fila_mod < 4 and 0 <= col_mod < 4:
		nuevo_valor = float(input("Nuevo valor de intensidad: "))
		matriz_luz[fila_mod][col_mod] = nuevo_valor
		print("Intensidad modificada.")
	else:
		print("Posición fuera de rango.")

# Calcular el promedio general de iluminación
suma = sum(sum(fila) for fila in matriz_luz)
promedio = suma / 16
print(f"\nPromedio general de iluminación en la cuadrícula: {promedio:.2f}")
