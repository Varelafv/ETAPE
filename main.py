from tkinter.ttk import Combobox
from tkinter import *
from generate import *

def show():
    List_Port=[]
    # Énumère toutes les ports séries disponibles.
    portas_seriais = list(serial.tools.list_ports.comports())

    # fiche des informations sur chaque port série disponible.
    for porta in portas_seriais:
        print("Port série disponible:", porta.device)
        List_Port.append(porta.device)
    return(List_Port)







if __name__ == '__main__':
    #Aquisition de nombre de ports disponible
    Port_disponible=[]
    Port_disponible=show()
    print(Port_disponible)

    #Crée la fenêtre principale.
    window = Tk()
     #Configuration windows
    window.config(background='#2E4053')
    window.title("CEMES")
    window.geometry("700x500")
    window.iconbitmap("LOGO.ico")
    window.minsize(700, 500)
    window.maxsize(700, 500)

    label_title = Label(window, text="INTERFACE REDIPITAYA", font="Georgia", bg="#2E4053", fg='white')
    label_title.pack()
    width=200
    height=200
    #***Connexion avec la porte ****
    PORT_data = StringVar(window)
    Port_label = Label(window, text="Port", font="Georgia", bg="#2E4053", fg='white')
    Port_label.place(x=20, y=10)
    Port_box = Combobox(window, textvariable=PORT_data, values=Port_disponible, width=7)
    Port_box.place(x=10, y=30)
   # connetion= Button(window, text="connecter",command=lambda :connect())
    #connetion.place(x=10, y=55)

    # ajoute d'image
    image=PhotoImage(file="graphsansgrid.PNG").zoom(20).subsample(40)
    canvas=Canvas(window,width=width,height=height,bg='#2E4053',bd=1,highlightthickness=0)
    canvas.create_image(width/2,height/2,image=image)
    canvas.pack()
    Channel_list= list(range(1, 3))

    #  ****************************************la liste de Options ****************************************
    Waves_list = ['Sin', 'Square']
    Gating_list = ['0%', '5%', '10%', '15%', '20%', '50%']
    Frequency_list = ['31.3kHz', '15.6kHz', '7.81kHz', '3.91kHz', '1.95kHz', '977Hz', '488Hz', '244Hz', '122Hz', '61Hz',
                      '30.5Hz', '15Hz', '7.63Hz', '3.81Hz']

    Waves_data = StringVar(window)
    Gating_data = StringVar(window)
    Frequency_data = StringVar(window)
    Channel_data =StringVar(window)

    #CREIATION DE FRAME 1 ****************************************



    frame_1=Frame(window, bg="#2E4053",bd=2 ,relief=SUNKEN)

    # cria o widget de texto

    Channel_label = Label(frame_1, text="Channel", font="Georgia", bg="#2E4053", fg='white')
    Channel_label.grid(row=0, column=2)
    Channel_box2 = Combobox(frame_1, textvariable=Channel_data, values=Channel_list, width=7)
    Channel_box2.grid(row=1, column=2)

    Waves_label = Label(frame_1, text="Waves", font="Georgia", bg="#2E4053", fg='white')
    Waves_label.grid(row=2, column=0)
    Waves_box1 = Combobox(frame_1, textvariable=Waves_data, values=Waves_list, width=7)
    Waves_box1.grid(row=3, column=0)

    vide = Label(frame_1, text="VIDEVIDE", font="Georgia", bg="#2E4053", fg='#2E4053')
    vide.grid(row=2, column=1)

    Gating_label = Label(frame_1, text="Gating", font="Georgia", bg="#2E4053", fg='white')
    Gating_label.grid(row=2, column=2)
    Gating_box2 = Combobox(frame_1, textvariable=Gating_data, values=Gating_list, width=7)
    Gating_box2.grid(row=3, column=2)

    vide2 = Label(frame_1, text="VIDEVIDE", font="Georgia", bg="#2E4053", fg='#2E4053')
    vide2.grid(row=2, column=3)

    Frequency_label = Label(frame_1, text="Frequency", font="Georgia", bg="#2E4053", fg='white')
    Frequency_label.grid(row=2, column=4)
    Frequency_box3 = Combobox(frame_1, textvariable=Frequency_data, values=Frequency_list, width=7)
    Frequency_box3.grid(row=3, column=4)
    vide3 = Label(frame_1, text="VIDEVIDE", font="Georgia", bg="#2E4053", fg='#2E4053')
    vide3.grid(row=4, column=3)

    SET_Button = Button(frame_1, text="GENERATE", command=lambda:generate(PORT_data.get(),Channel_data.get(),Waves_data.get(),Gating_data.get(),Frequency_data.get()) )
    SET_Button.grid(row=5, column=2)
    #*********************************************
    frame_1.pack()

    # Démarre la boucle principale de l'interface graphique.
    window.mainloop()
