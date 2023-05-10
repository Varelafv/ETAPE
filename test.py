from tkinter.ttk import Combobox

import serial.tools.list_ports
from tkinter import *


def show():
    # lista todas as portas seriais disponíveis
    portas_seriais = list(serial.tools.list_ports.comports())

    # imprime informações sobre cada porta serial disponível
    for porta in portas_seriais:
        print('Porta serial disponível:', porta.device)


def connect():
    porta = 'COM8'  # substitua com o nome da porta serial desejada
    baud_rate = 115200
    timeout = 1

    # abre a porta serial
    ser = serial.Serial(porta, baud_rate, timeout=timeout)

    # envia dados para a porta serial
    """ser.write(b'!0000000100100!')

    # lê dados da porta serial
    dados = ser.readline()
    print(dados)"""
    return ser

def generate( porta,baud_rate,timeout ) :

    ser = serial.Serial(porta, baud_rate, timeout=timeout)
    Channel=Channel_data.get()
    Wave=Waves_data.get()
    Gating=Gating_data.get()
    Frequency=Frequency_data.get()
    #a=b'!0000001000100!'
    DATA=list("!0000000000000000000000000!")
    d=b'!0000001000100!'
    #*************************************************TRAITEMENT DE CHANNEL *************************************************

    if(Channel=='1'):
        numero_binario = format(0, '01b')#--CH1
        DATA[1] = str(numero_binario)
    if (Channel == '2'):
        numero_binario = format(1, '01b')#--CH2
        DATA[1] = str(numero_binario)

    # *************************************************TRAITEMENT DE WAVES *************************************************
    if(Wave=='Sin'):
        numero_binario = format(1, '08b')
        DATA[2:10] = str(numero_binario)
    if (Wave == 'Square'):
        numero_binario = format(2, '08b')
        DATA[2:10] = str(numero_binario)
    # *************************************************TRAITEMENT DE GATING*************************************************
    if (Gating== '0%'):
        numero_binario = format(0, '08b')
        DATA[10:18] = str(numero_binario)
    if (Gating == '5%'):
        numero_binario = format(1, '08b')
        DATA[10:18] = str(numero_binario)
    if (Gating == '10%'):
        numero_binario = format(2, '08b')
        DATA[10:18] = str(numero_binario)
    if (Gating == '15%'):
        numero_binario = format(3, '08b')
        DATA[10:18] = str(numero_binario)
    if (Gating == '20%'):
        numero_binario = format(4, '08b')
        DATA[10:18] = str(numero_binario)
    if (Gating == '50%'):
        numero_binario = format(5, '08b')
        DATA[10:18] = str(numero_binario)
    # *************************************************TRAITEMENT DE FREQUENCY*************************************************

    if (Frequency == '31.3kHz'):
        numero_binario = format(0, '08b')
        DATA[18:26] = str(numero_binario)
    if (Frequency == '15.6kHz'):
        numero_binario = format(1, '08b')
        DATA[18:26] = str(numero_binario)
    if (Frequency == '7.81kHz'):
        numero_binario = format(2, '08b')
        DATA[18:26] = str(numero_binario)
    if (Frequency == '3.91kHz'):
        numero_binario = format(3, '08b')
        DATA[18:26] = str(numero_binario)
    if (Frequency == '1.95kHz'):
        numero_binario = format(4, '08b')
        DATA[18:26] = str(numero_binario)
    if (Frequency == '977Hz'):
        numero_binario = format(5, '08b')
        DATA[18:26] = str(numero_binario)
    if (Frequency == '488Hz'):
        numero_binario = format(6, '08b')
        DATA[18:26] = str(numero_binario)
    if (Frequency == '244Hz'):
        numero_binario = format(7, '08b')
        DATA[18:26] = str(numero_binario)
    if (Frequency == '122Hz'):
        numero_binario = format(8, '08b')
        DATA[18:26] = str(numero_binario)
    if (Frequency == '61Hz'):
        numero_binario = format(9, '08b')
        DATA[18:26] = str(numero_binario)
    if (Frequency == '30.5Hz'):
        numero_binario = format(10, '08b')
        DATA[18:26] = str(numero_binario)
    if (Frequency == '15Hz'):
        numero_binario = format(11, '08b')
        DATA[18:26] = str(numero_binario)
    if (Frequency == '7.63Hz'):
        numero_binario = format(12, '08b')
        DATA[18:26] = str(numero_binario)
    if (Frequency == '3.81Hz'):
        numero_binario = format(13, '08b')
        DATA[18:26] = str(numero_binario)

#*********CONCATENATION**************************************
    DATA=''.join(DATA)
    print(DATA)
    DATA_code =DATA.encode('utf-8')
    ser.write(DATA_code)
    print(Channel, Wave, Gating, Frequency)
    print("OK")
def deconnect():
    ser.close()


# Press the green button in the gutter to run the script.
def on_button_click():
    print('hi')


if __name__ == '__main__':
    show()
    connect()
    porta = 'COM8'  # substitua com o nome da porta serial desejada
    baud_rate = 115200
    timeout = 1
    """ numero_decimal = int(input())
    numero_binario = bin(numero_decimal)[2:]
    print(numero_binario)
    numero_binario = format(numero_decimal, '08b')
    print(numero_binario)"""

    # função que será executada quando o botão for pressionado

    # cria a janela principal
    window = Tk()
     #Configuration windows
    # cria o label
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
    # ajoute de image
    image=PhotoImage(file="graphsansgrid.PNG").zoom(20).subsample(40)
    canvas=Canvas(window,width=width,height=height,bg='#2E4053',bd=1,highlightthickness=0)
    canvas.create_image(width/2,height/2,image=image)
    canvas.pack()
    Channel_list= list(range(1, 3))
    Waves_list = ['Sin', 'Square']
    Gating_list = ['0%', '5%', '10%', '15%', '20%', '50%']
    Frequency_list = ['31.3kHz', '15.6kHz', '7.81kHz', '3.91kHz', '1.95kHz', '977Hz', '488Hz', '244Hz', '122Hz', '61Hz',
                      '30.5Hz', '15Hz', '7.63Hz', '3.81Hz']
    Waves_data = StringVar(window)
    Gating_data = StringVar(window)
    Frequency_data = StringVar(window)
    Channel_data =StringVar(window)

    #CRIATION DE FRAME 1 ****************************************



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

    SET_Button = Button(frame_1, text="GENERATE", command=lambda:generate( porta,baud_rate,timeout ) )
    SET_Button.grid(row=5, column=2)
    #*********************************************
    frame_1.pack()

    # cria o botão

    # inicia o loop principal da interface gráfica
    window.mainloop()
