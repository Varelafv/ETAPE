import tkinter as tk
from tkinter import messagebox


def open_subwindow():
    global subwindow

    # Vérifier si la sous-fenêtre est déjà ouverte
    if subwindow is None or not subwindow.winfo_exists():
        subwindow = tk.Toplevel(root)
        subwindow.title("Sous-fenêtre")
        subwindow.geometry("200x100")

        label = tk.Label(subwindow, text="Ceci est une sous-fenêtre")
        label.pack(pady=20)

        # Fermer la sous-fenêtre
        def close_subwindow():
            subwindow.destroy()

        close_button = tk.Button(subwindow, text="Fermer", command=close_subwindow)
        close_button.pack()


root = tk.Tk()
subwindow = None

# Bouton pour ouvrir la sous-fenêtre
open_button = tk.Button(root, text="Ouvrir la sous-fenêtre", command=open_subwindow)
open_button.pack(pady=20)

root.mainloop()
