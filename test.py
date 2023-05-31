import tkinter as tk
from tkinter import messagebox

def handle_button_click():
    try:
        # Code qui génère une erreur
        result = 10 / 0
    except Exception as e:
        # Affiche une fenêtre d'erreur
        messagebox.showerror("Erreur", "Une erreur s'est produite : " + str(e))

root = tk.Tk()

# Crée un bouton
button = tk.Button(root, text="Cliquer", command=handle_button_click)
button.pack()

root.mainloop()