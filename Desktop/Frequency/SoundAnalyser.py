#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 21:28:42 2018

@author: roxanneturcotte
"""

import matplotlib.pyplot as plt
import plotly.plotly as py
from scipy.io import wavfile as wav
import numpy as np
from scipy.fftpack import fft









rate, data = wav.read("Resonnance.wav")
print("rate", rate)             #sample rate (in samples/sec)

Fs = rate       # Sampling rate
Ts = 1.0/Fs     # Sampling interval
t = np.arange(0,1,Ts) # time vector

n = len(data)   # Length of the signal
q = int(n/2)
k = np.arange(n)
T = n/Fs
frq = k/T # two sides frequency range
frq = frq[range(q)] # one side frequency range

freq = np.fft.fftfreq(n, d=Ts)
freq = freq[range(q)]

Y = np.fft.fft(data)/n  # FFT computing and normalisation
print(abs(Y[:10]))
Y = Y[range(q)]         # What is that doing ?
print(abs(Y[:10]))
real_Y = abs(Y)


threshold = 150
for i, d in enumerate(abs(Y)):
    if d >= threshold:
        peak = [i,d]
print("peak", peak)
freq_peak = frq[peak[0]]
print("frq peak", frq[peak[0]])


fig, ax = plt.subplots(2, 1)
ax[0].plot(data, "#00549F")
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Amplitude')
ax[1].plot(freq, abs(Y), '#A11035') # plotting the spectrum
ax[1].set_xlim(0,10000)
ax[1].axvline(freq_peak, color="#DAA520", linewidth=1, linestyle="--")
ax[1].set_xlabel('Freq (Hz)')
ax[1].set_ylabel('|Y(freq)|')
plt.savefig("/Users/roxanneturcotte/Dropbox/RWTH Aachen/EnEx/Resonnance_freq_DOM.svg")
#
#plot_url = py.plot_mpl(fig, filename='mpl-basic-fft')


#print(data)
#fft_out = fft(data)
#numfft = np.fft.ifft(data)
#plt.figure()
#plt.plot(np.abs(fft_out))
#plt.show()

#rate, data = wav.read("Resonnance.wav")
#fft_out = fft(data)
#numfft = np.fft.fft(data)
#plt.figure()
#plt.plot(np.abs(fft_out))
#plt.show()