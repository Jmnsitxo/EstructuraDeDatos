import time

def tiene_duplicados_lineal(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False

#pruebas con diferentes tamaños de arreglos
sizes = [100, 1000, 10000]

for n in sizes:
    arr = list(range(n)) #arreglo sin duplicados

start_time =time.time()
tiene_duplicados_lineal(arr)
end_time = time.time()
print(f" tamaño del arreglo: {n}, tiempo de ejecucion:{end_time - start_time} segundos")
