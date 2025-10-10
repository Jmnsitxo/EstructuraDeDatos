# Mapa de Temperaturas en una Ciudad (3x3)
mapa_temperaturas = []

# Captura de temperaturas promedio para cada zona
print("Ingresa la temperatura promedio para cada zona (3x3):")
for i in range(3):
	fila = []
	for j in range(3):
		temp = float(input(f"Temperatura en zona [{i}][{j}]: "))
		fila.append(temp)
	mapa_temperaturas.append(fila)

# Imprimir toda la matriz
print("\nMapa de temperaturas:")
for fila in mapa_temperaturas:
	print(fila)

# Acceder a una celda específica (por ejemplo, la central)
fila_central, col_central = 1, 1
print(f"\nTemperatura en la zona central [{fila_central}][{col_central}]: {mapa_temperaturas[fila_central][col_central]}")

# Modificar el valor de la celda central
modificar = input("¿Deseas modificar la temperatura de la zona central? (s/n): ").lower()
if modificar == 's':
	nueva_temp = float(input("Nueva temperatura para la zona central: "))
	mapa_temperaturas[fila_central][col_central] = nueva_temp
	print(f"Temperatura actualizada en la zona central: {mapa_temperaturas[fila_central][col_central]}")

# Imprimir la matriz actualizada
print("\nMapa de temperaturas actualizado:")
for fila in mapa_temperaturas:
	print(fila)
