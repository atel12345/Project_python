# 📋 Project Club - Gestion de Club

Application de bureau pour gérer les membres, activités et participations d'un club.

## 🚀 Installation

```bash
python main.py
```

C'est tout ! Tkinter et SQLite sont inclus avec Python.

## 📁 Structure du Projet

```
Project_python/
├── main.py                 # Point d'entrée de l'application
├── model.py               # Modèles de données (Membre, Activite, Participation)
├── database.py            # Fonctions de requêtes
├── config.py              # Configuration
├── crud_operations.py     # Formulaires CRUD
├── ui_components.py       # Composants UI réutilisables
└── data.db               # Base de données SQLite (auto-créée)
```

## ✨ Fonctionnalités

- Gestion des membres (ajouter, modifier, supprimer, rechercher)
- Gestion des activités (types, durées)
- Suivi des participations (qui participe à quoi)
- Statistiques en temps réel
- Tri par colonnes (cliquer sur les en-têtes)
- Détails complets (double-clic sur une ligne)
- Suivi des paiements

## 🎯 Utilisation

### Membres

1. Cliquer **"Membre"** pour voir la liste
2. **"Ajouter Membre"** → Remplir le formulaire → **"Sauvegarder"**
3. **"Modifier Membre"** → Entrer ID → Modifier → **"Sauvegarder"**
4. **"Supprimer Membre"** → Entrer ID → **"Supprimer"**
5. **Double-clic** sur une ligne pour voir les détails complets

### Activités

1. Cliquer **"Activite"** pour changer de vue
2. **"Ajouter Activité"** → Remplir (ID, Nom, Type, Durée) → **"Sauvegarder"**
3. **Double-clic** pour voir les participants

### Participations

1. **"Ajouter Participation"**
2. Entrer: ID Membre, ID Activité, Date
3. **"Ajouter"**

### Tri

Cliquer sur n'importe quel en-tête de colonne (ID, Nom, Prenom, Role) pour trier.

## 🗄️ Schéma de Base de Données

### Table `membre`

- `id_membre` : Identifiant unique
- `nom_mbr` : Nom de famille
- `prenom_mbr` : Prénom
- `role_mbr` : Rôle (Membre, Président, Trésorier...)
- `payee_mbr` : Statut de paiement (0/1)
- `date_inscription_mbr` : Date d'inscription
- `num_tel_mbr` : Numéro de téléphone
- `email_mbr` : Email

### Table `activite`

- `id_activite` : Identifiant unique
- `nom_act` : Nom de l'activité
- `type_act` : Type (sport, culture...)
- `duree_act` : Durée en minutes

### Table `participation`

- `id_membre` : Référence au membre
- `id_activite` : Référence à l'activité
- `date` : Date de participation

**Relation:** Many-to-Many (0,n ↔ 0,n) entre MEMBRE et ACTIVITE via PARTICIPATION

## ⚙️ Configuration

Modifier `config.py` pour personnaliser:

```python
WINDOW_TITLE = "Project Club"    # Titre de la fenêtre
WINDOW_WIDTH = 1000               # Largeur
WINDOW_HEIGHT = 600               # Hauteur
DATABASE_NAME = 'data.db'         # Nom de la base de données
```

## 🔧 Dépannage

**Base de données verrouillée:** Fermer toutes les instances de l'application

**Tkinter non trouvé (Linux):**

```bash
sudo apt-get install python3-tk
```

## 📚 Concepts Utilisés

- **Tkinter:** Interface graphique (Treeview, LabelFrame, grid/pack layout)
- **SQLite:** Base de données (CRUD, clés étrangères)
- **POO Python:** Classes pour les modèles de données
- **Événements:** Double-clic, tri par colonnes
- **StringVar:** Mise à jour dynamique des statistiques

## 🐛 Problèmes Connus

- Pas de validation pour les IDs dupliqués
- Format de date non vérifié (utiliser YYYY-MM-DD)
- Fonction recherche affiche messagebox au lieu de filtrer

## 📝 Améliorations Futures

- [ ] Filtrage dans le Treeview
- [ ] Export CSV/Excel
- [ ] Validation des formulaires
- [ ] Photos des membres
- [ ] Sauvegarde/restauration
- [ ] Vue calendrier

---

**Projet d'apprentissage Python - Binôme scolaire**
