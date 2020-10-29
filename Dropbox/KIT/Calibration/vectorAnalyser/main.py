import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import VAPlotter
import readingVAcsv
import os
import glob

import pylab as plot
params = {'legend.fontsize': 8,
          'legend.handlelength': 1}
plot.rcParams.update(params)

"""Vector analyser data"""
path = "/Users/roxanneturcotte/Dropbox/KIT/Calibration/vectorAnalyser/"
folder = "10092020/"
folder = "14102020/"
#folder = "15102020/"
#folder = "16102020/"
folder = "20102020/"
#folder = "27102020/"

outpath = path+folder+"plot/"
name = 'RT*.csv'

def mean_amplitude(path, folder, name, gain=True):
    val = readingVAcsv.isGain(gain)
    amplitudes = []
    for filename in glob.iglob(path + folder + name, recursive=True):
        filename = filename.split("/")[-1]
        print(filename)
        va = readingVAcsv.VectorAnalyser(path + folder, filename)
        amplitudes.append(va.amplitude[val])
    return np.mean(np.array(amplitudes), axis=0)

mean_gain = mean_amplitude(path, folder, name)
VAPlotter.plot_differences(va, mean_gain, lim_x=[0, 450], lim_y=[-185, 185]):


fig = plt.figure(figsize=(8, 5.2))
gs = gridspec.GridSpec(1, 1, wspace=0.2, hspace=0.3)
ax = fig.add_subplot(gs[0])
for filename in glob.iglob(path + folder + name, recursive=True):
    filename = filename.split("/")[-1]
    print(filename)
    va = readingVAcsv.VectorAnalyser(path + folder, filename)
    ax = VAPlotter.plot_gain(ax, va, lim_x=[0, 450], lim_y=[-20, 5])
ax.legend(loc="lower right", ncol=4)
fig.savefig(outpath + "gain_"+name.split(".")[0]+".pdf")
plt.close()


fig = plt.figure(figsize=(8, 5.2))
gs = gridspec.GridSpec(1, 1, wspace=0.2, hspace=0.3)
ax = fig.add_subplot(gs[0])
for filename in glob.iglob(path + folder + name, recursive=True):
    filename = filename.split("/")[-1]
    print(filename)
    va = readingVAcsv.VectorAnalyser(path + folder, filename)
    ax = VAPlotter.plot_phase(ax, va, lim_x=[0, 450], lim_y=[-185, 185])
ax.legend(loc="lower right", ncol=4)
fig.savefig(outpath + "phase_"+name.split(".")[0]+".pdf")
plt.close()


# filename1 = "GAPH_RTV2_06_12P.csv"
# va1 = readingVAcsv.VectorAnalyser(path+folder, filename1)
# name = "GAPH_RTV2_06_*P.csv"
# # PHASE
# # =============================
# files = []
# fig = plt.figure(figsize=(8, 5.2))
# gs = gridspec.GridSpec(1, 1, wspace=0.2, hspace=0.3)
# # ax = fig.add_subplot(gs[0])
# ax = fig.add_subplot(gs[0])
#
#
# for filename in glob.iglob(path + folder + name, recursive=True):
#     filename = filename.split("/")[-1]
#     print(filename)
#     files = np.append(files, filename)
#
#     va = readingVAcsv.VectorAnalyser(path+folder, filename)
#     print(va.amplitude)
#     ax = fig.add_subplot(gs[0])
#     ax.plot(va.frequency[1], va1.amplitude[1] - va.amplitude[1], label=filename)
#
# ax.set_ylabel("phase / degree")
# ax.set_xlabel("frequency / MHz")
# ax.set_ylim(-10, 10)
# ax.set_xlim(70, 400)
# #ax.axhline(0, color="black", ls="--", linewidth=2)
# ax.legend(loc="lower right", ncol=4)
# fig.savefig(outpath + "phaseDiff_"+name.split(".")[0]+".pdf")
#
# plt.close()
#
#
#
# filename1 = "GAPH_RTV2_06_12P.csv"
# va1 = readingVAcsv.VectorAnalyser(path+folder, filename1)
# name = "GAPH_RTV2_06_*.csv"
# # PHASE
# # =============================
# files = []
# fig = plt.figure(figsize=(8, 5.2))
# gs = gridspec.GridSpec(1, 1, wspace=0.2, hspace=0.3)
# # ax = fig.add_subplot(gs[0])
# ax = fig.add_subplot(gs[0])
#
#
# for filename in glob.iglob(path + folder + name, recursive=True):
#     filename = filename.split("/")[-1]
#     print(filename)
#     files = np.append(files, filename)
#
#     va = readingVAcsv.VectorAnalyser(path+folder, filename)
#     print(va.amplitude)
#     ax = fig.add_subplot(gs[0])
#     ax.plot(va.frequency[0], va1.amplitude[0] - va.amplitude[0], label=filename)
#
# ax.set_ylabel("gain / dB")
# ax.set_xlabel("frequency / MHz")
# ax.set_ylim(-1, 1)
# ax.set_xlim(70, 400)
# #ax.axhline(0, color="black", ls="--", linewidth=2)
# ax.legend(loc="lower right", ncol=4)
# fig.savefig(outpath + "gainDiff_"+name.split(".")[0]+".pdf")
#
# plt.close()



# files = []
# fig = plt.figure(figsize=(8, 5.2))
# gs = gridspec.GridSpec(1, 1, wspace=0.2, hspace=0.3)
# ax = fig.add_subplot(gs[0])
#
# for filename in glob.iglob(path + folder + 'PHASE*N.csv', recursive=True):
#     filename = filename.split("/")[-1]
#     print(filename)
#     files = np.append(files, filename)
#
#     va = readingVAcsv.VectorAnalyser(path+folder, filename)
#     print(va.amplitude)
#     ax.plot(va.frequency[0], va.amplitude[0], label=filename)
# ax.set_ylabel("phase / degree")
# ax.set_xlabel("frequency / MHz")
# #ax.set_ylim(-20, 5)
# ax.set_xlim(20, 450)
# ax.axhline(0)
# ax.legend(loc="lower right", ncol=4)
# fig.savefig(outpath + "phase_pol2_N_45V.pdf")
#
#
# """Data for the radioTad components"""
# path = "/Users/roxanneturcotte/Dropbox/KIT/Hardware/radioTad-test/"
# ulp_file = "ULP-340+_S2P/ULP-340+_Plus25DegC.s2p"
# sxhp_file = "SXHP-48+_S2P/SXHP-48+_Plus25DegC.s2p"

