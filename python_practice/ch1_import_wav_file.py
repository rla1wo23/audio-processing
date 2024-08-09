from scipy.io.wavfile import read

# read function's input: wav file
# read function's output: sampling rate and audio data array
# I wrote and composed this sound file: 'jaehyun_sound_for_study.wav'
# You are free to use this sound file for any purpose, including study, research, and creative projects.

(fs, x) = read('jaehyun_sound_for_study.wav')
print(fs)
print(x)
