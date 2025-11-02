import sqlite3
from config import DATABASE_NAME

def get_membres(search_text="", sort_by="id_membre"):
    conn = sqlite3.connect(DATABASE_NAME)
    query = f'SELECT id_membre, nom_mbr, prenom_mbr, role_mbr FROM membre ORDER BY {sort_by}'
    cursor = conn.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


def get_activites(search_text="", sort_by="id_activite"):
    conn = sqlite3.connect(DATABASE_NAME)
    query = f'SELECT id_activite, nom_act, type_act, duree_act FROM activite ORDER BY {sort_by}'
    cursor = conn.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


def get_membre_details(membre_id):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.execute('SELECT id_membre, nom_mbr, prenom_mbr, role_mbr, payee_mbr, date_inscription_mbr, num_tel_mbr, email_mbr FROM membre WHERE id_membre = ?', (membre_id,))
    result = cursor.fetchone()
    conn.close()
    return result

def get_activite_details(activite_id):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.execute('SELECT id_activite, nom_act, type_act, duree_act FROM activite WHERE id_activite = ?', (activite_id,))
    result = cursor.fetchone()
    conn.close()
    return result

def get_membre_activities(membre_id):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.execute('SELECT a.nom_act, a.type_act, p.date FROM participation p JOIN activite a ON p.id_activite = a.id_activite WHERE p.id_membre = ?', (membre_id,))
    results = cursor.fetchall()
    conn.close()
    return results

def get_activite_participants(activite_id):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.execute('SELECT m.nom_mbr, m.prenom_mbr, m.role_mbr, p.date FROM participation p JOIN membre m ON p.id_membre = m.id_membre WHERE p.id_activite = ?', (activite_id,))
    results = cursor.fetchall()
    conn.close()
    return results

def get_participation_count(membre_id):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.execute('SELECT COUNT(*) FROM participation WHERE id_membre = ?', (membre_id,))
    count = cursor.fetchone()[0]
    conn.close()
    return count

def get_participants_count(activite_id):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.execute('SELECT COUNT(*) FROM participation WHERE id_activite = ?', (activite_id,))
    count = cursor.fetchone()[0]
    conn.close()
    return count

def get_kpi_data():
    conn = sqlite3.connect(DATABASE_NAME)
    total_membres = conn.execute('SELECT COUNT(*) FROM membre').fetchone()[0]
    total_activites = conn.execute('SELECT COUNT(*) FROM activite').fetchone()[0]
    non_payers = conn.execute('SELECT COUNT(*) FROM membre WHERE payee_mbr = 0').fetchone()[0]
    conn.close()
    return total_membres, total_activites, non_payers
