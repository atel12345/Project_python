import sqlite3

class Membre:
    def __init__(self, id_membre,nom, prenom,role,payee,date_inscription,tel):
        self.nom = nom
        self.prenom = prenom
        self.role = role
        self.id_membre = id_membre
        self.payee = payee
        self.date_inscription = date_inscription
        self.tel = tel


    def ajouter_membre(self,membre):
        conn.execute(
            'INSERT INTO membre (id_membre, nom, prenom, role, payee, date_inscription,tel) VALUES (?, ?, ?, ?, ?, ?)',
            (membre.id_membre, membre.nom, membre.prenom, membre.role, membre.payee, membre.date_inscription, membre.tel)
        )
        conn.commit()


class Activite:
    def __init__(self, id_activite,nom,type,date,duree):
        self.nom = nom
        self.type = type
        self.duree = duree
        self.date = date
        self.id_activite = id_activite

class Paiement:
    def __init__(self, id_paiement, id_membre, montant, date_paiement):
        self.id_paiement = id_paiement
        self.id_membre = id_membre
        self.montant = montant
        self.date_paiement = date_paiement

conn=sqlite3.connect('data.db')
conn.execute('CREATE TABLE IF NOT EXISTS membre(id_membre integer primary key,nom text, prenom text,role text,payee boolean,date_inscription date)')
mem=Membre(17,'1','1','1','0','15/02/2003')
mem.ajouter_membre(mem)
conn.commit()
