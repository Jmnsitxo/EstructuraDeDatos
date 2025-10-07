def busqueda_binaria(lista, objetivo):
    low, high = 0, len(lista)-1
    while low <=high:
        mid=(low+high)//2
        if lista[mid]==objetivo:
            return mid
        elif lista[mid]<objetivo:
            low=mid+1
        else:
            high=mid-1
            return -1
#ejemplo
nums=[2,4,7,10,15,20,35]
x=15
pos=busqueda_binaria(nums,x)
print("elemento encontrado en la posicion:",pos)

