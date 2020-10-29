import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec
import matplotlib
import readingVAcsv

font = {'size': 16}
matplotlib.rc('font', **font)


def plot_gain(ax, va, lim_x=[0, 450], lim_y=[-20, 5]):
    ax.plot(va.frequency[0], va.amplitude[0], label=va.filename)
    ax.set_ylabel("gain / dB")
    ax.set_xlabel("frequency / MHz")
    ax.set_ylim(lim_y)
    ax.set_xlim(lim_x)
    return ax

def plot_phase(ax, va, lim_x=[0, 450], lim_y=[-185, 185]):
    ax.plot(va.frequency[1], va.amplitude[1], label=va.filename)
    ax.set_ylabel("phase / degree")
    ax.set_xlabel("frequency / MHz")
    ax.set_ylim(lim_y)
    ax.set_xlim(lim_x)
    return ax

def plot_diffpairs_together(va_N, va_P, lim_x=[0, 450], lim_y=[-185, 185]):
    totalAmp = readingVAcsv.addPairsTogether(va_N.amplitude, va_P.amplitude)
    ax.plot(va_N.frequency[0], totalAmp, label=va_N.filename)
    ax.set_ylabel("gain / dB")
    ax.set_xlabel("frequency / MHz")
    ax.set_ylim(lim_y)
    ax.set_xlim(lim_x)
    return ax


def plot_differences(va, mean_amplitude, lim_x=[0, 450], lim_y=[-185, 185], gain=True):
    val = readingVAcsv.isGain(gain)
    ax.plot(va_N.frequency[val], va.amplitude[val] - mean_amplitude, label=va.filename)
    if val == 0:
        ax.set_ylabel("gain / dB")
    elif val ==1:
        ax.set_ylabel("phase / degree")
    ax.set_xlabel("frequency / MHz")
    ax.set_ylim(lim_y)
    ax.set_xlim(lim_x)
    return

