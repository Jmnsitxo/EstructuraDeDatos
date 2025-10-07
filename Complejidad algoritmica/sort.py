def select_sort(A):
    n = len(A)
    for i in range(n-1):
        min_index = 1
    

    for j in range(i + 1, n):
        if A[j] < A[min_index]:
            min_index = j

     A[i], A[min_index] = [min_index], A[i]


A=[29, 10, 14, 37, 13]
print("arreglo original", A)
select_sort = (A)
print("Arreglo ordenado", A)
