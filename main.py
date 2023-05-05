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
    b
    # abre a porta serial
    ser = serial.Serial(porta, baud_rate, timeout=timeout)

    # envia dados para a porta serial
    ser.write(b'!0000000100100!')

    # lê dados da porta serial
    dados = ser.readline()
    print(dados)

def deconnect():
    ser.close()
# Press the green button in the gutter to run the script.
def on_button_click():
    print('hi')


if __name__ == '__main__':
    show()

    """ numero_decimal = int(input())
    numero_binario = bin(numero_decimal)[2:]
    print(numero_binario)
    numero_binario = format(numero_decimal, '08b')
    print(numero_binario)"""



# função que será executada quando o botão for pressionado

# cria a janela principal
window = Tk()

# cria o label
window.config(background='#2E4053')
window.title("CEMES INTERFACE REDPITAYA")
window.geometry("700x500")
window.iconbitmap("LOGO.ico")
window.minsize(700,500)
# cria o widget de texto
text_box = Text(window, height=1, width=30)
text_box.pack()
SET_Button= Button(window,text="SET",command=connect)
SET_Button.pack()
# cria o botão


# inicia o loop principal da interface gráfica
window.mainloop()
