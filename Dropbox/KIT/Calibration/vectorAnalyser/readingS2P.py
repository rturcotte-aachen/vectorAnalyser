import skrf as rf

class S2P:
    def __init__(self):
        self.path = ""
        self.filename = ""

    def readS2P(self, path, filename):
        return rf.Network(path + filename)

# todo : ok.... what to do here ?


