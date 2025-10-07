# Ejercicio 1: Simulación de Sensores en un Robot

# Arreglo con las lecturas de los 4 sensores
sensores = [120, 85, 210, 150]

umbral = 100

print("Lecturas de sensores del robot:\n")

for i in range(len(sensores)):
    lectura = sensores[i]
    print(f"Sensor {i+1}: {lectura} cm")
    
    if lectura < umbral:
        print(" Obstáculo demasiado cerca")
        
