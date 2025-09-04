import numpy as np
import matplotlib.pyplot as plt

#definir la funcion 
def f1(x):
    return 2 * x + 1

#generar datos
x= np.linspace(-5, 5, 100)
y= f1(x)

#graficar
plt.figure(figsize=(15, 8))
plt.plot(x, y, label="$f(x) = 2x + 1$", color="blue")
plt.title(" Funcion Luneal Creciente")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()
 
    