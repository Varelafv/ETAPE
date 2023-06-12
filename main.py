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


def sub_fene_parametre_f():
    global sub_fene_parametre

    if sub_fene_parametre is None or not sub_fene_parametre.winfo_exists():

        sub_fene_parametre= tk.Toplevel(window)
        sub_fene_parametre.title("Paramettre")
        sub_fene_parametre.geometry("300x200")
        sub_fene_parametre.minsize(300, 200)
        sub_fene_parametre.maxsize(300, 200)
        sub_fene_parametre.iconbitmap("images/LOGO.ico")
        sub_fene_parametre.config(background=backgroud_type[s])

        #--------------------------------------------------------------------------------
        Prm=["CHANNEL->","WAVE","AMP","FREQ","GAT"]
        #-----------------------------------------------------------------------------
        Parametre_label= tk.Label(sub_fene_parametre, text=Prm,fg="Yellow",bg=backgroud_type[s])
        Parametre_label.pack()
        TRE1 = tk.Label(sub_fene_parametre, text="--------------------------------------------------------------------", fg="Yellow", bg=backgroud_type[s])
        TRE1.pack()
        CH1_label = tk.Label(sub_fene_parametre, text=CH1, fg="White", bg=backgroud_type[s])
        CH1_label.pack()
        TRE2 = tk.Label(sub_fene_parametre, text="--------------------------------------------------------------------",
                        fg="Yellow", bg=backgroud_type[s])
        TRE2.pack()
        CH2_label = tk.Label(sub_fene_parametre, text=CH2, fg="White", bg=backgroud_type[s])
        CH2_label.pack()
        TRE3 = tk.Label(sub_fene_parametre, text="--------------------------------------------------------------------",
                        fg="Yellow", bg=backgroud_type[s])
        TRE3.pack()

        # Fermer la sous-fenêtre
        def close_subwindow():
            sub_fene_parametre.destroy()

        close_button = tk.Button(sub_fene_parametre, text="Fermer",bg=color_button, command=close_subwindow)
        close_button.place(x=125,y=150)



def set_value_par(Channel,Waves,Gating,Frequency, Select):
   # CH1 = ["CH1->:", "Sin", "1V", "62.5kHz", "0%"]
   # CH2 = ["CH2->:", "Square", "1V", "31.kHz", "5%"]
   #La mise a jour de signal , est fete pour chaque SORTIE
    if(Channel=="1") :

        if(Select=='Waves') :

            CH1[1]=Waves
        elif (Select =='Freq'):
            CH1[3]=Frequency
        elif(Select=='Gating'):
            if CH1[1]=="Square" :  #Gating c'est valide lorsque on a un Square a la sortie
                 CH1[4]=Gating
    else:
        if (Select == 'Waves'):

            CH2[1] = Waves
        elif (Select == 'Freq'):
            CH2[3] = Frequency
        elif (Select == 'Gating'):#Gating c'est valide lorsque on a un Square a la sortie
            if CH2[1]=="Square" :
                CH2[4]=Gating







