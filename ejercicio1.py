# Ejercicio1
# A partir de los arrays x y fx calcule la segunda derivada de fx con respecto a x. 
# Esto lo debe hacer sin usar ciclos 'for' ni 'while'.
# Guarde esta segunda derivada en funcion de x en una grafica llamada 'segunda.png'

import numpy as np

x = np.linspace(0,2.,10)
fx = np.array([0., 0.0494, 0.1975, 0.4444, 0.7901,1.2346 , 1.7778, 2.4198, 3.1605, 4.])

def desplazar(numpy_arr):
    lista=[0]+list(numpy_arr)
    return np.array(lista[1:-1])

dx=np.mean(x[1:]-desplazar(x))

df=(fx[1:]-desplazar(fx))/dx # valores de la derivada desde donde está definida, es decir, desde x[1]

df2=(df[1:]-desplazar(df))/dx # la segunda derivada sólo está definida desde x[2]
