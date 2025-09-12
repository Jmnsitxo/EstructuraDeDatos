import matplotlib.pyplot as plt
import time
import random
random.seed(42)

# Solución exacta usando fuerza bruta para el problema de la mochila
def mochila_fuerza_bruta(valores, pesos, capacidad):
    n = len(valores)
    max_valor = 0

    def helper(i, peso_actual, valor_actual):
        nonlocal max_valor
        if i == n:
            if valor_actual > max_valor:
                max_valor = valor_actual
            return
        # No tomar el objeto i
        helper(i + 1, peso_actual, valor_actual)
        # Tomar el objeto i si cabe
        if peso_actual + pesos[i] <= capacidad:
            helper(i + 1, peso_actual + pesos[i], valor_actual + valores[i])

    helper(0, 0, 0)
    return max_valor

# Algoritmo aproximado para el problema de la mochila (greedy por valor/peso)
def mochila_aproximacion(valores, pesos, capacidad):
    n = len(valores)
    # Calcular el valor por peso de cada objeto y su índice
    objetos = sorted([(valores[i] / pesos[i], valores[i], pesos[i]) for i in range(n)], reverse=True)
    peso_total = 0
    valor_total = 0
    for ratio, valor, peso in objetos:
        if peso_total + peso <= capacidad:
            peso_total += peso
            valor_total += valor
    return valor_total

#funcion para medir tiempos de ejecucion 
def medir_tiempo(func, *args):
    start = time.time()
    func(*args)
    end = time.time()
    return end - start

#comparacion de tiempos para diferentes tamaños
sizes= [5, 10, 15, 20, 25]
tiempos_exactos = []
tiempos_aproximados = []
for size in sizes:
    valores = [random.randint(10, 100) for _ in range(size)]
    pesos = [random.randint(5, 30) for _ in range(size)]
    capacidad = size * 10  #Capacidad proporcional al tamaño

    #medir tiempo solucion exacta
    tiempo_exacto = medir_tiempo(mochila_fuerza_bruta, valores, pesos, capacidad)
    tiempos_exactos.append(tiempo_exacto)

    #medir tiempo aproximado (solo para tamaños pequeños)
    if size <= 20:
        tiempo_aproximado = medir_tiempo(mochila_aproximacion, valores, pesos, capacidad)
        tiempos_aproximados.append(tiempo_aproximado)
    else:
        tiempos_aproximados.append(None)  

print("Tiempos exactos:", tiempos_exactos)
print("Tiempos aproximados:", tiempos_aproximados)
    

#Graficar resultados
plt.figure(figsize=(10, 6))
plt.plot(sizes[ : len(tiempos_exactos)], tiempos_exactos, label='Fuerza Bruta', marker='o')
plt.plot(sizes[ : len(tiempos_aproximados)], tiempos_aproximados, label='Aproximacion', marker='o')
plt.xlabel("tamaño del problema (n)")
plt.ylabel("Tiempo de ejecucion (segundos)")
plt.title("Comparacion de tiempos: Fuerza Bruta vs Aproximacion")
plt.legend()
plt.grid(True)
plt.yscale('log')  #Escala logaritmica para mejor visualizacion
plt.show()