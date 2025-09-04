import numpy as np
import matplotlib.pyplot as plt

#definir la funcion 
def f2(x):
    return np.exp(x)

#generar datos
x= np.linspace(-100000, 100000, 20000000)
y= f2(x)

#graficar
plt.figure(figsize =(8, 4))
plt.plot(x,y, label="$f(x)=e^x$", color="red")
plt.title(" funcion exponencial creciente")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()        
plt.show()
