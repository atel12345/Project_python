from tkinter import *
from tkinter import messagebox
from model import Membre, Activite, Participation, is_table_empty

# ------------------- MEMBRE FUNCTIONS -------------------

def add_membre(refresh_callback=None):
    def save():
        mem = Membre(
            int(entry_id.get()),
            entry_nom.get(),
            entry_prenom.get(),
            entry_role.get(),
            1 if entry_payee.get().lower() in ("oui","yes","1") else 0,
            entry_date.get(),
            entry_tel.get(),
            entry_email.get()
        )
        mem.ajouter_membre()
        messagebox.showinfo("Succès", "Membre ajouté!")
        top.destroy()
        if refresh_callback:
            refresh_callback()

    top = Toplevel()
    top.title("Ajouter Membre")
    Label(top, text="ID").grid(row=0,column=0)
    entry_id = Entry(top); entry_id.grid(row=0,column=1)
    Label(top, text="Nom").grid(row=1,column=0)
    entry_nom = Entry(top); entry_nom.grid(row=1,column=1)
    Label(top, text="Prenom").grid(row=2,column=0)
    entry_prenom = Entry(top); entry_prenom.grid(row=2,column=1)
    Label(top, text="Role").grid(row=3,column=0)
    entry_role = Entry(top); entry_role.grid(row=3,column=1)
    Label(top, text="Payee (oui/non)").grid(row=4,column=0)
    entry_payee = Entry(top); entry_payee.grid(row=4,column=1)
    Label(top, text="Date inscription").grid(row=5,column=0)
    entry_date = Entry(top); entry_date.grid(row=5,column=1)
    Label(top, text="Tel").grid(row=6,column=0)
    entry_tel = Entry(top); entry_tel.grid(row=6,column=1)
    Label(top, text="Email").grid(row=7,column=0)
    entry_email = Entry(top); entry_email.grid(row=7,column=1)
    Button(top,text="Ajouter", command=save).grid(row=8,column=0,columnspan=2,pady=10)

def edit_membre(refresh_callback=None):
    def save():
        mem = Membre(
            int(entry_id.get()),
            entry_nom.get(),
            entry_prenom.get(),
            entry_role.get(),
            1 if entry_payee.get().lower() in ("oui","yes","1") else 0,
            entry_date.get(),
            entry_tel.get(),
            entry_email.get()
        )
        mem.modifier_membre()
        messagebox.showinfo("Succès", "Membre modifié!")
        top.destroy()
        if refresh_callback:
            refresh_callback()

    top = Toplevel()
    top.title("Modifier Membre")
    Label(top, text="ID").grid(row=0,column=0)
    entry_id = Entry(top); entry_id.grid(row=0,column=1)
    Label(top, text="Nom").grid(row=1,column=0)
    entry_nom = Entry(top); entry_nom.grid(row=1,column=1)
    Label(top, text="Prenom").grid(row=2,column=0)
    entry_prenom = Entry(top); entry_prenom.grid(row=2,column=1)
    Label(top, text="Role").grid(row=3,column=0)
    entry_role = Entry(top); entry_role.grid(row=3,column=1)
    Label(top, text="Payee (oui/non)").grid(row=4,column=0)
    entry_payee = Entry(top); entry_payee.grid(row=4,column=1)
    Label(top, text="Date inscription").grid(row=5,column=0)
    entry_date = Entry(top); entry_date.grid(row=5,column=1)
    Label(top, text="Tel").grid(row=6,column=0)
    entry_tel = Entry(top); entry_tel.grid(row=6,column=1)
    Label(top, text="Email").grid(row=7,column=0)
    entry_email = Entry(top); entry_email.grid(row=7,column=1)
    Button(top,text="Modifier", command=save).grid(row=8,column=0,columnspan=2,pady=10)

def delete_membre(refresh_callback=None):
    def remove():
        id_m = int(entry_id.get())
        mem = Membre(id_m,"","","",0,"","","")
        mem.supprimer_membre()
        messagebox.showinfo("Succès", "Membre supprimé!")
        top.destroy()
        if refresh_callback:
            refresh_callback()
    top = Toplevel()
    top.title("Supprimer Membre")
    Label(top,text="ID du membre").grid(row=0,column=0)
    entry_id = Entry(top); entry_id.grid(row=0,column=1)
    Button(top,text="Supprimer", command=remove).grid(row=1,column=0,columnspan=2,pady=10)

# ------------------- ACTIVITE FUNCTIONS -------------------

def add_activite(refresh_callback=None):
    def save():
        act = Activite(
            int(entry_id.get()),
            entry_nom.get(),
            entry_type.get(),
            int(entry_duree.get())
        )
        act.ajouter_activite()
        messagebox.showinfo("Succès", "Activité ajoutée!")
        top.destroy()
        if refresh_callback:
            refresh_callback()
    top = Toplevel()
    top.title("Ajouter Activité")
    Label(top,text="ID").grid(row=0,column=0)
    entry_id = Entry(top); entry_id.grid(row=0,column=1)
    Label(top,text="Nom").grid(row=1,column=0)
    entry_nom = Entry(top); entry_nom.grid(row=1,column=1)
    Label(top,text="Type").grid(row=2,column=0)
    entry_type = Entry(top); entry_type.grid(row=2,column=1)
    Label(top,text="Durée (min)").grid(row=3,column=0)
    entry_duree = Entry(top); entry_duree.grid(row=3,column=1)
    Button(top,text="Ajouter", command=save).grid(row=4,column=0,columnspan=2,pady=10)

