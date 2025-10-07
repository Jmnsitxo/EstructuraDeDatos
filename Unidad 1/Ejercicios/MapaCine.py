# Ejercicio 3: Mapa de Asientos de un Cine

# Matriz 4x5
filas = 4
columnas = 5
asientos = [[0 for _ in range(columnas)] for _ in range(filas)]

# Función para imprimir mapa de asientos
def imprimir_mapa():
    print(" Mapa de asientos (0=Libre, 1=Ocupado):")
    for fila in asientos:
        print(" ".join(map(str, fila)))

# Mostrar mapa inicial
imprimir_mapa()

# Pedir fila y asiento al usuario
fila = int(input("\nIngrese la fila (1-4): ")) - 1
columna = int(input("Ingrese el asiento (1-5): ")) - 1

# Marcar asiento como ocupado si está libre
if asientos[fila][columna] == 0:
    asientos[fila][columna] = 1
    print("Asiento reservado.")
else:
    print("Ese asiento ya esta ocupado.")

# Mapa actualizado
imprimir_mapa()

# Contar asientos libres
libres = sum(fila.count(0) for fila in asientos)
print(f"Total de asientos libres: {libres}")
