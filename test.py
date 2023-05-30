import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot_sine():
    # Créer les données pour le graphique
    import numpy as np
    x = np.linspace(0, 2*np.pi, 100)
    y = np.sin(x)

    # Créer la figure et le graphique
    fig = Figure(figsize=(6, 4), dpi=100)
    plot = fig.add_subplot(111)
    plot.plot(x, y)

    # Créer le widget Canvas Tkinter pour afficher le graphique
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Créer la fenêtre Tkinter
root = tk.Tk()
root.title("Graphique de Sinus")

# Bouton pour afficher le graphique
button = tk.Button(root, text="Afficher le graphique", command=plot_sine)
button.pack()

# Lancer la boucle principale Tkinter
root.mainloop()