def edit_activite(refresh_callback=None):
    def save():
        act = Activite(
            int(entry_id.get()),
            entry_nom.get(),
            entry_type.get(),
            int(entry_duree.get())
        )
        act.modifier_activite()
        messagebox.showinfo("Succès", "Activité modifiée!")
        top.destroy()
        if refresh_callback:
            refresh_callback()
    top = Toplevel()
    top.title("Modifier Activité")
    Label(top,text="ID").grid(row=0,column=0)
    entry_id = Entry(top); entry_id.grid(row=0,column=1)
    Label(top,text="Nom").grid(row=1,column=0)
    entry_nom = Entry(top); entry_nom.grid(row=1,column=1)
    Label(top,text="Type").grid(row=2,column=0)
    entry_type = Entry(top); entry_type.grid(row=2,column=1)
    Label(top,text="Durée (min)").grid(row=3,column=0)
    entry_duree = Entry(top); entry_duree.grid(row=3,column=1)
    Button(top,text="Modifier", command=save).grid(row=4,column=0,columnspan=2,pady=10)

def delete_activite(refresh_callback=None):
    def remove():
        id_a = int(entry_id.get())
        act = Activite(id_a,"","",0)
        act.supprimer_activite()
        messagebox.showinfo("Succès", "Activité supprimée!")
        top.destroy()
        if refresh_callback:
            refresh_callback()
    top = Toplevel()
    top.title("Supprimer Activité")
    Label(top,text="ID de l'activité").grid(row=0,column=0)
    entry_id = Entry(top); entry_id.grid(row=0,column=1)
    Button(top,text="Supprimer", command=remove).grid(row=1,column=0,columnspan=2,pady=10)

# ------------------- PARTICIPATION FUNCTIONS -------------------

def add_participation(refresh_callback=None):
    """Assign an activity to a member"""
    top = Toplevel()
    top.title("Ajouter Participation")
    top.geometry("300x200")

    Label(top, text="ID Membre").grid(row=0, column=0, pady=5)
    entry_id_membre = Entry(top)
    entry_id_membre.grid(row=0, column=1, pady=5)

    Label(top, text="ID Activité").grid(row=1, column=0, pady=5)
    entry_id_activite = Entry(top)
    entry_id_activite.grid(row=1, column=1, pady=5)

    Label(top, text="Date Participation").grid(row=2, column=0, pady=5)
    entry_date = Entry(top)
    entry_date.grid(row=2, column=1, pady=5)

    def save():
        par = Participation(
            int(entry_id_activite.get()),
            int(entry_id_membre.get()),
            entry_date.get()
        )
        par.ajouter_participation()
        messagebox.showinfo("Succès", "Participation ajoutée!")
        top.destroy()
        if refresh_callback:
            refresh_callback()

    Button(top, text="Ajouter", command=save).grid(row=3, column=0, columnspan=2, pady=10)

# ------------------- CRUD FRAME -------------------

def setup_crud_frame(parent_frame, refresh_callback=None):
    # Membres
    Label(parent_frame, text="--- Membres ---", fg="blue").pack(pady=5)
    Button(parent_frame, text="Ajouter Membre", command=lambda: add_membre(refresh_callback)).pack(pady=2)
    Button(parent_frame, text="Modifier Membre", command=lambda: edit_membre(refresh_callback)).pack(pady=2)
    Button(parent_frame, text="Supprimer Membre", command=lambda: delete_membre(refresh_callback)).pack(pady=2)

    frame_search_m = Frame(parent_frame)
    frame_search_m.pack(pady=3)
    entry_search_m = Entry(frame_search_m)
    entry_search_m.pack(side=LEFT, padx=2)
    def search_membre():
        result = Membre(0,"","","",0,"","","").recherche_membre(entry_search_m.get())
        if result:
            messagebox.showinfo("Résultat", f"ID:{result[0]} Nom:{result[1]} Prénom:{result[2]}")
        else:
            messagebox.showwarning("Résultat", "Membre non trouvé")
    Button(frame_search_m, text="🔍 Rechercher Membre", command=search_membre).pack(side=LEFT, padx=2)

    # Activités
    Label(parent_frame, text="--- Activités ---", fg="green").pack(pady=5)
    Button(parent_frame, text="Ajouter Activité", command=lambda: add_activite(refresh_callback)).pack(pady=2)
    Button(parent_frame, text="Modifier Activité", command=lambda: edit_activite(refresh_callback)).pack(pady=2)
    Button(parent_frame, text="Supprimer Activité", command=lambda: delete_activite(refresh_callback)).pack(pady=2)

    frame_search_a = Frame(parent_frame)
    frame_search_a.pack(pady=3)
    entry_search_a = Entry(frame_search_a)
    entry_search_a.pack(side=LEFT, padx=2)
    def search_activite():
        result = Activite(0,"","",0).recherche_activite(entry_search_a.get())
        if result:
            messagebox.showinfo("Résultat", f"ID:{result[0]} Nom:{result[1]} Type:{result[2]} Durée:{result[3]} min")
        else:
            messagebox.showwarning("Résultat", "Activité non trouvée")
    Button(frame_search_a, text="🔍 Rechercher Activité", command=search_activite).pack(side=LEFT, padx=2)

    # Participations
    Label(parent_frame, text="--- Participations ---", fg="purple").pack(pady=5)
    Button(parent_frame, text="Ajouter Participation", command=lambda: add_participation(refresh_callback)).pack(pady=2)

