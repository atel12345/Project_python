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
        conn = sqlite3.connect('data.db')
        try:
            conn.execute('''
                INSERT INTO membre (id_membre, nom, prenom, role, payee, date_inscription,tel)
                VALUES (?, ?, ?, ?, ?, ?, ?)''',
                (membre.id_membre, membre.nom, membre.prenom, membre.role, membre.payee, membre.date_inscription, membre.tel)
            )
            conn.commit()
        finally:
            conn.close()

    def modifier_membre(self,membre):
        conn = sqlite3.connect('data.db')
        try:
            conn.execute('''
                UPDATE membre SET nom = ?, prenom = ?, role = ?, payee = ?, date_inscription = ?, tel = ? 
                WHERE id_membre = ?''',
                (membre.nom, membre.prenom, membre.role, membre.payee, membre.date_inscription,
                 membre.tel, membre.id_membre)
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
                SELECT id_membre, nom, prenom, role, payee, date_inscription,tel
                FROM membre WHERE id_membre = ?''',(id_membre,)
            )
            row = res.fetchone()
            return row if row else None
        finally:
            conn.close()

class Activite:
    def __init__(self, id_activite,nom,type,duree):
        self.nom = nom
        self.type = type
        self.duree = duree
        self.id_activite = id_activite

    def ajouter_activite(self, activite):
        conn = sqlite3.connect('data.db')
        try:
            conn.execute('''
                INSERT INTO activite (id_activite,nom,type,duree) 
                VALUES (?, ?, ?, ?)''',
                (activite.id_activite,activite.nom,activite.type,activite.duree)
            )
            conn.commit()
        finally:
            conn.close()

    def modifier_activite(self,activite):
        conn = sqlite3.connect('data.db')
        try:
            conn.execute('''
                UPDATE activite SET nom = ?, type = ?, duree = ? 
                WHERE id_activite = ?''',
                (activite.nom,activite.type,activite.duree,activite.id_activite)
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
                SELECT id_activite,nom,type,duree
                FROM activite WHERE id_activite = ?''',(id_activite,)
            )
            row = res.fetchone()
            return row if row else None
        finally:
            conn.close()

class Participation:
    def __init__(self, id_activite, id_membre, date_participation):
        self.id_activite = id_activite
        self.id_membre = id_membre
        self.date_participation = date_participation

    def ajouter_participation(self, participation):
        conn = sqlite3.connect('data.db')
        try:
            conn.execute("PRAGMA foreign_keys = ON;")
            conn.execute('''
                INSERT INTO participation (id_activite,id_membre,date_participation) 
                VALUES (?, ?, ?)''',
                (participation.id_activite,participation.id_membre,participation.date_participation)
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
def is_table_empty(table_name):
    """Return True if the given table has no rows, False otherwise"""
    cursor = conn.execute(f"SELECT COUNT(*) FROM {table_name}")
    count = cursor.fetchone()[0]
    return count == 0

