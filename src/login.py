from steamgrid import SteamGridDB
import sys
import tkinter.simpledialog as dlg
def login(cfg):
	while True:
            sgdb = SteamGridDB(cfg.data["steamgrid"]["key"])
            try:
                sgdb.get_game_by_gameid(1)
                break
            except:
                pass
            newkey = dlg.askstring("log in","please login with your SteamGridDB key\n(https://www.steamgriddb.com/profile/preferences/api)")
            if newkey == None:
                print("user canceled login")
                sys.exit(0)
            cfg.data["steamgrid"]["key"] = newkey
            cfg.save()
            return sgdb
