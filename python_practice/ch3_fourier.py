import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import triang
from scipy.fftpack import fft

x=triang(15)
X=fft(x)
mX=abs(X)
pX=np.angle(x)
plt.plot(x)
plt.plot(pX)