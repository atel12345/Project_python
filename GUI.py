import sqlite3
from tkinter import *
from model import Membre, Activite, Participation
mem=Membre('1','1','1','1','1','0','1')
act=Activite('1','1','a',1)
r=mem.recherche_membre('0')
print(r)
u=act.recherche_activite('1')
print(u)
# window=Tk()
# window.title('information')
# window.geometry("300x300")
# window.minsize(100,100)
# window.iconbitmap("icon.ico")
# window.mainloop()