#test con problema mas grande

print("Test con problema mas grande")
import random
random.seed(42)

#generar problema con 20 items
n=20
valores = [random.randint(10, 100) for _ in range(n)]
pesos = [random.randint(5, 30) for _ in range(n)]
capacidad = 100

def mochila_fuerza_bruta(valores, pesos, capacidad):
	n = len(valores)
	mejor_valor = 0
	mejor_comb = []
	for i in range(1 << n):
		peso_total = 0
		valor_total = 0
		comb = []
		for j in range(n):
			if i & (1 << j):
				peso_total += pesos[j]
				valor_total += valores[j]
				comb.append(j)
		if peso_total <= capacidad and valor_total > mejor_valor:
			mejor_valor = valor_total
			mejor_comb = comb
	return mejor_valor, mejor_comb

#Solo la solucion aproximada es viable
print(f"pesos: {pesos}")
print(f"valores: {valores}")    
#result_approx = mochila_aproximacion(valores, pesos, capacidad)
result_approx = mochila_fuerza_bruta(valores, pesos, capacidad)
print(f"problema grande ({n} objetos):")            
print(f"Solucion aproximada: ganancia {result_approx[0]},objetos {result_approx[1]}")
print("(la solucion exacta es inviable en tiempo razonable)")

