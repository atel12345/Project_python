"""
Configuration file for the Project Club application
Contains database settings and UI constants
"""

# Database configuration
DATABASE_NAME = 'data.db'

# Window configuration
WINDOW_TITLE = "Project Club"
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

# Tree configuration
TREE_HEIGHT = 10
LEFT_CONTAINER_WIDTH = 550

# Column widths (same for both trees for consistency)
COLUMN_WIDTHS = {
    'ID': 40,
    'Nom': 100,
    'Prenom': 100,
    'Role': 100,
    'Type': 100,
    'Duree (min)': 100
}

# Membre columns
MEMBRE_COLUMNS = ('ID', 'Nom', 'Prenom', 'Role')
MEMBRE_SORT_OPTIONS = {
    'ID': 'id_membre',
    'Nom': 'nom_mbr',
    'Prenom': 'prenom_mbr',
    'Role': 'role_mbr'
}

# Activite columns
ACTIVITE_COLUMNS = ('ID', 'Nom', 'Type', 'Duree (min)')
ACTIVITE_SORT_OPTIONS = {
    'ID': 'id_activite',
    'Nom': 'nom_act',
    'Type': 'type_act',
    'Duree (min)': 'duree_act'
}
