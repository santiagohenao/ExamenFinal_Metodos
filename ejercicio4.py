#Ejercicio4
# 'y' es una senal en funcion del tiempo 't' con las unidades descritas en el codigo.
# a. Grafique la senal en funcion del tiempo en la figura 'senal.png' ('y' vs. 't')
# b. Calule la transformada de Fourier (sin utilizar funciones de fast fourier transform) y
# grafique la norma de la transformada en funcion de la frecuencia (figura 'fourier.png')
# c. Lleve a cero los coeficientes de Fourier con frecuencias mayores que 10000 Hz y calcule 
# la transformada inversa para graficar la nueva senal (figura 'filtro.png')

import numpy as np


n = 512 # number of point in the whole interval
f = 200.0 #  frequency in Hz
dt = 1 / (f * 128 ) #128 samples per frequency
t = np.linspace( 0, (n-1)*dt, n) 
y = np.sin(2 * np.pi * f * t) + np.cos(2 * np.pi * f * t * t)
noise = 1.4*(np.random.rand(n)+0.7)
y  =  y + noise

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def fourier(time_arr,g_arr,freq):
    s=0j
    for i in range(len(time_arr)):
        s+=g_arr[i]*np.exp(-2*np.pi*1j*freq*time_arr[i])
    return s

def i_fourier(f_arr,transf_arr,time):
    g=0j
    for i in range(len(f_arr)):
        g+=transf_arr[i]*np.exp(2*np.pi*1j*f_arr[i]*time)
    return g

fspace=np.linspace(0,10000,len(t))

sspace=np.array([fourier(t,y,freq) for freq in fspace])

plt.figure()
plt.scatter(t,y,s=10)
plt.savefig("señal.png")

plt.figure()
plt.scatter(fspace,np.sqrt(sspace.real**2+sspace.imag**2),s=1,c='k')
plt.xlim([0,1000])
plt.savefig("fourier.png")

tspace=t
yspace=np.array([i_fourier(fspace,sspace,time_val) for time_val in tspace])

plt.figure()
plt.scatter(tspace,yspace.real,s=10,c='k')
#plt.xlim([0,1000])
plt.savefig("filtro.png")