#Ejercicio3
# Los arrays `u` y `v` representan dos series en funcion del tiempo `t`.
# Grafique las dos series de datos en una misma imagen 'serie.png'
# Calcule la covarianza entre `u` y `v` e imprima su valor.

import numpy as np
t = np.array([0.,0.1,0.2,0.3,0.4,0.5,0.6, 0.8, 0.9])
u = np.array([12.,45.,6.,78.,34.,22.,-10.,31.,-27.])
v = np.array([3.,11.,1.3,37.,11.,6.,-23.,7.,7.])


import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.figure(figsize=(10,7))
plt.scatter(t,u,s=20,label="u")
plt.scatter(t,v,s=20,label="v")
plt.plot(t,u)
plt.plot(t,v)
plt.legend(loc=4)
plt.savefig("serie.png")

def cov(a,b):
    if(len(a)!=len(b)):
        return 1j
    c=0
    for i in range(len(a)):
        c+=(a[i]-a.mean())*(b[i]-b.mean())
    return c/(len(a)-1)

print(cov(u,v))