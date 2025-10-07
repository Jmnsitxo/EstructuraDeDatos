def angryProfessor(k, a):
    contador= 0
    for tiempo in a:
        if tiempo <= 0:
            contador += 1

    if contador >= k:
        return "yes"
    else:
        return "no"
    
t = int(input())
for _ in range(t):
    datos = input().split()
    n = int(datos[0])
    k = int(datos[1])

    tiempos = list(map(int, input().split()))
    resultado = angryProfessor(k, tiempos)
    print(resultado)