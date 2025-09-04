#reconocimiento de patrones

caracteristica = [3, 5, 1, 4,0.2]
sum = 0

for i in caracteristica:
    sum += i

    print("El valor de la caracteristica es: ", sum)

    for j in range(len(caracteristica)):
        caracteristica[j] = caracteristica[j]/sum

        print("las caracteristicas normaizadas son: ", caracteristica)
    