if __name__ == '__main__':
    #Aquisition de nombre de ports disponible
    Port_disponible=[]
    Port_disponible=show()
    global  CH1
    global CH2
    CH1 = ["CH1->:", "None", "1V", "62.5kHz", "0%"]
    CH2 = ["CH2->:", "None", "1V", "62.kHz", "0%"]
    #Crée la fenêtre principale.
    window = Tk()
    sub_fene_parametre = None
     #Configuration windows

    s = 0; #-->
    color_button="#08D9FA"
    backgroud_type=['#2E4053','#101618']
    image_name = ["images/graphsansgrid.PNG", "images/graphsansgrid2.PNG"]
    window.config(background= backgroud_type[s])
    window.title("CEMES INTERFACE REDIPITAYA")
    window.geometry("700x500")
    window.iconbitmap("images/LOGO.ico")
    window.minsize(700, 500) #limitation minimal
    window.maxsize(700, 500) #limitation maximal

    #label_title = Label(window, text="INTERFACE REDIPITAYA", font="Georgia", bg= backgroud_type[s], fg='white')
    #label_title.pack()
    width=200
    height=200
    #***Connexion avec la porte ****
    PORT_data = StringVar(window)
    Port_label = Label(window, text="Port", font="Georgia", bg =backgroud_type[s], fg='white')
    Port_label.place(x=20, y=10)
    Port_box = Combobox(window, textvariable=PORT_data, values=Port_disponible, width=7)
    Port_box.place(x=10, y=30)

    Parmt_Button=Button(window,text="IIIII",command=lambda:sub_fene_parametre_f())
    Parmt_Button.place(x=650,y=5)
   # connetion= Button(window, text="connecter",command=lambda :connect())
    #connetion.place(x=10, y=55)

    # ajoute d'image Graphique
    image=PhotoImage(file=image_name[s]).zoom(20).subsample(40)
    canvas=Canvas(window,width=width,height=height,bg= backgroud_type[s],bd=1,highlightthickness=0)
    canvas.create_image(width/2,height/2,image=image)
    canvas.pack()


    #  ****************************************la liste de Options ****************************************
    Channel_list = list(range(1, 3))
    Waves_list = ['Sin', 'Square']
    Gating_list = ['0%', '5%', '10%', '15%', '20%', '50%']
    Frequency_list = ['62.5kHz','31.3kHz', '15.6kHz', '7.81kHz', '3.91kHz', '1.95kHz', '977Hz', '488Hz', '244Hz', '122Hz', '61Hz',
                      '30.5Hz', '15Hz', '7.63Hz', '3.81Hz']
    Select_list=['Waves','Gating','Freq']
    #*********************LES DATA DE RECUPERATION
    Select_data=StringVar(window)
    Select_data.set('Waves')#--Definir valeur de default
    Waves_data = StringVar(window)
    Waves_data.set('Sin')
    Gating_data = StringVar(window)
    Gating_data.set('0%')
    Frequency_data = StringVar(window)
    Frequency_data.set('62.5kHz')
    Channel_data =StringVar(window)
    Channel_data.set('1')

    #CREIATION DE FRAME 1 ****************************************
    frame_1=Frame(window, bg=backgroud_type[s],bd=2 ,relief=SUNKEN)
     #  Box pour selectionner channel
    Channel_label = Label(frame_1, text="Channel", font="Georgia", bg=backgroud_type[s], fg='white')
    Channel_label.grid(row=0, column=2)
    Channel_box= Combobox(frame_1, textvariable=Channel_data, values=Channel_list, width=7)

    Channel_box.grid(row=1, column=2)

    #  Box pour selectionner Type Waves
    Waves_label = Label(frame_1, text="Waves", font="Georgia", bg=backgroud_type[s], fg='white')
    Waves_label.grid(row=2, column=0)
    Waves_box1 = Combobox(frame_1, textvariable=Waves_data, values=Waves_list, width=7)

    Waves_box1.grid(row=3, column=0)

    vide = Label(frame_1, text="VIDEVIDE", font="Georgia", bg=backgroud_type[s], fg=backgroud_type[s])
    vide.grid(row=2, column=1)
    #  Box pour selectionner Gating
    Gating_label = Label(frame_1, text="Gating", font="Georgia", bg=backgroud_type[s], fg='white')
    Gating_label.grid(row=2, column=2)
    Gating_box2 = Combobox(frame_1, textvariable=Gating_data, values=Gating_list, width=7)
    Gating_box2.grid(row=3, column=2)

    vide2 = Label(frame_1, text="VIDEVIDE", font="Georgia", bg=backgroud_type[s], fg=backgroud_type[s])
    vide2.grid(row=2, column=3)
    #  Box pour selectionner Gating
    Frequency_label = Label(frame_1, text="Frequency", font="Georgia", bg=backgroud_type[s], fg='white')
    Frequency_label.grid(row=2, column=4)
    Frequency_box3 = Combobox(frame_1, textvariable=Frequency_data, values=Frequency_list, width=7)
    Frequency_box3.grid(row=3, column=4)
    vide3 = Label(frame_1, text="VIDEVIDE", font="Georgia", bg=backgroud_type[s], fg=backgroud_type[s])
    vide3.grid(row=4, column=3)
    frame_1.pack()
    frame_2 = Frame(window, bg=backgroud_type[s], bd=2)
    Newvalue_label= Label(frame_2, text="Select", font="Georgia", bg=backgroud_type[s], fg='white')
    Newvalue_label.grid(row=5, column=2)
    Select_box=Combobox(frame_2,textvariable=Select_data,values=Select_list,width=7)
    Select_box.grid(row=6,column=1)
    #ORIGINAL BUTTON
    #SET_Button = Button(frame_2, text="Set Value ",bg="#08D9FA",command=lambda:generate(PORT_data.get(),Channel_data.get(),Waves_data.get(),Gating_list.index(Gating_data.get()),Frequency_list.index(Frequency_data.get()),Select_data.get()))
    SET_Set_button = Button(frame_2, text="Set Value ", bg=color_button,
                        command=lambda: [generate(PORT_data.get(),Channel_data.get(), Waves_data.get(),
                                                 Gating_list.index(Gating_data.get()),
                                                 Frequency_list.index(Frequency_data.get()), Select_data.get()),
                                         set_value_par(Channel_data.get(), Waves_data.get(),
                                                 Gating_data.get(),
                                                 Frequency_data.get(), Select_data.get())])



    SET_Set_button.grid(row=6, column=3)

    #*********************************************
    frame_2.pack()

    # Démarre la boucle principale de l'interface graphique.
    window.mainloop()
