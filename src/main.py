import toml
import tkinter
import os
import tkinter.ttk as ttk
import sv_ttk
import darkdetect
from config import *
from login import *
from PIL import Image, ImageTk

cfg = loadcfg()
#db = login(cfg)

win = tkinter.Tk()
demo = Image.open(cfg.incl+"/test.png")
demo = demo.resize((150,225))
demo = ImageTk.PhotoImage(demo)
ttk.Button(win,image=demo).pack()
#panel = tkinter.Frame(win)
#panel.pack()
#ttk.Button(panel,text="hello",style="Accent.TButton").pack()

icon = tkinter.PhotoImage(file=cfg.incl+"/icon.png")
win.iconphoto(True, icon)
sv_ttk.set_theme(darkdetect.theme())

tkinter.mainloop()
print("user quit")
