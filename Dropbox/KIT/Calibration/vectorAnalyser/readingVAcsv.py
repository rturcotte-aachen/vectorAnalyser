#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:31:58 2019

@author: roxanneturcotte
"""
import numpy as np
import pandas as pd
mega = 10**(6)


def fromPowertoDb(value):
    return 20 * np.log10(value)


def fromDbtoPower(value):
    return 10 ** (value / 20)


def HztoMhz(freq):
    return freq*mega


def MhztoHz(freq):
    return freq/mega


class VectorAnalyser():
    def __init__(self):
        self.filename = ""
        self.path = ""
        self.amplitude = []
        self.frequency = []



    # Todo : split the file when there is more than one measurement
    def readCSV(self, path, filename):
        """reads the file and stock 2 arrays, frequency and amplitude"""
        self.path = path
        self.filname = filename
        data = pd.read_csv(path + filename, names=["freq", "amp"], comment="!", header=1, skipfooter=1)
        self.amplitude = data["amp"]
        self.frequency = data["freq"]
        return data


    def addPairsTogether(self, diffPairPositive, diffPairNegative):
        return fromPowertoDb(fromDbtoPower(diffPairPositive) + fromDbtoPower(diffPairNegative))


    def splitData(self, frequency, amplitude):
        # When array frequency gets same value, split ?
        return














    # ====================================
    # TO BE DELETED

    # def plotGain(self, ax, color="k", alpha=0.5, linestyle="--", label="placeHolder"):
    #     ax.plot(self.data["freq"]*mega, self.data["amp"], color=color, alpha=alpha, linestyle=linestyle, label=label)
    #     ax.set_xlabel("frequency [MHz]")
    #     ax.set_ylabel("gain [dB]")

#
# # MODIFIED FOR 4 DATASET
# def s11s21(data):
#     is_begin = data["freq"] == "BEGIN"
#     is_end = data["freq"] == "END"
#     end = data.index[is_end]
#     begin = data.index[is_begin]
#
#     for i, val in enumerate(begin):
#         if data["amp"][val-3] == "S11" and data["freq"][val-1] == "! DATA UNIT dB":
#             s11 = data[(val+1):(end[i]-1)]
#             s11['freq'] = s11['freq'].astype(float)
#             s11['amp'] = s11['amp'].astype(float)
#         elif data["amp"][val-3] == "S11" and data["freq"][val-1] == "! DATA UNIT Degrees":
#             p11 = data[(val+1):(end[i]-1)]
#             p11['freq'] = p11['freq'].astype(float)
#             p11['amp'] = p11['amp'].astype(float)
#         elif data["amp"][val-3] == "S21" and data["freq"][val-1] == "! DATA UNIT dB":
#             s21 = data[(val+1):(end[i]-1)]
#             s21['freq'] = s21['freq'].astype(float)
#             s21['amp'] = s21['amp'].astype(float)
#         elif data["amp"][val-3] == "S21" and data["freq"][val-1] == "! DATA UNIT Degrees":
#             p21 = data[(val+1):(end[i]-1)]
#             p21['freq'] = p21['freq'].astype(float)
#             p21['amp'] = p21['amp'].astype(float)
#     return s11, s21, p11, p21
#
#
#
# legendnames = []
# for file in files:
#     legendnames.append(file[7:-4]+" dB")
#
#
# # TEST
# file = "LNA_20_G.csv"
# #file = "LNA122_P-40.csv"
# data = pd.read_csv(file, names=["freq", "amp"])
# print(data.head(17))
# s11, s21, p11, p21 = s11s21(data)
#
# plt.figure()
# plt.plot(s11["freq"]*mega, s11["amp"])
# plt.figure()
# plt.plot(s21["freq"]*mega, s21["amp"])
# plt.figure()
# plt.plot(p11["freq"]*mega, p11["amp"])
# plt.figure()
# plt.plot(p21["freq"]*mega, p21["amp"])
#
# # Find column "amp" of value DATA Freq
# #13                           ! DATA Freq                        S21
# # is_spara = data["freq"] == "! DATA Freq"
# # print(data.loc[is_spara])
#
# # if data["freq"] == "! DATA Freq":
# #     print(data.index)
#
#
# #%%
#
# # setting the size of the fig. setting the style
#
# fig_s21,ax_s21 = plt.subplots()
# fig_s11,ax_s11 = plt.subplots()
# fig_p21,ax_p21 = plt.subplots()
# fig_p11,ax_p11 = plt.subplots()
# for name in files:
#     #print("in",files)
#     data = pd.read_csv(name, names=["freq", "amp"])
#     s11, s21, p11, p21 = s11s21(data)
#
#     #Transmission s21
#     ax_s21.plot(s21["freq"]*mega, s21["amp"])
#     ax_s21.set_xlabel("frequency [MHz]")
#     ax_s21.set_ylabel("amplitude [dB]")
#     ax_s21.set_title("%s Transmission S21" %files[0][0:6])
#     # ax_s21.legend(files)
#     # fig_s21.savefig("transmission_s21_%s" %path[:-1])
#     #Transmission s11
#     ax_s11.plot(s11["freq"]*mega, s11["amp"])
#     ax_s11.set_xlabel("frequency [MHz]")
#     ax_s11.set_ylabel("amplitude [dB]")
#     ax_s11.set_title("%s Transmission S11" %files[0][0:6])
#
#     #Phase s21
#     ax_p21.plot(p21["freq"]*mega, p21["amp"])
#     ax_p21.set_xlabel("frequency [MHz]")
#     ax_p21.set_ylabel("amplitude [dB]")
#     ax_p21.set_title("%s Phase S21" %files[0][0:6])
#     # ax_p21.legend(files)
#     # fig_p21.savefig("phase_s21_%s" %path[:-1])
#     #Phase s21
#     ax_p11.plot(p11["freq"]*mega, p11["amp"])
#     ax_p11.set_xlabel("frequency [MHz]")
#     ax_p11.set_ylabel("amplitude [dB]")
#     ax_p11.set_title("%s Phase S11" %files[0][0:6])
#
# # ax_s21.legend(legendnames)
# # fig_s21.savefig("%s_transmission_s21" %files[0][0:6])
# # ax_s21.legend(legendnames)
# # fig_s21.savefig("%s_transmission_s11" %files[0][0:6])
#
# # ax_p21.legend(legendnames, loc="upper right")
# # fig_p21.savefig("%s_phase_s21" %files[0][0:6])
# # ax_p21.legend(legendnames, loc="upper right")
# # fig_p21.savefig("%s_phase_s11" %files[0][0:6])
#
# # Removing the cable from the signal
# cable = "CABLES_PLOW.csv"
# pHigh = "LNA122_p-40.csv"
# data_cable = pd.read_csv(cable, names=["freq", "amp"])
# s11_cable, s21_cable, p11_cable, p21_cable = s11s21(data_cable)
#
# data_phigh = pd.read_csv(pHigh, names=["freq", "amp"])
# s11_phigh, s21_phigh, p11_phigh, p21_phigh = s11s21(data_phigh)
#
#
# fig, ax = plt.subplots()
# ax.plot(s21_phigh["freq"]*mega, s21_phigh["amp"]-s21_cable["amp"])
# ax.set_xlabel("frequency [MHz]")
# ax.set_ylabel("amplitude [dB]")
# ax.set_title("Transmission_s21_wocable_phigh")
# fig_s21.savefig("Transmission_s21_wocable_phigh")
#
# ax_s21.plot(s21_phigh["freq"]*mega, s21_phigh["amp"]-s21_cable["amp"])
# ax_s21.legend(legendnames)
# fig_s21.savefig("test")


# if __name__ == '__main__':
#     import glob
#     import matplotlib
#     import matplotlib.gridspec as gridspec
#     import skrf as rf
#
#     font = {'size': 16}
#
#     matplotlib.rc('font', **font)
#
#     path = "/Users/roxanneturcotte/Dropbox/KIT/Calibration/vectorAnalyser/"
#     folder = "10092020/"
#
#     va = VectorAnalyser()
    # for filename in glob.iglob(path+folder+"*.csv", recursive=True):
    #     filename = filename.split("/")[-1]
    #     print(filename)
    #     data = va.readCSV(path+folder, filename)
    #
    #     gs = gridspec.GridSpec(1, 1, wspace=0.2, hspace=0.3)
    #     fig = plt.figure(figsize=(8, 5.2))
    #     ax = fig.add_subplot(gs[0])
    #     va.plotGain(ax, color="k", alpha=0.5)
    #     ax.set_title(filename)
    #     plt.savefig(path+folder+"plot/"+filename.split(".")[-2], format="png")
    #     plt.close()

    # ulp_file = "/Users/roxanneturcotte/Dropbox/KIT/Hardware/radioTad-test/ULP-340+_S2P/ULP-340+_Plus25DegC.s2p"
    # ring_slot_ulp = rf.Network(ulp_file)
    #
    # sxhp_file = "/Users/roxanneturcotte/Dropbox/KIT/Hardware/radioTad-test/SXHP-48+_S2P/SXHP-48+_Plus25DegC.s2p"
    # ring_slot_sxhp = rf.Network(sxhp_file)

# # PLOT POLARISATION
#     gs = gridspec.GridSpec(1, 1, wspace=0.2, hspace=0.3)
#     fig = plt.figure(figsize=(8, 5.2))
#     ax = fig.add_subplot(gs[0])
#     data = va.readCSV(path+folder, "F_S_HP_RB11N.csv")
#     va.plotGain(ax, color="k", alpha=0.5, linestyle="-", label="pol. 1")
#     data = va.readCSV(path+folder, "F_S_HP_RB_11N.csv")
#     va.plotGain(ax, color="k", alpha=0.1, linestyle="-", label="pol. 1")
#     data = va.readCSV(path+folder, "F_S_HP_RB11P.csv")
#     va.plotGain(ax, color="r", alpha=0.5, linestyle="--", label="pol. 2")
#     data = va.readCSV(path+folder, "F_S_HP_RB_11P.csv")
#     va.plotGain(ax, color="r", alpha=0.1, linestyle="--", label="pol. 2")
#     #ax.set_title(filename)
#     ax.legend()
#     ax.set_ylim(-5, -2)
#     ax.set_xlim(40, 350)
#     plt.savefig(path+folder+"plot/twoPol2", format="png")
#     plt.close()
#
# # PLOT TOTAL GAIN
#     def plot_addedPairs(path, file1, file2):
#         gs = gridspec.GridSpec(1, 1, wspace=0.2, hspace=0.3)
#         fig = plt.figure(figsize=(8, 5.2))
#         ax = fig.add_subplot(gs[0])
#         dataPol1 = va.readCSV(path, file1)
#         #va.plotGain(ax, color="k", alpha=0.1, linestyle="-", label="pol. 1")
#         dataPol2 = va.readCSV(path, file2)
#         ax.plot(va.data["freq"], (20 * np.log10(10 ** (dataPol1["amp"] / 20) + 10 ** (dataPol2["amp"] / 20)))-3, linewidth=2)
#         # ax.plot(va.data["freq"] * mega, dataPol1["amp"]+dataPol2["amp"])
#
#         #ring_slot_ulp.frequency.unit = 'hz'
#         #ring_slot_ulp.plot_s_db(m=0, n=1)
#
#         #ring_slot_sxhp.frequency.unit = 'hz'
#         #ring_slot_sxhp.plot_s_db(m=0, n=1)
#
#         ax.set_xlabel("frequency [MHz]")
#         ax.set_ylabel("gain [dB]")
#         ax.set_ylim(-5, 10)
#         ax.set_xlim(30, 450)
#
#         #ax.set_ylim(0.2e8, 1)
#         #ax.set_xlim(0.3e8, 5e8)
#         #plt.tight_layout()
#         plt.savefig(path + "sumPairsZoom.png", format="png")

#
# path = "/Users/roxanneturcotte/Dropbox/KIT/Calibration/vectorAnalyser/radioBoard/"
# file1 = "B01_11P.csv"
# file2 = "B01_11N.csv"
# plot_addedPairs(path, file1, file2)
#
#     #ax.set_title(filename)
#     # ax.legend()
#     # ax.set_ylim(-5, -2)
#     # ax.set_xlim(40, 350)
#     # plt.savefig(path+folder+"plot/twoPol2", format="png")
#     # plt.close()
#
#
#
#
#
# # ADDING THEM TOGETHER
# "F_S_HP_RB11N"      # Measurement set 1
# "F_S_HP_RB11P"
#
# "F_S_HP_RB_11N"     # Measurement set 2
# "F_S_HP_RB_11P"
#
# # COMPARING SPLITTER OUTPUT
# "F_S4_HP_RB11N"
# "F_S3_HP_RB11N"
# "F_S2_HP_RB11N"
# "F_S_HP_RB11N"