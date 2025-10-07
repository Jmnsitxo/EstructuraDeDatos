numeros = [70, 150, 360, 55, 17,1, 4, 2, 5, 3]
print ("Lista original:", numeros)

def insertionSort(lista):
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1
        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key
    return lista

numeros_ordenados = insertionSort(numeros)
print("Lista ordenada:", numeros_ordenados)