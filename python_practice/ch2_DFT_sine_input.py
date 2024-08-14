import numpy as np
import matplotlib.pyplot as plt

N=64
k0=7
X=np.array([])
x=np.cos(2*np.pi*k0/N*np.arange(N)) #generate cos wave
nv = np.arange(-N/2,N/2) # time indexes
kv = np.arange(-N/2,N/2) # index for k  

for k in kv:
  s=np.exp(1j*2*np.pi*k/N*nv)
  X=np.append(X,sum(x*np.conjugate(s)))

plt.plot(kv,abs(X))
plt.axis([-N/2,N/2-1,0,N])

plt.show()