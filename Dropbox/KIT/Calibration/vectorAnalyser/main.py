import numpy as np
import VAPlotter as vaplt
import readingVAcsv
import os
import glob

"""Vector analyser data"""
path = "/Users/roxanneturcotte/Dropbox/KIT/Calibration/vectorAnalyser/"
folder = "10092020/"
folder = "13102020/"

filename = "GP_24P_5V.csv"

va = readingVAcsv.VectorAnalyser(path+folder, filename)


"""Data for the radioTad components"""
path = "/Users/roxanneturcotte/Dropbox/KIT/Hardware/radioTad-test/"
ulp_file = "ULP-340+_S2P/ULP-340+_Plus25DegC.s2p"
sxhp_file = "SXHP-48+_S2P/SXHP-48+_Plus25DegC.s2p"

