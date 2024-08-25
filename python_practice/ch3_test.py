import numpy as np
from scipy.fftpack import fft
import sys, os, math
import matplotlib.pyplot as plt
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../software/models/'))
import utilFunctions as UF

# Set FFT window size 
M = 501
hM1 = int(math.floor((M+1)/2))
hM2 = int(math.floor(M/2))

# Read sound file
(fs, x) = UF.wavread('../sounds/soprano-E4.wav')
x1 = x[5000:5000+M] * np.hamming(M)

# Set FFT buffer
N = 1024
fftbuffer = np.zeros(N)

# Buffering with correct array sizes
fftbuffer[:hM1] = x1[hM2:]  # Copy the second half of x1 to the first half of fftbuffer
fftbuffer[N-hM2:] = x1[:hM2]  # Copy the first half of x1 to the second half of fftbuffer

# FFT
X = fft(fftbuffer)
mX = abs(X)  # Magnitude
mX_db = 20 * np.log10(mX + 1e-10)  # Magnitude in dB, small constant added to avoid log(0)

pX = np.unwrap(np.angle(X))  # unwrapped Phase

# Plotting
plt.figure(figsize=(10, 8))  # Adjusted figure size

# Plot original signal x1
plt.subplot(2, 2, 1)
plt.plot(x1)
plt.title('Original Signal (x1)')
plt.xlabel('Sample Index')
plt.ylabel('Amplitude')

# Plot FFT buffer
plt.subplot(2, 2, 2)
plt.plot(fftbuffer)
plt.title('FFT Buffer')
plt.xlabel('Sample Index')
plt.ylabel('Amplitude')

# Plot magnitude spectrum in dB
plt.subplot(2, 2, 3)
plt.plot(mX_db)
plt.title('Magnitude Spectrum (dB)')
plt.xlabel('Frequency Bin')
plt.ylabel('Magnitude (dB)')

# Plot phase spectrum
plt.subplot(2, 2, 4)
plt.plot(pX)
plt.title('Phase Spectrum')
plt.xlabel('Frequency Bin')
plt.ylabel('Phase (radians)')

plt.tight_layout()
plt.show()
