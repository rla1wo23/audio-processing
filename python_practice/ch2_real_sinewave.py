import matplotlib.pyplot as plt
import numpy as np

A = .8   #amplitude
f0 = 1000  #Hz
phi = np.pi/2  #initial phase
fs = 44100 #Sampling Rates
t = np.arange(-0.002,.002, 1.0/fs)  #(start value, end value, increaments)
x = A*np.cos(2*np.pi*f0*t+phi)

plt.plot(t,x)  #make graph with t and x
plt.axis([-0.002, .002, -.8, .8])  #-0.002 to .002: x-axis, -.8 to .8: y-axis
plt.xlabel('time')
plt.ylabel('amplitude')

plt.show()

