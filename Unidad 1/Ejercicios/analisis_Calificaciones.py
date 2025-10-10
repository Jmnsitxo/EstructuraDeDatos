
# Arreglo para almacenar las calificaciones de los estudiantes
calificaciones = []

# Solicitar el número de estudiantes
num_estudiantes = int(input("¿Cuántos estudiantes hay en la materia?: "))

# Capturar las calificaciones
for i in range(num_estudiantes):
	calif = float(input(f"Calificación del estudiante {i}: "))
	calificaciones.append(calif)

print("Calificaciones de los estudiantes:", calificaciones)

# Consultar una calificación por índice
indice = int(input("¿Qué índice de calificación quieres consultar?: "))
if 0 <= indice < len(calificaciones):
	print(f"La calificación en el índice {indice} es: {calificaciones[indice]}")
else:
	print("Índice fuera de rango.")

# Modificar una calificación por índice
modificar = input("¿Quieres modificar alguna calificación? (s/n): ").lower()
if modificar == 's':
	indice_mod = int(input("Índice a modificar: "))
	if 0 <= indice_mod < len(calificaciones):
		nuevo_valor = float(input("Nuevo valor de la calificación: "))
		calificaciones[indice_mod] = nuevo_valor
		print("Calificación modificada.")
	else:
		print("Índice fuera de rango.")

# Calcular el promedio general del grupo
promedio = sum(calificaciones) / len(calificaciones) if calificaciones else 0
print(f"El promedio general del grupo es: {promedio:.2f}")
