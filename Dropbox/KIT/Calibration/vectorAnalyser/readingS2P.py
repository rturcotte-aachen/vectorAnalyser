import skrf as rf
path = "/Users/roxanneturcotte/Dropbox/KIT/Calibration/LNA/"
folder = "BOT/"

for filename in glob.iglob(path + folder + '*.s2p', recursive=True):
    filename = filename.split("/")[-1]
    print(filename)
    lna = rf.Network(path + folder + filename)
    lna.plot_s_db(m=1, n=0)

filename = "S-Parameter_LNA.s2p"
lna = rf.Network(path + filename)
lna.plot_s_db(m=1, n=0)