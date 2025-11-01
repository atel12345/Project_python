"""
UI Components for the Project Club application
Contains reusable UI elements and popup windows
"""

from tkinter import *
from tkinter import ttk
import webbrowser
from database import *
from config import *


def create_treeview(parent, columns):
    """
    Create a configured treeview widget
    
    Args:
        parent: Parent widget
        columns: Tuple of column names
    
    Returns:
        Treeview widget
    """
    tree = ttk.Treeview(parent, show='headings', height=TREE_HEIGHT)
    tree['columns'] = columns
    
    # Configure columns
    for col in columns:
        tree.heading(col, text=col)
        width = COLUMN_WIDTHS.get(col, 100)
        tree.column(col, width=width, anchor=W, stretch=False)
    
    return tree


def show_membre_details(tree_widget):
    """Show detailed information popup for selected membre"""
    selected = tree_widget.selection()
    if not selected:
        return
    
    # Get selected membre ID
    item = tree_widget.item(selected[0])
    membre_id = item['values'][0]
    
    # Fetch full details
    row = get_membre_details(membre_id)
    if not row:
        return
    
    # Create popup window
    window = Toplevel()
    window.title(f"Détails Membre: {row[1]} {row[2]}")
    window.geometry("450x400")
    window.resizable(False, False)
    
    # Info frame
    frame = LabelFrame(window, text="Informations", padx=15, pady=10)
    frame.pack(fill=BOTH, expand=True, padx=10, pady=10)
    
    # Display member information
    Label(frame, text=f"ID: {row[0]}", font=('Arial', 10)).grid(row=0, column=0, sticky=W, pady=3)
    Label(frame, text=f"Nom: {row[1]}", font=('Arial', 10)).grid(row=1, column=0, sticky=W, pady=3)
    Label(frame, text=f"Prénom: {row[2]}", font=('Arial', 10)).grid(row=2, column=0, sticky=W, pady=3)
    Label(frame, text=f"Rôle: {row[3]}", font=('Arial', 10)).grid(row=3, column=0, sticky=W, pady=3)
    Label(frame, text=f"Téléphone: {row[6]}", font=('Arial', 10)).grid(row=4, column=0, sticky=W, pady=3)
    Label(frame, text=f"Email: {row[7]}", font=('Arial', 10)).grid(row=5, column=0, sticky=W, pady=3)
    Label(frame, text=f"Date d'inscription: {row[5]}", font=('Arial', 10)).grid(row=6, column=0, sticky=W, pady=3)
    
    # Payment status indicator
    payment_frame = Frame(frame)
    payment_frame.grid(row=7, column=0, sticky=W, pady=3)
    Label(payment_frame, text="Payé: ", font=('Arial', 10)).pack(side=LEFT)
    
    if row[4]:  # payee status
        Label(payment_frame, text="✓", font=('Arial', 14, 'bold'), fg='green').pack(side=LEFT)
    else:
        Label(payment_frame, text="✗", font=('Arial', 14, 'bold'), fg='red').pack(side=LEFT)
    
    # Action buttons
    btn_frame = Frame(frame)
    btn_frame.grid(row=8, column=0, pady=15, sticky=W)
    
    email_addr = row[7] if row[7] else ""
    Button(btn_frame, text="📧 Email", padx=10, pady=5,
           command=lambda: webbrowser.open(f"mailto:{email_addr}")).pack(side=LEFT, padx=5)
    Button(btn_frame, text="📞 Appeler", padx=10, pady=5,
           command=lambda: webbrowser.open(f"tel:{row[6]}")).pack(side=LEFT, padx=5)
    
    # View activities button
    Button(frame, text="📋 Voir Activités Participées", padx=10, pady=5,
           command=lambda: show_membre_activities_window(membre_id, f"{row[1]} {row[2]}")
          ).grid(row=9, column=0, pady=5, sticky=W)
    
    # Activity count
    count = get_participation_count(membre_id)
    Label(frame, text=f"Nombre d'activités: {count}", font=('Arial', 9), fg='gray').grid(row=10, column=0, sticky=W)


def show_activite_details(tree_widget):
    """Show detailed information popup for selected activite"""
    selected = tree_widget.selection()
    if not selected:
        return
    
    # Get selected activite ID
    item = tree_widget.item(selected[0])
    activite_id = item['values'][0]
    
    # Fetch full details
    row = get_activite_details(activite_id)
    if not row:
        return
    
    # Create popup window
    window = Toplevel()
    window.title(f"Détails Activité: {row[1]}")
    window.geometry("400x300")
    window.resizable(False, False)
    
    # Info frame
    frame = LabelFrame(window, text="Informations", padx=15, pady=10)
    frame.pack(fill=BOTH, expand=True, padx=10, pady=10)
    
    # Display activity information
    Label(frame, text=f"ID: {row[0]}", font=('Arial', 10)).grid(row=0, column=0, sticky=W, pady=3)
    Label(frame, text=f"Nom: {row[1]}", font=('Arial', 10)).grid(row=1, column=0, sticky=W, pady=3)
    Label(frame, text=f"Type: {row[2]}", font=('Arial', 10)).grid(row=2, column=0, sticky=W, pady=3)
    Label(frame, text=f"Durée: {row[3]} minutes", font=('Arial', 10)).grid(row=3, column=0, sticky=W, pady=3)
    
    # Participant count
    count = get_participants_count(activite_id)
    Label(frame, text=f"Nombre de participants: {count}", font=('Arial', 10)).grid(row=4, column=0, sticky=W, pady=3)
    
    # View participants button
    Button(frame, text="👥 Voir Participants", padx=10, pady=5,
           command=lambda: show_activite_participants_window(activite_id, row[1])
          ).grid(row=5, column=0, pady=15, sticky=W)


def show_membre_activities_window(membre_id, membre_name):
    """Show window with all activities a membre participated in"""
    window = Toplevel()
    window.title(f"Activités de {membre_name}")
    window.geometry("500x300")
    
    frame = LabelFrame(window, text="Participations", padx=10, pady=10)
    frame.pack(fill=BOTH, expand=True, padx=10, pady=10)
    
    # Create treeview
    cols = ('Activité', 'Type', 'Date Participation')
    tree = ttk.Treeview(frame, columns=cols, show='headings', height=10)
    
    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, width=150)
    
    scrollbar = ttk.Scrollbar(frame, orient=VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=RIGHT, fill=Y)
    tree.pack(fill=BOTH, expand=True)
    
    # Load data
    activities = get_membre_activities(membre_id)
    for row in activities:
        tree.insert('', END, values=row)


def show_activite_participants_window(activite_id, activite_name):
    """Show window with all participants of an activite"""
    window = Toplevel()
    window.title(f"Participants - {activite_name}")
    window.geometry("500x300")
    
    frame = LabelFrame(window, text="Liste des Participants", padx=10, pady=10)
    frame.pack(fill=BOTH, expand=True, padx=10, pady=10)
    
    # Create treeview
    cols = ('Nom', 'Prénom', 'Rôle', 'Date Participation')
    tree = ttk.Treeview(frame, columns=cols, show='headings', height=10)
    
    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, width=120)
    
    scrollbar = ttk.Scrollbar(frame, orient=VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=RIGHT, fill=Y)
    tree.pack(fill=BOTH, expand=True)
    
    # Load data
    participants = get_activite_participants(activite_id)
    for row in participants:
        tree.insert('', END, values=row)
