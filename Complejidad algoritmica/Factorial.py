def factorial_recursivo(n):
    if n==0 or n==1:
        return 1
    else:
        print("n =", n, " n-1=,",n-1)
        return n * factorial_recursivo(n-1)
    
numero=1000
resultado= factorial_recursivo(numero)
print(f"El factorial de {numero} es: {resultado}")


