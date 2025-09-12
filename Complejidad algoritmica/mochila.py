def mochila_fuerza_bruta(valores, pesos ,capacidad):
    n = len(valores)
    mejor_valor = 0
    mejor_combinacion = []

    #Probamos todas las combinaciones posibles (2^n)

    for i in range(1 << n):
        peso_actual = 0
        valor_actual = 0
        Objetos_seleccionados=[]

        for j in range(n):
            if i & (1 << j): #Si el j-ésimo bit de i es 1, incluimos el j-ésimo objeto
                peso_actual += pesos[j]
                valor_actual += valores[j]
                Objetos_seleccionados.append(j)
       #Verificamos si es valida y mejor
        if peso_actual <= capacidad and valor_actual > mejor_valor:
            mejor_valor = valor_actual
            mejor_combinacion = Objetos_seleccionados 

    return mejor_valor, mejor_combinacion




def mochila_aproximacion(valores, pesos, capacidad):
    n = len(valores)
    ratio = [(valores[i] / pesos[i], i) for i in range(n)]
    ratio.sort(reverse=True, key=lambda x: x[0]) #Ordenamos por valor/peso

    peso_actual = 0
    valor_actual = 0
    Objetos_seleccionados = []

    for r, i in ratio:
        if peso_actual + pesos[i] <= capacidad:
            peso_actual += pesos[i]
            valor_actual += valores[i]
            Objetos_seleccionados.append(i)

    return valor_actual, Objetos_seleccionados



valores = [4, 2, 1, 10, 2]
pesos = [12, 2, 1, 4, 1]
capacidad = 15

n = len(valores)
print(f"pesos: {pesos}")
print(f"valores: {valores}")
#result_approx = mochila_aproximacion(valores, pesos, capacidad)

result_approx = mochila_fuerza_bruta(valores, pesos, capacidad)
print(f"problema grande ({n} objetos):")
print(f"Solucion aproximada: ganancia {result_approx[0]},objetos {result_approx[1]}")