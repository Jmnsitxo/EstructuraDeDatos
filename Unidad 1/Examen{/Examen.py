# Función para calcular la diferencia absoluta entre las diagonales de una matriz cuadrada
def DiferenciaDiagonal(arr):
    n = len(arr)  # tamaño de la matriz (n x n)
    
    # Suma de la diagonal principal (izquierda a derecha)
    primary = sum(arr[i][i] for i in range(n))
    
    # Suma de la diagonal secundaria (derecha a izquierda)
    secondary = sum(arr[i][n - 1 - i] for i in range(n))
    
    # Retornar la diferencia absoluta
    return abs(primary - secondary)


# Ejemplo de uso:
if __name__ == "__main__":
    # Entrada de ejemplo (puedes modificarla)
    arr = [
        [11, 2, 4],
        [4, 5, 6],
        [10, 8, -12]
    ]
    
    # Llamada a la función y salida del resultado
    result = DiferenciaDiagonal(arr)
    print("La diferencia absoluta entre diagonales es:", result)
