import matplotlib.pyplot as plt
import numpy as np

N = 500 #size of DFT or array length
k = 5
n = np.arange(-N/2,N/2)
s = np.exp (1j *2 * np.pi*k*n/N)

plt.plot(n,np.imag(s))  #make graph to n with real part of s
plt.axis([-N/2,N/2-1,-1,1])  #-1 to 1 because it was normalized
plt.xlabel('n')
plt.ylabel('amplitude')
plt.show()

