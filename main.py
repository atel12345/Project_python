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
            'INSERT INTO membre (id_membre, nom, prenom, role, payee, date_inscription,tel) VALUES (?, ?, ?, ?, ?, ?, ?)',
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

    def ajouter_activite(self, activite):
        conn.execute(
            'INSERT INTO activite (id_activite,nom,type,date,duree) VALUES (?, ?, ?, ?, ?)',
            (activite.id_activite,activite.nom,activite.type,activite.date,activite.duree)
        )
        conn.commit()

class Paiement:
    def __init__(self, id_paiement, id_membre, montant, date_paiement):
        self.id_paiement = id_paiement
        self.id_membre = id_membre
        self.montant = montant
        self.date_paiement = date_paiement

conn=sqlite3.connect('data.db')
conn.execute(
    'CREATE TABLE IF NOT EXISTS membre(id_membre integer primary key,nom text, prenom text,role text,payee boolean,date_inscription date,tel text)'
)
conn.execute(
    'CREATE TABLE IF NOT EXISTS activite(id_activite integer primary key,nom text,type text,date date,duree integer)'
)
print("Saisis info membre :\n")
id_m = int(input("id_membre: "))
nom = input("nom: ")
prenom = input("prenom: ")
role = input("role: ")
payee_input = input("payee (oui/non): ").strip().lower()
payee = True if payee_input in ("oui", "yes", "1", "true") else False
date_inscription = input("date_inscription (JJ/MM/AAAA): ")
telephone = input("telephone: ")
mem = Membre(id_m, nom, prenom, role, payee, date_inscription, telephone)
mem.ajouter_membre(mem)
print("Saisis info activite :\n")
id_a = int(input("id_activite: "))
n = input("nom: ")
type = input("type: ")
date=input("date: ")
duree=int(input("duree: "))
act=Activite(id_a,n,type,date,duree)
act.ajouter_activite(act)
conn.commit()
