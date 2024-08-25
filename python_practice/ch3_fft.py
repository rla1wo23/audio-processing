import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import triang
from scipy.fftpack import fft

# Generate triangular window
x = triang(15)

# Prepare fftbuffer
fftbuffer = np.zeros(15)
fftbuffer[:8] = x[7:]
fftbuffer[8:] = x[:7]

# Compute FFT
X = fft(fftbuffer)
mX = abs(X)
pX = np.angle(X)

# Plot the results
plt.figure(figsize=(12, 8))

# First plot: original FFT result
plt.subplot(3, 1, 1)
plt.plot(X.real, label='Real Part')
plt.plot(X.imag, label='Imaginary Part')
plt.title('FFT of fftbuffer')
plt.legend()

# Second plot: Magnitude Spectrum
plt.subplot(3, 1, 2)
plt.plot(mX, label='Magnitude')
plt.title('Magnitude Spectrum')
plt.legend()

# Third plot: Phase Spectrum
plt.subplot(3, 1, 3)
plt.plot(pX, label='Phase')
plt.title('Phase Spectrum')
plt.legend()

plt.tight_layout()
plt.show()
