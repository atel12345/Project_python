import sqlite3

class Membre:
    def __init__(self, id_membre, nom_mbr, prenom_mbr, role_mbr, payee_mbr, date_inscription_mbr, num_tel_mbr, email_mbr=""):
        self.nom_mbr = nom_mbr
        self.prenom_mbr = prenom_mbr
        self.role_mbr = role_mbr
        self.id_membre = id_membre
        self.payee_mbr = payee_mbr
        self.date_inscription_mbr = date_inscription_mbr
        self.num_tel_mbr = num_tel_mbr
        self.email_mbr = email_mbr

    def ajouter_membre(self,membre):
        conn = sqlite3.connect('data.db')
        try:
            conn.execute('''
                INSERT INTO membre (id_membre, nom_mbr, prenom_mbr, role_mbr, payee_mbr, date_inscription_mbr, num_tel_mbr, email_mbr)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                (membre.id_membre, membre.nom_mbr, membre.prenom_mbr, membre.role_mbr, membre.payee_mbr, membre.date_inscription_mbr, membre.num_tel_mbr, membre.email_mbr)
            )
            conn.commit()
        finally:
            conn.close()

    def modifier_membre(self,membre):
        conn = sqlite3.connect('data.db')
        try:
            conn.execute('''
                UPDATE membre SET nom_mbr = ?, prenom_mbr = ?, role_mbr = ?, payee_mbr = ?, date_inscription_mbr = ?, num_tel_mbr = ?, email_mbr = ? 
                WHERE id_membre = ?''',
                (membre.nom_mbr, membre.prenom_mbr, membre.role_mbr, membre.payee_mbr, membre.date_inscription_mbr,
                 membre.num_tel_mbr, membre.email_mbr, membre.id_membre)
            )
            conn.commit()
        finally:
            conn.close()

    def supprimer_membre(self,id_membre):
        conn = sqlite3.connect('data.db')
        try:
            conn.execute('''
                DELETE FROM membre WHERE id_membre = ?''',(id_membre,)
            )
            conn.commit()
        finally:
            conn.close()

    def recherche_membre(self,id_membre):
        conn = sqlite3.connect('data.db')
        try:
            res = conn.execute('''
                SELECT id_membre, nom_mbr, prenom_mbr, role_mbr, payee_mbr, date_inscription_mbr, num_tel_mbr, email_mbr
                FROM membre WHERE id_membre = ?''',(id_membre,)
            )
            row = res.fetchone()
            return row if row else None
        finally:
            conn.close()

class Activite:
    def __init__(self, id_activite, nom_act, type_act, duree_act):
        self.nom_act = nom_act
        self.type_act = type_act
        self.duree_act = duree_act
        self.id_activite = id_activite

    def ajouter_activite(self, activite):
        conn = sqlite3.connect('data.db')
        try:
            conn.execute('''
                INSERT INTO activite (id_activite, nom_act, type_act, duree_act) 
                VALUES (?, ?, ?, ?)''',
                (activite.id_activite, activite.nom_act, activite.type_act, activite.duree_act)
            )
            conn.commit()
        finally:
            conn.close()

    def modifier_activite(self,activite):
        conn = sqlite3.connect('data.db')
        try:
            conn.execute('''
                UPDATE activite SET nom_act = ?, type_act = ?, duree_act = ? 
                WHERE id_activite = ?''',
                (activite.nom_act, activite.type_act, activite.duree_act, activite.id_activite)
            )
            conn.commit()
        finally:
            conn.close()

    def supprimer_activite(self,id_activite):
        conn = sqlite3.connect('data.db')
        try:
            conn.execute('''
                DELETE FROM activite WHERE id_activite = ?''',(id_activite,)
            )
            conn.commit()
        finally:
            conn.close()

    def recherche_activite(self,id_activite):
        conn = sqlite3.connect('data.db')
        try:
            res = conn.execute('''
                SELECT id_activite, nom_act, type_act, duree_act
                FROM activite WHERE id_activite = ?''',(id_activite,)
            )
            row = res.fetchone()
            return row if row else None
        finally:
            conn.close()

class Participation:
    def __init__(self, id_activite, id_membre, date):
        self.id_activite = id_activite
        self.id_membre = id_membre
        self.date = date

    def ajouter_participation(self, participation):
        conn = sqlite3.connect('data.db')
        try:
            conn.execute("PRAGMA foreign_keys = ON;")
            conn.execute('''
                INSERT INTO participation (id_activite, id_membre, date) 
                VALUES (?, ?, ?)''',
                (participation.id_activite, participation.id_membre, participation.date)
            )
            conn.commit()
        finally:
            conn.close()

    def supprimer_participation(self,id_activite,id_membre):
        conn = sqlite3.connect('data.db')
        try:
            conn.execute("PRAGMA foreign_keys = ON;")
            conn.execute('''
                DELETE FROM participation WHERE id_activite = ? AND id_membre = ?''',
                (id_activite,id_membre)
            )
            conn.commit()
        finally:
            conn.close()

# Database initialization - create tables if they don't exist
conn = sqlite3.connect('data.db')
conn.execute("PRAGMA foreign_keys = ON;")

#creating tables if they don't exist
conn.execute('''
    CREATE TABLE IF NOT EXISTS membre
    (id_membre integer primary key,
    nom_mbr text, prenom_mbr text, role_mbr text, payee_mbr boolean, date_inscription_mbr date, num_tel_mbr text, email_mbr text)
''')
conn.execute('''
    CREATE TABLE IF NOT EXISTS activite(
    id_activite integer primary key, nom_act text, type_act text, duree_act integer)
''')
conn.execute('''
    CREATE TABLE IF NOT EXISTS participation(
    id_activite integer, id_membre integer, date date, 
    primary key(id_membre,id_activite), 
    foreign key (id_membre) references membre(id_membre),
    foreign key (id_activite) references activite(id_activite))
''')

def is_table_empty(table_name):
    """Return True if the given table has no rows, False otherwise"""
    cursor = conn.execute(f"SELECT COUNT(*) FROM {table_name}")
    count = cursor.fetchone()[0]
    return count == 0
