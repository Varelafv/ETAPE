import serial.tools.list_ports
import tkinter as tk
from tkinter import messagebox
def connect():

    porta = 'COM8' #  Port série souhaitée.
    baud_rate = 115200
    timeout = 1

    # ouvre la porte serial
    ser = serial.Serial(porta, baud_rate, timeout=timeout)
def deconnect(ser):
    ser.close()
def generate(port,Channel_data,Waves_data,Gating_data,Frequency_data,Select_data) :
    try:

        porta = port  # Port série souhaitée.
        baud_rate = 115200
        timeout = 1
        ser = serial.Serial(porta, baud_rate, timeout=timeout)
        Channel=Channel_data
        Wave=Waves_data
        Gating=Gating_data
        Frequency=Frequency_data
        #a=b'!0000001000100!'
        DATA=list("0000000000!")
        d=b'!0000001000100!'
        #posution definie
        adr=1
        init=2
        fin=10

        if(Channel=='1'):
            numero_binario = format(0, '01b')#--CH1
            DATA[0] = str(numero_binario)
        elif (Channel == '2'):
            numero_binario = format(1, '01b')#--CH2
            DATA[0] = str(numero_binario)

        # *************************************************TRAITEMENT DE WAVES *************************************************
        if(Select_data=='Waves'):
            DATA[adr]='W'
            if(Wave=='Sin'):
                numero_binario = format(1, '08b')
                DATA[init:fin] = str(numero_binario)
            if (Wave == 'Square'):
                numero_binario = format(2, '08b')
                DATA[init:fin] = str(numero_binario)
        # *************************************************TRAITEMENT DE GATING*************************************************
        if (Select_data == 'Gating'):
            DATA[adr] = 'G'
            numero_binario = format(Gating, '08b')
            DATA[init:fin] = str(numero_binario)
        # *************************************************TRAITEMENT DE FREQUENCY*************************************************
        if (Select_data == 'Freq'):
            DATA[adr]='F'
            numero_binario = format(Frequency, '08b')
            DATA[init:fin] = str(numero_binario)


    #*********CONCATENATION**************************************
        DATA=''.join(DATA)
        print(DATA)
        DATA_code =DATA.encode('utf-8')
        ser.write(DATA_code)
        print(Channel, Wave, Gating, Frequency)
        print("OK")

    except Exception as e:
        # Affiche une fenêtre d'erreur
        messagebox.showerror("Erreur", "Une erreur s'est produite : " + str(e))