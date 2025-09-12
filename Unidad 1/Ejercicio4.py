# Ejercicio 4: Historial de Entrenamiento de un Modelo (versión con for)

# Lista dinámica para guardar las precisiones
precisiones = []

n = int(input("¿Cuántas épocas de entrenamiento quieres registrar? "))

for i in range(n):
    valor = float(input(f"Precisión de la época {i+1}: "))
    precisiones.append(valor)

# Mostrar resultados
print("\n--- Resultados del entrenamiento ---")
print(f"Precisión final: {precisiones[-1]}%")
print(f"Máxima precisión alcanzada: {max(precisiones)}%")
