# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 15:54:10 2021

@author: enzoa
"""

import librosa, librosa.display
import matplotlib.pyplot as plt
import numpy as np

file = "11- Preprocessing audio data for deep learning_code_blues.00000.wav"

# waveform
signal, sr = librosa.load(file, sr=22050) # sr * T -> 22050 * 30
#librosa.display.waveplot(signal, sr=sr)
#plt.xlabel("Time")
#plt.ylabel("Amplitude")
#plt.show()

# fft -> spectrum
fft = np.fft.fft(signal)

magnitude = np.abs(fft)
frequency = np.linspace(0, sr, len(magnitude))

left_frequency = frequency[:int(len(frequency)/2)] # Nyquist frequency sr/2
left_magnitude = magnitude[:int(len(frequency)/2)] # Nyquist frequency sr/2

#plt.plot(left_frequency, left_magnitude)
#plt.xlabel("Frequency")
#plt.ylabel("Magnitude")
#plt.show()

# stft -> spectogram

n_fft = 2048 # window length, power of 2 is faster
hop_length = 512 # slide window, usually multiple of 2 too

stft = librosa.core.stft(signal, n_fft=n_fft, hop_length=hop_length)
spectogram = np.abs(stft) 
log_spectogram = librosa.amplitude_to_db(spectogram) # we percieve sound in log scale

#librosa.display.specshow(log_spectogram, sr=sr, hop_length=hop_length)
#plt.xlabel("Time")
#plt.ylabel("Frequency")
#plt.colorbar()
#plt.show()

# MFCCs
MFCCs = librosa.feature.mfcc(signal, n_fft=n_fft, hop_length=hop_length, sr=sr, n_mfcc=13)
librosa.display.specshow(MFCCs, sr=sr, hop_length=hop_length)
plt.xlabel("Time")
plt.ylabel("MFCC")
plt.colorbar()
plt.show() 