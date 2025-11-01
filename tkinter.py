import sqlite3
from model import Membre, Activite, Paiement

mem=Membre('1','5','50','5','5','5','5')
mem.modifier_membre(mem)
act=Activite('1','2','2','2','2')
act.modifier_activite(act)
pai=Paiement('1','1','1','1')
pai.ajouter_paiement(pai)