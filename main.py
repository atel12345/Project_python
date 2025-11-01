"""
Main Application File - Project Club Management System
Entry point for the application

This is a school project organized for binome collaboration:
- main.py: Main application and UI layout (current file)
- database.py: All database operations
- ui_components.py: Reusable UI components and popups
- crud_operations.py: CRUD operations (for your binome to implement)
- config.py: Configuration and constants
- model.py: Database models and table creation
"""

from tkinter import *
from tkinter import ttk
from config import *
from database import *
from ui_components import *
from crud_operations import setup_crud_frame


class ProjectClubApp:
    """Main application class"""
    
    def __init__(self, root):
        self.root = root
        self.root.title(WINDOW_TITLE)
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        
        # Variables
        self.current_view = StringVar(value="membre")
        self.sort_var = StringVar(value="ID")
        
        # Setup UI
        self.setup_grid()
        self.create_top_controls()
        self.create_data_display()
        self.create_crud_section()
        self.create_kpi_section()
        
        # Load initial data
        self.load_membres()
    
    def setup_grid(self):
        """Configure grid layout"""
        self.root.grid_columnconfigure(0, weight=0)  # Left: fixed
        self.root.grid_columnconfigure(1, weight=1)  # Right: expandable
        self.root.grid_rowconfigure(0, weight=0)     # Top: buttons
        self.root.grid_rowconfigure(1, weight=1)     # Middle: data + CRUD
        self.root.grid_rowconfigure(2, weight=0)     # Bottom: KPIs
    
    def create_top_controls(self):
        """Create top control buttons and sort dropdown"""
        # Left side: view switch buttons
        btn_frame = Frame(self.root, pady=5)
        btn_frame.grid(row=0, column=0, sticky=W, padx=10)
        
        self.btn_membre = Button(btn_frame, text="Membre", 
                                  command=lambda: self.switch_view("membre"),
                                  relief=SUNKEN, padx=8, pady=2, font=('Arial', 9))
        self.btn_membre.pack(side=LEFT, padx=2)
        
        self.btn_activite = Button(btn_frame, text="Activite",
                                    command=lambda: self.switch_view("activite"),
                                    relief=RAISED, padx=8, pady=2, font=('Arial', 9))
        self.btn_activite.pack(side=LEFT, padx=2)
        
        Button(btn_frame, text="↻",
               command=lambda: self.switch_view(self.current_view.get()),
               padx=6, pady=2, font=('Arial', 9)).pack(side=LEFT, padx=10)
        
        # Right side: sort by column click (integrated in treeview headers)
        # No separate sort dropdown - click column headers to sort
    
    def create_data_display(self):
        """Create the left side data display area with trees"""
        # Container with fixed width
        container = Frame(self.root, width=LEFT_CONTAINER_WIDTH)
        container.grid(row=1, column=0, sticky=N+W, padx=10, pady=(0, 10))
        container.grid_propagate(False)
        
        # Data frame
        self.data_frame = LabelFrame(container, text="Liste des Membres", padx=5, pady=5)
        self.data_frame.pack(fill=BOTH, expand=True)
        
        # Create both trees
        self.tree_membre = create_treeview(self.data_frame, MEMBRE_COLUMNS)
        self.tree_activite = create_treeview(self.data_frame, ACTIVITE_COLUMNS)
        
        # Scrollbars
        self.scroll_membre = ttk.Scrollbar(self.data_frame, orient=VERTICAL,
                                           command=self.tree_membre.yview)
        self.tree_membre.configure(yscroll=self.scroll_membre.set)
        
        self.scroll_activite = ttk.Scrollbar(self.data_frame, orient=VERTICAL,
                                             command=self.tree_activite.yview)
        self.tree_activite.configure(yscroll=self.scroll_activite.set)
        
        # Bind double-click events
        self.tree_membre.bind('<Double-Button-1>',
                             lambda e: show_membre_details(self.tree_membre))
        self.tree_activite.bind('<Double-Button-1>',
                               lambda e: show_activite_details(self.tree_activite))
        
        # Bind column header clicks for sorting
        for col in MEMBRE_COLUMNS:
            self.tree_membre.heading(col, text=col, 
                                    command=lambda c=col: self.sort_by_column('membre', c))
        
        for col in ACTIVITE_COLUMNS:
            self.tree_activite.heading(col, text=col,
                                      command=lambda c=col: self.sort_by_column('activite', c))
        
        # Show membre tree initially
        self.scroll_membre.pack(side=RIGHT, fill=Y)
        self.tree_membre.pack(fill=BOTH, expand=True)
    
    def create_crud_section(self):
        """Create the right side CRUD operations area"""
        crud_frame = LabelFrame(self.root, text="Operations CRUD", padx=5, pady=5)
        crud_frame.grid(row=1, column=1, sticky=N+W+E+S, padx=(0, 10), pady=(0, 10))
        
        # Setup CRUD interface with refresh callback
        setup_crud_frame(crud_frame, refresh_callback=self.refresh_current_view)
    
    def create_kpi_section(self):
        """Create the bottom KPI statistics section"""
        kpi_frame = LabelFrame(self.root, text="Statistiques", padx=10, pady=5)
        kpi_frame.grid(row=2, column=0, columnspan=2, sticky=W+E, padx=10, pady=(0, 10))
        
        # KPI variables
        self.kpi_membres = StringVar(value="0")
        self.kpi_activites = StringVar(value="0")
        self.kpi_non_payers = StringVar(value="0")
        
        # KPI display
        display = Frame(kpi_frame)
        display.pack(fill=X)
        
        Label(display, text="Total Membres:", font=('Arial', 10, 'bold')).pack(side=LEFT, padx=10)
        Label(display, textvariable=self.kpi_membres, font=('Arial', 10), fg='blue').pack(side=LEFT, padx=5)
        
        Label(display, text="|", font=('Arial', 10)).pack(side=LEFT, padx=10)
        
        Label(display, text="Total Activités:", font=('Arial', 10, 'bold')).pack(side=LEFT, padx=10)
        Label(display, textvariable=self.kpi_activites, font=('Arial', 10), fg='blue').pack(side=LEFT, padx=5)
        
        Label(display, text="|", font=('Arial', 10)).pack(side=LEFT, padx=10)
        
        Label(display, text="Non Payés:", font=('Arial', 10, 'bold')).pack(side=LEFT, padx=10)
        Label(display, textvariable=self.kpi_non_payers, font=('Arial', 10), fg='red').pack(side=LEFT, padx=5)
    
    def load_membres(self, sort_by='id_membre'):
        """Load membres data into tree"""
        try:
            # Clear tree
            for item in self.tree_membre.get_children():
                self.tree_membre.delete(item)
            
            # Fetch and display data
            membres = get_membres(sort_by=sort_by)
            for row in membres:
                self.tree_membre.insert('', END, values=row)
            
            self.update_kpis()
        except Exception as e:
            from tkinter import messagebox
            messagebox.showerror("Erreur", f"Erreur de chargement membres: {str(e)}")
    
    def load_activites(self, sort_by='id_activite'):
        """Load activites data into tree"""
        try:
            # Clear tree
            for item in self.tree_activite.get_children():
                self.tree_activite.delete(item)
            
            # Fetch and display data
            activites = get_activites(sort_by=sort_by)
            for row in activites:
                self.tree_activite.insert('', END, values=row)
            
            self.update_kpis()
        except Exception as e:
            from tkinter import messagebox
            messagebox.showerror("Erreur", f"Erreur de chargement activités: {str(e)}")
    
    def update_kpis(self):
        """Update KPI statistics"""
        total_m, total_a, non_p = get_kpi_data()
        self.kpi_membres.set(str(total_m))
        self.kpi_activites.set(str(total_a))
        self.kpi_non_payers.set(str(non_p))
    
    def sort_by_column(self, view_type, column):
        """Sort tree by clicking column header"""
        if view_type == 'membre':
            sort_by = MEMBRE_SORT_OPTIONS.get(column, 'id_membre')
            self.load_membres(sort_by)
        else:
            sort_by = ACTIVITE_SORT_OPTIONS.get(column, 'id_activite')
            self.load_activites(sort_by)
    
    def refresh_current_view(self):
        """Refresh the currently displayed view (called after CRUD operations)"""
        self.switch_view(self.current_view.get())
    
    def switch_view(self, view):
        """Switch between membre and activite views"""
        self.current_view.set(view)
        
        if view == "membre":
            # Update button states
            self.btn_membre.config(relief=SUNKEN)
            self.btn_activite.config(relief=RAISED)
            
            # Update UI
            self.data_frame.config(text="Liste des Membres")
            
            # Hide activite, show membre
            self.tree_activite.pack_forget()
            self.scroll_activite.pack_forget()
            self.scroll_membre.pack(side=RIGHT, fill=Y)
            self.tree_membre.pack(fill=BOTH, expand=True)
            
            self.load_membres()
        else:
            # Update button states
            self.btn_activite.config(relief=SUNKEN)
            self.btn_membre.config(relief=RAISED)
            
            # Update UI
            self.data_frame.config(text="Liste des Activites")
            
            # Hide membre, show activite
            self.tree_membre.pack_forget()
            self.scroll_membre.pack_forget()
            self.scroll_activite.pack(side=RIGHT, fill=Y)
            self.tree_activite.pack(fill=BOTH, expand=True)
            
            self.load_activites()


# Main entry point
if __name__ == "__main__":
    root = Tk()
    app = ProjectClubApp(root)
    root.mainloop()
