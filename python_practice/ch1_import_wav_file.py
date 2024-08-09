from scipy.io.wavfile import read
import matplotlib.pyplot as plt
# read function's input: wav file
# read function's output: sampling rate and audio data array
# I wrote and composed this sound file: 'jaehyun_sound_for_study.wav'
# You are free to use this sound file for any purpose, including study, research, and creative projects.

(fs, x) = read('jaehyun_sound_for_study.wav')
print(f" variable \"fs\" is sampling rate, fs is {fs}")
print(f"then, var x is matrix that processed matrix by this library")
print(f"x.size is {x.size}, x/fs={x.size/fs}, it means length of the wav file")
print(f"If the X/FS result is twice the actual output length, it means that the file is a stereo file and has two channels, one for the left and one for the right.")

