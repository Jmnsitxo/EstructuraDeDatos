import numpy as np
import matplotlib.pyplot as plt

#definir la funcion 
def f3(x):
    return -x + 3

#generar datos
x=np.linspace(-5, 5, 100)
y= f3(x)

#graficar
plt.figure(figsize=(8,4))
plt.plot(x,y label)


