def migratoryBirds(arr):
    # Contar cuántas veces aparece cada tipo de ave
    conteo = {}
    for ave in arr:
        if ave in conteo:
            conteo[ave] += 1
        else:
            conteo[ave] = 1

    # Encontrar la frecuencia máxima
    max_frecuencia = max(conteo.values())

    
    tipos_max = [tipo for tipo, freq in conteo.items() if freq == max_frecuencia]
    return min(tipos_max)


# ejemplo
arr = [1, 4, 4, 4, 5, 3]
print(migratoryBirds(arr))  # Salida esperada: 4


arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]
print(migratoryBirds(arr))  # Salida esperada: 3
