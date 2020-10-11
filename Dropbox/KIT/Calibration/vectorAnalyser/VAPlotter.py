import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

font = {'size': 16}
matplotlib.rc('font', **font)


""" THATS A MESS !!!!!!!!! """

class Plotter:
    def __int__(self, outpath="~/Documents/lostPlots/"):
        self.outpath = outpath

    def plotGainBasic(self, frequency, amplitude, ax, lim=[-50, 10], filename="gainPlot.pdf", color="k", alpha=0.5, linestyle="--", label="placeHolder"):
        gs = gridspec.GridSpec(1, 1, wspace=0.2, hspace=0.3)
        fig = plt.figure(figsize=(8, 5.2))
        ax = fig.add_subplot(gs[0])
        for i,  amplitude in enumerate(amplitude)
            ax.plot(frequency, amplitude, color=color, alpha=alpha, linestyle=linestyle, label=label)
        ax.set_xlabel("frequency / MHz")
        ax.set_ylabel("gain / dB")
        ax.set_ylim(lim)
        ax.legend()
        plt.savefig(outpath + filename)



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