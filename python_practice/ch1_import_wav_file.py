from scipy.io.wavfile import read
#read function's input: wav file
#read function's output: sampling rate
#i wrote this sound file

(fs, x)=read('jaehyun_sound_for_study.wav')
print(fs)
print(x)