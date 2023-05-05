import tkinter as tk

# função que será executada quando o botão for pressionado
def on_button_click():
    # adiciona o conteúdo do widget de texto à label
    label.configure(text=text_box.get("1.0", tk.END))

# cria a janela principal
root = tk.Tk()

# cria o label
label = tk.Label(root, text="Olá, mundo!")
label.pack()

# cria o widget de texto
text_box = tk.Text(root, height=5, width=30)
text_box.pack()

# cria o botão
button = tk.Button(root, text="Pressione-me!", command=on_button_click)
button.pack()

# inicia o loop principal da interface gráfica
root.mainloop()