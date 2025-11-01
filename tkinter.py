import sqlite3
from model import Membre, Activite

mem=Membre('1','5','50','5','5','5','5')
mem.modifier_membre(mem)
act=Activite('1','2','2','2')
act.ajouter_activite(act)