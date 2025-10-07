def angryProfessor(k, a):
    
    
    
    # Contar cuántos estudiantes llegaron a tiempo
    on_time = sum(1 for time in a if time <= 0)
    
    
    return "YES" if on_time < k else "NO"


# --- Entrada y salida desde consola ---
if __name__ == "__main__":
    t = int(input().strip()) 
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        print(angryProfessor(k, a))
