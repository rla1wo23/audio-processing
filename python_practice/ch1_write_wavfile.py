from scipy.io.wavfile import read, write

(fs, x) = read('jaehyun_sound_for_study.wav')
y=x[44100:58800]
print("We will create a new file by extracting parts of the original file named test.wav")
write('test.wav',fs,y)