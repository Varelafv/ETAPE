import serial.tools.list_ports
def connect():

    porta = 'COM8' #  Port série souhaitée.
    baud_rate = 115200
    timeout = 1

    # ouvre la porte serial
    ser = serial.Serial(porta, baud_rate, timeout=timeout)
def deconnect(ser):
    ser.close()
def generate(port,Channel_data,Waves_data,Gating_data,Frequency_data) :
    porta = port  # Port série souhaitée.
    baud_rate = 115200
    timeout = 1
    ser = serial.Serial(porta, baud_rate, timeout=timeout)
    Channel=Channel_data
    Wave=Waves_data
    Gating=Gating_data
    Frequency=Frequency_data
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
