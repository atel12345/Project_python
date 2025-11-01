"""
Database operations for the Project Club application
Handles all database queries and data retrieval
"""

import sqlite3
from config import DATABASE_NAME


def get_membres(search_text="", sort_by="id_membre"):
    """
    Fetch membres from database with optional search and sort
    
    Args:
        search_text: Text to search in nom_mbr, prenom_mbr, role_mbr
        sort_by: Database column name to sort by
    
    Returns:
        List of tuples containing membre data
    """
    conn = sqlite3.connect(DATABASE_NAME)
    query = 'SELECT id_membre, nom_mbr, prenom_mbr, role_mbr FROM membre'
    params = []
    
    if search_text:
        try:
            search_id = int(search_text)
            query += ' WHERE id_membre = ?'
            params = [search_id]
        except ValueError:
            query += ' WHERE nom_mbr LIKE ? OR prenom_mbr LIKE ? OR role_mbr LIKE ?'
            search_pattern = f'%{search_text}%'
            params = [search_pattern, search_pattern, search_pattern]
    
    query += f' ORDER BY {sort_by}'
    cursor = conn.execute(query, params)
    results = cursor.fetchall()
    conn.close()
    
    return results


def get_activites(search_text="", sort_by="id_activite"):
    """
    Fetch activites from database with optional search and sort
    
    Args:
        search_text: Text to search in nom_act, type_act
        sort_by: Database column name to sort by
    
    Returns:
        List of tuples containing activite data
    """
    conn = sqlite3.connect(DATABASE_NAME)
    query = 'SELECT id_activite, nom_act, type_act, duree_act FROM activite'
    params = []
    
    if search_text:
        try:
            search_id = int(search_text)
            query += ' WHERE id_activite = ?'
            params = [search_id]
        except ValueError:
            query += ' WHERE nom_act LIKE ? OR type_act LIKE ?'
            search_pattern = f'%{search_text}%'
            params = [search_pattern, search_pattern]
    
    query += f' ORDER BY {sort_by}'
    cursor = conn.execute(query, params)
    results = cursor.fetchall()
    conn.close()
    
    return results


def get_membre_details(membre_id):
    """Get full details of a specific membre"""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.execute(
        'SELECT id_membre, nom_mbr, prenom_mbr, role_mbr, payee_mbr, date_inscription_mbr, num_tel_mbr, email_mbr FROM membre WHERE id_membre = ?',
        (membre_id,)
    )
    result = cursor.fetchone()
    conn.close()
    return result


def get_activite_details(activite_id):
    """Get full details of a specific activite"""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.execute(
        'SELECT id_activite, nom_act, type_act, duree_act FROM activite WHERE id_activite = ?',
        (activite_id,)
    )
    result = cursor.fetchone()
    conn.close()
    return result


def get_membre_activities(membre_id):
    """Get all activities a membre participated in"""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.execute('''
        SELECT a.nom_act, a.type_act, p.date 
        FROM participation p
        JOIN activite a ON p.id_activite = a.id_activite
        WHERE p.id_membre = ?
    ''', (membre_id,))
    results = cursor.fetchall()
    conn.close()
    return results


def get_activite_participants(activite_id):
    """Get all participants of an activite"""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.execute('''
        SELECT m.nom_mbr, m.prenom_mbr, m.role_mbr, p.date
        FROM participation p
        JOIN membre m ON p.id_membre = m.id_membre
        WHERE p.id_activite = ?
    ''', (activite_id,))
    results = cursor.fetchall()
    conn.close()
    return results


def get_participation_count(membre_id):
    """Get count of activities a membre participated in"""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.execute(
        'SELECT COUNT(*) FROM participation WHERE id_membre = ?',
        (membre_id,)
    )
    count = cursor.fetchone()[0]
    conn.close()
    return count


def get_participants_count(activite_id):
    """Get count of participants in an activite"""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.execute(
        'SELECT COUNT(*) FROM participation WHERE id_activite = ?',
        (activite_id,)
    )
    count = cursor.fetchone()[0]
    conn.close()
    return count


def get_kpi_data():
    """
    Get KPI statistics
    
    Returns:
        Tuple of (total_membres, total_activites, non_payers)
    """
    conn = sqlite3.connect(DATABASE_NAME)
    
    cursor = conn.execute('SELECT COUNT(*) FROM membre')
    total_membres = cursor.fetchone()[0]
    
    cursor = conn.execute('SELECT COUNT(*) FROM activite')
    total_activites = cursor.fetchone()[0]
    
    cursor = conn.execute('SELECT COUNT(*) FROM membre WHERE payee_mbr = 0')
    non_payers = cursor.fetchone()[0]
    
    conn.close()
    return total_membres, total_activites, non_payers
