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
        conn.execute('''
            INSERT INTO membre (id_membre, nom, prenom, role, payee, date_inscription,tel)
            VALUES (?, ?, ?, ?, ?, ?, ?)''',
            (membre.id_membre, membre.nom, membre.prenom, membre.role, membre.payee, membre.date_inscription, membre.tel)
        )
        conn.commit()

    def modifier_membre(self,membre):
        conn.execute('''
            UPDATE membre SET nom = ?, prenom = ?, role = ?, payee = ?, date_inscription = ?, tel = ? 
            WHERE id_membre = ?''',
            (membre.nom, membre.prenom, membre.role, membre.payee, membre.date_inscription,
             membre.tel, membre.id_membre)
        )
        conn.commit()

    def supprimer_membre(self,id_membre):
        conn.execute('''
            DELETE FROM membre WHERE id_membre = ?''',(id_membre,)
        )
        conn.commit()

    def recherche_membre(self,id_membre):
        res =(
        conn.execute('''
        SELECT id_membre, nom, prenom, role, payee, date_inscription,tel
        FROM membre WHERE id_membre = ?''',(id_membre,)
        ))
        row = res.fetchone()
        if row:
            return row
        else:
            return None

class Activite:
    def __init__(self, id_activite,nom,type,duree):
        self.nom = nom
        self.type = type
        self.duree = duree
        self.id_activite = id_activite

    def ajouter_activite(self, activite):
        conn.execute('''
            INSERT INTO activite (id_activite,nom,type,duree) 
            VALUES (?, ?, ?, ?)''',
            (activite.id_activite,activite.nom,activite.type,activite.duree)
        )
        conn.commit()

    def modifier_activite(self,activite):
        conn.execute('''
            UPDATE activite SET nom = ?, type = ?, duree = ? 
            WHERE id_activite = ?''',
            (activite.nom,activite.type,activite.duree,activite.id_activite)
        )
        conn.commit()

    def supprimer_activite(self,id_activite):
        conn.execute('''
            DELETE FROM activite WHERE id_activite = ?''',(id_activite,)
        )
        conn.commit()

    def recherche_activite(self,id_activite):
        res =(
        conn.execute('''
        SELECT id_activite,nom,type,duree
        FROM activite WHERE id_activite = ?''',(id_activite,)
        ))
        row = res.fetchone()
        if row:
            return row
        else:
            return None

class Participation:
    def __init__(self, id_activite, id_membre, date_participation):
        self.id_activite = id_activite
        self.id_membre = id_membre
        self.date_participation = date_participation

    def ajouter_participation(self, participation):
        conn.execute('''
            INSERT INTO participation (id_activite,id_membre,date_participation) 
            VALUES (?, ?, ?)''',
            (participation.id_activite,participation.id_membre,participation.date_participation)
        )
        conn.commit()

    def supprimer_participation(self,id_activite,id_membre):
        conn.execute('''
            DELETE FROM participation WHERE id_activite = ? AND id_membre = ?''',
            (id_activite,id_membre)
        )
        conn.commit()

#connecting to DB and enabling foreign keys
conn=sqlite3.connect('data.db')
conn.execute("PRAGMA foreign_keys = ON;")

#creating tables if they don't exist
conn.execute('''
    CREATE TABLE IF NOT EXISTS membre
    (id_membre integer primary key,
    nom text, prenom text,role text,payee boolean,date_inscription date,tel text)
''')
conn.execute('''
    CREATE TABLE IF NOT EXISTS activite(
    id_activite integer primary key,nom text,type text,duree integer)
''')
conn.execute('''
    CREATE TABLE IF NOT EXISTS participation(
    id_activite integer , id_membre integer,date_participation date, 
    primary key(id_membre,id_activite), 
    foreign key (id_membre) references membre(id_membre),
    foreign key (id_activite) references activite(id_activite))
''')


#adding member infos to table membre
# print("\nSaisis info membre :")
# id_m = int(input("id_membre: "))
# nom = input("nom: ")
# prenom = input("prenom: ")
# role = input("role: ")
# payee_input = input("payee (oui/non): ").strip().lower()
# payee = True if payee_input in ("oui", "yes", "1", "true") else False
# date_inscription = input("date_inscription (JJ/MM/AAAA): ")
# telephone = input("telephone: ")
# mem = Membre(id_m, nom, prenom, role, payee, date_inscription, telephone)
# mem.ajouter_membre(mem)

#adding activity infos to table activite
# print("\nSaisis info activite :")
# id_a = int(input("id_activite: "))
# n = input("nom: ")
# type = input("type: ")
# date=input("date: ")
# duree=int(input("duree: "))
# act=Activite(id_a,n,type,date,duree)
# act.ajouter_activite(act)

#adding payment infos to table paiement
# print("\nSaisis info paiement :")
# id_p = int(input("id_paiement: "))
# montant = float(input("montant: "))
# date_paiement = input("date_paiement (JJ/MM/AAAA): ")
# pai=Paiement(id_p,id_m,montant,date_paiement)#id_m : id_membre as foreign key referencing id_membre in table membre
# pai.ajouter_paiement(pai)
