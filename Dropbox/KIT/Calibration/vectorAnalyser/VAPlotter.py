import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

font = {'size': 16}
matplotlib.rc('font', **font)


def plotGain(self, ax, color="k", alpha=0.5, linestyle="--", label="placeHolder"):
    ax.plot(self.data["freq"] * mega, self.data["amp"], color=color, alpha=alpha, linestyle=linestyle, label=label)
    ax.set_xlabel("frequency [MHz]")
    ax.set_ylabel("gain [dB]")

