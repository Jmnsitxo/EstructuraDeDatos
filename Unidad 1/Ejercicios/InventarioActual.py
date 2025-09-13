# Ejercicio 2: Inventario de Productos en un Almacén

# Matriz: [ID, cantidad, precio]
inventario = [
    [101, 50, 20.5],   
    [102, 30, 15.0],   
    [103, 80, 10.0]   
]

# Imprimir inventario
print("Inventario actual:\n")
for producto in inventario:
    print(f"ID: {producto[0]}, Cantidad: {producto[1]}, Precio: ${producto[2]}")

# Calcular valor total de un producto específico
indice = 1  
cantidad = inventario[indice][1]
precio = inventario[indice][2]
valor_total = cantidad * precio
print(f"Valor total del producto {inventario[indice][0]}: ${valor_total}")

# Vender 10 unidades y actualizar stock
inventario[indice][1] -= 10
print(f"Stock actualizado del producto {inventario[indice][0]}: {inventario[indice][1]}")
