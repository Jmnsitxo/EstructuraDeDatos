#limpieza de datos con numpy
import numpy as np

#simular matriz de datos de 5*5
np.random.seed(42)
datos= np.random.randint(5,5)*100

#simular datos erroneos
datos[0,0]= -99
datos[2,3]=1000

print("Matriz original:\n", datos)

indices_erroneos=[0,2]

datos_limpios= np.delete(datos, indices_erroneos, axis=0)
print("Matriz limpia:\n", datos_limpios)