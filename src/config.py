import os
import toml
import sys
from pathlib import Path
def lzymkdir(dirs):
    try:
        os.makedirs(dirs)
        print("created dir "+dirs)
    except:
        print("skipped mdkir "+dirs)
def autoload(cfg):
    if not os.path.exists(cfg):
        fc = open(cfg,"w")
        fc.write("[systems]\ninstalled = [\"linux\"]\n[games]\ninstalled=[]\ncovers={}\n[steamgrid]\nkey = \"invalid\"")
        fc.close()
        print("auto generated config "+cfg)
    else:
        print("found config "+cfg)
    return toml.load(open(cfg,"r"))
class Config:
    path = None
    data = None
    home = None
    incl = None
    def __init__(self,file):
        try:
            self.incl = sys._MEIPASS
            print("using sys._MEIPASS for data")
        except:
            self.incl = "./data"
            print("using relative data directory as data path")
        self.path = os.path.dirname(os.path.realpath(file))
        self.home = self.path+"/.cabinets"
        lzymkdir(self.home+"/covers")
        lzymkdir(self.home+"/systems")
        self.data = autoload(self.home+"/cfg.toml")
    def save(self):
        toml.dump(self.data, open(self.home+"/cfg.toml","w"))
        print("updated config "+self.home+"/cfg.toml")
def loadcfg():
    if getattr(sys,"frozen",False):
        print("frozen python detected using sys.executable")
        cfg = Config(sys.executable)
    else:
        print("unfrozen python using __file__")
        cfg = Config(__file__)
    return cfg
