#!/usr/bin/env python
#!_*_ coding: utf8 _*_
import os
import re
import time
from scapy.all import *
#from pyx import *

arreglo = []
ipOrigen = []
ipOrigenDEC = []
ipdestino = []
ipdestinoDEC = []

def leer(): ##Leemos el documento
    file = open('trama-datos.txt', 'r') ## leemos archivo
    for linea in file: ## recorremos archivo
        for ch in linea.split(): ##obtenemo la linea y la convertimos en arreglo con split() y lo recorremos
            arreglo.append(ch) ## agregamos los datos al arreglo
    file.close()
    return arreglo## retornamos el arreglo

def lecturasimple(): #imprimimos paquete
    file = open('trama-datos.txt', 'r')
    for linea in file:
        time.sleep(.5)
        print('\t',linea)
    file.close()

def DA(): #Direccion destion
    ar = leer()
    print("\n\t", "Cabecera Ethernet")
    print('    Direccion destino:     ',end="")
    for i in range(0, 6): ##Leemos los primero 6 bytes
        if(i<5):
            print(ar[i], ': ', end="")
        else:
            print(ar[i])

def SA(): #Source Addres
    ar = leer()
    print('    Direccion origen:          ',end="")
    for i in range(6, 12): ##Leemos los siguientes -> 6 bytes despues de DA
        if(i<11):
            print(ar[i], ': ', end="")
        else:
            print(ar[i])

def Protocol(): # Lectura de protocolos
    ar =leer()
    proto = ''
    print('',end="")
    for i in range(12, 14):
        ##print(ar[i], end="") 
        proto = proto + ar[i]
    if(proto == '0800'):
         print('    protocolo EtherType:    0x',proto)
         print('    Protocolo          :     version 4 (IPv4)')
    else:
        print('')
        print('    Lo sentimos el protocolo 0x',proto,'no se reconoce por el momento.')  
        print('    Estara disponible en la siguiente version de este programa')
        print('')

def ip(): #mostramos y validamos la ip hasta la direccion ip destino
    ar =leer()
    ltpd = 0
    proto = ''
    for i in range(14, 36):
        #version y longitud
        if(i == 14): #obtenemos la longitud de la cabecera
            time.sleep(1)
            print("\n\t", "FORMATO IPv4")
            print("    byte completo en hexadecimal: ", ar[i]) #byte completo
            print('    version: ', ar[i][0], '| Grupo de ', ar[i][0], 'bytes')
            #print("    Primer valor: ", ar[i][0], " = ",int(ar[i][0],16)) #separamos le caracter
            #print("    Segundo valor: ", ar[i][1], " = ",int(ar[i][1],16)) #otro caracter 
            long = int(ar[i][0],16) * int(ar[i][1],16) #multiplicamos los datos convertidos en decimal 
            print("    Longitud de cabecera: ", long, "bytes")
        elif(i == 15):
            time.sleep(1)
            #print('')

            ##Tipo de servicio
            #print('    Byte', ar[i])
            binario = int(ar[i],16)
            binario1 = format(int(ar[i][0],16),'b')
            binario2 = format(int(ar[i][1],16),'b')
            ##Rutina
            print()
            print('    Tipo de servicio')
            if(binario == 0):
                print('')
                print('    Precedencia: \t Rutina')
                print('    Servicio: \t Normal')
            elif(binario == 16):
                print('    Binario: ',format(int(ar[i],16),'b'))
                print('    Precedencia: \t Rutina')
                print('    Servicio: \t Minimizar retardo')
                print('')
            elif(binario == 8):
                print('    Binario: ',format(int(ar[i],16),'b'))
                print('    Precedencia: \t Rutina')
                print('    Servicio: \t Maximizar densidad de flujo')
                print('')
            elif(binario == 4):
                print('    Binario: ',format(int(ar[i],16),'b'))
                print('    Precedencia: \t Rutina')
                print('    Servicio: \t Maximizar la fiabilidad')
                print('')
            elif(binario == 2):
                print('    Binario: ',format(int(ar[i],16),'b'))
                print('    Precedencia: \t Rutina')
                print('    Servicio: \t Minimizar costo monetario')
                print('')
            ##Prioridad
            elif(binario == 32):
                print('    Binario: ',format(int(ar[i],16),'b'))
                print('    Precedencia: \t Prioridad')
                print('    Servicio: \t Normal')
            elif(binario == 48):
                print('    Binario: ',format(int(ar[i],16),'b'))
                print('    Precedencia: \t Prioridad')
                print('    Servicio: \t Minimizar retardo')
                print('')
            elif(binario == 40):
                print('    Binario: ',format(int(ar[i],16),'b'))
                print('    Precedencia: \t Prioridad')
                print('    Servicio: \t Maximizar densidad de flujo')
                print('')
            elif(binario == 36):
                print('    Binario: ',format(int(ar[i],16),'b'))
                print('    Precedencia: \t Prioridad')
                print('    Servicio: \t Maximizar la fiabilidad')
                print('')
            elif(binario == 34):
                print('    Binario: ',format(int(ar[i],16),'b'))
                print('    Precedencia: \t Prioridad')
                print('    Servicio: \t Minimizar costo monetario')
                print('')
            ##Inmediato
            elif(binario == 64):
                print('')
                print('    Precedencia: \t Inmediato')
                print('    Servicio: \t Normal')
            elif(binario == 80):
                print('    Binario: ',format(int(ar[i],16),'b'))
                print('    Precedencia: \t Inmediato')
                print('    Servicio: \t Minimizar retardo')
                print('')
            elif(binario == 72):
                print('    Binario: ',format(int(ar[i],16),'b'))
                print('    Precedencia: \t Inmediato')
                print('    Servicio: \t Maximizar densidad de flujo')
                print('')
            elif(binario == 68):
                print('    Binario: ',format(int(ar[i],16),'b'))
                print('    Precedencia: \t Inmediato')
                print('    Servicio: \t Maximizar la fiabilidad')
                print('')
            elif(binario == 66):
                print('    Binario: ',format(int(ar[i],16),'b'))
                print('    Precedencia: \t Inmediato')
                print('    Servicio: \t Minimizar costo monetario')
                print('')
            ##Flash
            elif(binario == 96):
                print('')
                print('    Precedencia: \t Flash')
                print('    Servicio: \t Normal')
            elif(binario == 112):
                print('    Binario: ',format(int(ar[i],16),'b'))
                print('    Precedencia: \t Flash')
                print('    Servicio: \t Minimizar retardo')
                print('')
            elif(binario == 104):
                print('    Binario: ',format(int(ar[i],16),'b'))
                print('    Precedencia: \t Flash')
                print('    Servicio: \t Maximizar densidad de flujo')
                print('')
            elif(binario == 100):
                print('    Binario: ',format(int(ar[i],16),'b'))
                print('    Precedencia: \t Flash')
                print('    Servicio: \t Maximizar la fiabilidad')
                print('')
            elif(binario == 98):
                print('    Binario: ',format(int(ar[i],16),'b'))
                print('    Precedencia: \t Flash')
                print('    Servicio: \t Minimizar costo monetario')
                print('')
            ##Flash override
            elif(binario == 128):
                print('')
                print('    Precedencia: \t Flash override')
                print('    Servicio: \t Normal')
            elif(binario == 144):
                print('    Binario: ',format(int(ar[i],16),'b'))
                print('    Precedencia: \t Flash override')
                print('    Servicio: \t Minimizar retardo')
                print('')
            elif(binario == 136):
                print('    Binario: ',format(int(ar[i],16),'b'))
                print('    Precedencia: \t Flash override')
                print('    Servicio: \t Maximizar densidad de flujo')
                print('')
            elif(binario == 132):
                print('    Binario: ',format(int(ar[i],16),'b'))
                print('    Precedencia: \t Flash override')
                print('    Servicio: \t Maximizar la fiabilidad')
                print('')
            elif(binario == 130):
                print('    Binario: ',format(int(ar[i],16),'b'))
                print('    Precedencia: \t Flash override')
                print('    Servicio: \t Minimizar costo monetario')
                print('')
            ##Critico
            elif(binario == 160):
                print('')
                print('    Precedencia: \t Critico')
                print('    Servicio: \t Normal')
            elif(binario == 176):
                print('    Binario: ',format(int(ar[i],16),'b'))
                print('    Precedencia: \t Critico')
                print('    Servicio: \t Minimizar retardo')
                print('')
            elif(binario == 168):
                print('    Binario: ',format(int(ar[i],16),'b'))
                print('    Precedencia: \t Critico')
                print('    Servicio: \t Maximizar densidad de flujo')
                print('')
            elif(binario == 164):
                print('    Binario: ',format(int(ar[i],16),'b'))
                print('    Precedencia: \t Critico')
                print('    Servicio: \t Maximizar la fiabilidad')
                print('')
            elif(binario == 162):
                print('    Binario: ',format(int(ar[i],16),'b'))
                print('    Precedencia: \t Critico')
                print('    Servicio: \t Minimizar costo monetario')
                print('')
            ##Control de red (Internet work control)
            elif(binario == 192):
                print('')
                print('    Precedencia: \t Control de red (Internet work control)')
                print('    Servicio: \t Normal')
            elif(binario == 208):
                print('    Binario: ',format(int(ar[i],16),'b'))
                print('    Precedencia: \t Control de red (Internet work control)')
                print('    Servicio: \t Minimizar retardo')
                print('')
            elif(binario == 200):
                print('    Binario: ',format(int(ar[i],16),'b'))
                print('    Precedencia: \t Control de red (Internet work control)')
                print('    Servicio: \t Maximizar densidad de flujo')
                print('')
            elif(binario == 196):
                print('    Binario: ',format(int(ar[i],16),'b'))
                print('    Precedencia: \t Control de red (Internet work control)')
                print('    Servicio: \t Maximizar la fiabilidad')
                print('')
            elif(binario == 194):
                print('    Binario: ',format(int(ar[i],16),'b'))
                print('    Precedencia: \t Control de red (Internet work control)')
                print('    Servicio: \t Minimizar costo monetario')
                print('')
            ##Control de red (Network control)
            elif(binario == 224):
                print('')
                print('    Precedencia: \t Control de red (Network control)')
                print('    Servicio: \t Normal')
            elif(binario == 240):
                print('    Binario: ',format(int(ar[i],16),'b'))
                print('    Precedencia: \t Control de red (Network control)')
                print('    Servicio: \t Minimizar retardo')
                print('')
            elif(binario == 232):
                print('    Binario: ',format(int(ar[i],16),'b'))
                print('    Precedencia: \t Control de red (Network control)')
                print('    Servicio: \t Maximizar densidad de flujo')
                print('')
            elif(binario == 228):
                print('    Binario: ',format(int(ar[i],16),'b'))
                print('    Precedencia: \t Control de red (Network control)')
                print('    Servicio: \t Maximizar la fiabilidad')
                print('')
            elif(binario == 226):
                print('    Binario: ',format(int(ar[i],16),'b'))
                print('    Precedencia: \t Control de red (Network control)')
                print('    Servicio: \t Minimizar costo monetario')
                print('')
            else:
                print('    Binario: ',format(int(ar[i],16),'b'))
                print('    No tenemos informacion para este dato, revice su trama')
        elif(i == 16 or i == 17):
            time.sleep(1)
            ltpd = int(ar[i],16) + ltpd
            if(i == 17):
                print('    Longitud total: \t', ltpd,' bytes')
        elif(i == 18 or i == 19):
            time.sleep(1)
            if(i == 18):
                print('    Identificacion: \t' ,"0x",ar[i], end=" ")
            else:
                print(ar[i])
                print('')
        elif(i == 20):
            time.sleep(1)
            bandera = format(int(ar[i],16), 'b')
            print('    Banderas de control:    \n')
            #print('    O: \t\tReservado')
            print('    Bit reservado')
            if(bandera[0] == '1'):
                print('    DF: \t', bandera[0], ' No permite fragmentacion')
            else:
                print('    DF: \t', bandera[0], ' Permite fragmentacion')
            if(bandera[1] == '0'):
                print('    MF: \t', bandera[1], ' No existen mas fragmentos')
            else:
                print('    MF: \t', bandera[1], ' Existen mas fragmentos')
        elif(i ==21):
            print('    Desplazamiento del fragmento: \t0x', ar[i-1], ar[i])
            if(int(ar[i],16) == 0):
                print('    No existe Fragmentacion el valor es cero', '\n')
            else:
                print('    El paquete esta fragmentado', '\n')
        elif(i ==22):
            print('    Tiempo de vida: \t0x', ar[i],'\t', int(ar[i],16), ' Segundos')
        elif(i ==23): #PROTOCLO
            proaltonivel = int(ar[i],16)
            if(proaltonivel == 0):
                print('    Protocolo IP: \t 0x', ar[i], ' RESERVADO')
            elif(proaltonivel == 1):
                print('    Protocolo IP: \t 0x', ar[i], ' ICMP')
            elif(proaltonivel == 2):
                print('    Protocolo IP: \t 0x', ar[i], ' IGMP')
            elif(proaltonivel == 3):
                print('    Protocolo IP: \t 0x', ar[i], ' GGP')
            elif(proaltonivel == 4):
                print('    Protocolo IP: \t 0x', ar[i], ' IP')
            elif(proaltonivel == 5):
                print('    Protocolo IP: \t 0x', ar[i], ' FLUJO (stream')
            elif(proaltonivel == 6):
                print('    Protocolo IP: \t 0x', ar[i], ' TCP')
            elif(proaltonivel == 8):
                print('    Protocolo IP: \t 0x', ar[i], ' EGP')
            elif(proaltonivel == 9):
                print('    Protocolo IP: \t 0x', ar[i], ' PIRP')
            elif(proaltonivel == 17):
                print('    Protocolo IP: \t 0x', ar[i], ' UDP')
            elif(proaltonivel == 89):
                print('    Protocolo IP: \t 0x', ar[i], ' OSPF')
            else:
                print('    Protocolo IP: \t Lo siento no encontramos el protocolo')
        elif( i == 24):
            time.sleep(1)
            print('    Checksum del paquete:\t 0x',ar[i], end="")
        elif(i ==25):
            print(ar[i])
            check = ar[i-1]+ar[i]
            datos = Checksum()
            time.sleep(.5)
            print("    Checksum verificado: 0x%x" % (ip_checksum(datos, len(datos)),))
            if(check == (ip_checksum(datos, len(datos)),)):
                print('    El checksum es correcrto')
            else:
                print('    ERROR checksum no corresponde')
            print()
        elif( i == 26 or i == 27 or i == 28 or i == 29 ):
            ipOrigen.append(ar[i])
            ipOrigenDEC.append(int(ar[i],16))
            time.sleep(1)
            if(i == 29):
                print('    IP Origen        : \t0x ', end="")
                for ip in ipOrigen:
                    print(ip,end=". ")
                print()
                print('    IP Origen Decimal: \t', end="")
                for ip in ipOrigenDEC:
                    print(ip,end=". ")
            
        elif( i == 30 or i == 31 or i == 32 or i == 33 ):
            ipdestino.append(ar[i])
            ipdestinoDEC.append(int(ar[i],16))
            time.sleep(1)
            if(i == 33):
                print()
                print('    IP Destino        : \t0x ', end="")
                for ip in ipdestino:
                    print(ip,end=". ")
                print()
                print('    IP Destino Decimal: \t', end="")
                for ip in ipdestinoDEC:
                    print(ip,end=". ")
        else:
            #print(ar[i], " ", end="") 
            print()
            break

def tcp():
    ar =leer()
    print()
    print('\t Cabecera TCP')
    for i in range(34, 56):
        if(i == 34 or i == 35):#Puerto de origen
            if(i == 35):
                print("    Puerto origen: \t\t", ' 0x', ar[i-1],'', ar[i],'    =>',int(ar[i-1]+ar[i],16), '   => |Puerto Registrado|')
                print("    Servicio: \t\t\t  Equipo servidor FTP Asociado (TCP)")
        elif(i == 36 or i == 37):#Puerto destino
            if(i == 37):
                print("    Puerto destino: \t\t" '  0x', ar[i-1],'', ar[i],'    =>',int(ar[i-1]+ar[i],16), '   => |Puerto Bien conocido|')
                print("    Servicio: \t\t\t  Servicio de Sesión NetBIOS (MS Windows) (TCP / UDP)")
        elif(i == 38 or i == 39 or i == 40 or i == 41):#Numero de secuencia: 
            if(i == 41):
                print('    Numero de secuencia: \t  0x',ar[i-3],ar[i-2],ar[i-1],ar[i],'    =>',int(ar[i-3]+ar[i-2]+ar[i-1]+ar[i],16))
        elif(i == 42 or i == 43 or i == 44 or i == 45):#Numero de secuencia: 
            if(i == 45):#Numero de confrimacion
                print('    Numero de confirmacion: \t  0x',ar[i-3],ar[i-2],ar[i-1],ar[i],'    =>',int(ar[i-3]+ar[i-2]+ar[i-1]+ar[i],16))
        elif(i == 46 or i == 47):#urg ack psh rst syn fin
            if(i == 47):
                ##format(int(ar[i-1][0],16),'04b')
                ##format(int(ar[i-1][1],16),'04b')
                a = format(int(ar[i][0],16),'04b')
                b = format(int(ar[i][1],16),'04b')
                print('    URG:        ', a[2], '   No Puesto')
                print('    ACK:        ', a[3], '   Puesto')
                print('    PSH:        ', b[0], '   Puesto')
                print('    RST:        ', b[1], '   No Puesto')
                print('    SYN:        ', b[2], '   No Puesto')
                print('    FIN:        ', b[3], '   No Puesto')
                datos = ChecksumParaTCP()
                print('    Checksum:            0x'+ar[50]+ar[51])
                print("    Checksum verificado: 0x", hex(TCPCheckSumTest(ar)))
                print("    Checksum No corresponde")

        else:
            break

def Checksum(): # retornamos los valores que suman el checksum
    data = leer()
    datos = {}
    x= 0
    for i in range(14,34):
        if(i == 24 or i == 25):
            continue
        else:
            #print(data[i], end=", ")
            datos[x]= int(data[i],16)
            x+=1
    return datos

def ChecksumParaTCP(): # retornamos los valores que suman el checksum de tcp
    data = leer()
    datos = {}
    pseudo = ['82','82','01','37','82','82','01','32','00','06', '00','4c','00', '72'] #0006 004c
    x= 0
    for i in range(34,54):
        if(i == 50):
            #datos[x]= int('00',16)
            continue
        elif(i == 51):
            #datos[x]= int('00',16)
            continue
        else:
            datos[x]= int(data[i],16)
            x+=1
    tam =18
    #print( datos)
    for i in pseudo:
        datos[tam] = int(i,16)
        tam +=1
    #print( datos)
    return datos

def ip_checksum(ip_header, size): #validamos
    
    cksum = 0
    pointer = 0
    
    #El bucle principal suma cada conjunto de 2 bytes. Primero se convierten en cadenas y luego se concatenan
    #juntos, convertidos a números enteros y luego sumados a la suma.
    while size > 1:
        cksum += int((str("%02x" % (ip_header[pointer],)) + 
                      str("%02x" % (ip_header[pointer+1],))), 16)
        size -= 2
        pointer += 2
    if size: #Esto explica una situación en la que el encabezado es extraño.
        cksum += ip_header[pointer]
        
    cksum = (cksum >> 16) + (cksum & 0xffff)
    cksum += (cksum >>16)
    
    return (~cksum) & 0xFFFF

def TCPCheckSumTest(Lista):  # TCP
    longitud_D = int(Lista[16] + Lista[17], 16) - (4 * 5) 
    suma = 0
    #print('comienza la primer suma')
    for y in range(26, 33, 2):
        suma += int(Lista[y] + Lista[y + 1], 16)
        #print(suma)
        #print(" for y in range(26, 33, 2):"
            #  "suma += int(Lista[y] + Lista[y + 1], 16)")
    #print(hex(suma) + "\n")
    suma += 0x0006  # reservado y protocolo
    suma += longitud_D  # longitud de datos
    if len(Lista) % 2 == 0:
        for y in range(34, len(Lista) - 1, 2):
            if y != 50:
                suma += int(Lista[y] + Lista[y + 1], 16)
                #print(hex(suma))
    else:
        #print('comienza la tercera suma')
        for y in range(34, len(Lista) - 1, 2):
            if y != 50:
                if y == (len(Lista)):
                    suma += int(Lista[y] + "00", 16)
                    print(suma)
                else:
                    suma += int(Lista[y] + Lista[y + 1], 16)
                    print(hex(suma))
        #print(hex(suma))
    suma += suma >> 16
    suma = bit_not(suma, 32)
    suma = suma & 0x0000FFFF
    return suma ##retornamos el valor del checksum

def bit_not(n, numbits=8):
    return (1 << numbits) - 1 - n

def wifi():
    """a= int(input("ingresa cuantos paquetes quieres capturar: "))
    int(a)
    pkt= sniff(filter='tcp', count=a) # buscamos paquetes en la red en este caso buscamos 2
    os.system('cls')
    print()
    b = a
    for i in range(b):
        time.sleep(1)
        hexdump(pkt[i]) #Imprimimosel paquete hexadesimal
        print('...')
        time.sleep(1)
        pkt[i].show() #imprimimos todos los valores TCP e IP del paquete
        pkt[i].pdfdump('')
        wrpcap('sniffer.pcap', [pkt])
        #pkt[i].psdump("/sniffer.pdf",layer_shift=1)
        os.system('pause')
        os.system('cls')"""
    cant = int(input("\tIngrese la cantidad de paquetes a capturar: "))
    wifi = sniff(filter='tcp', count=cant)
    os.system("cls")

    print("\t\tPaquetes capturados")
    print("\n\t",wifi,"\n")
    print("\n\t",wifi.nsummary())
    os.system("cls")

    numpk = int(input("\tIngrese el numero de paquete que desee visualizar: "))
    print(hexdump(wifi[numpk]))
    print("\n\n")
    wifi[numpk].show()
    print("\n\n")


    print("\n")
    print("         [a]  Imprimir PDF del datagrama capturado")
    print("         [b]  Exportar a un fichero .PCAP")
    print("         [c]  Regresar al menu anterior")
    opp = input("ingresa una opcion: ")

    if opp == "a":
        wifi[numpk].pdfdump("Datagrama.pdf")
        print("\t\tSe ha generado PDF")
    elif opp == "b":
        print("\t\tExportar Paquete a fichero .PCAP")
        name = str("junk")
        wrpcap('datagrama.cap', [wifi])
    elif opp == "c":
        print("\n")
        print("\n")
    else:
        print("Error de seleccion...\n")
        input()
        

def main():
    sl = 0
    print('')
    time.sleep(1)
    print('\t  || Bienvenido al programa ||')
    time.sleep(1)
    print('\t\t  DESTRAMADOR v1.0 ')
    print('')
    os.system('pause')
    while (sl == 0):

        try:
            os.system('cls')
            print('---MENU---')
            print('[1] Analizar un paquete existente de datos')
            print('[2] Analizar un paquete wifi')
            print('[3] Salir')
            print('')
            print('')
            op = int(input('ingresa la opcion a realizar: '))
        except ValueError: #validamos el caracter ingresado por el usuario
            print("Debes escribir un número.")
            os.system('pause')
            continue
        if op < 0: # validar que el numero sea entero 
            print("Debes escribir un número positivo.")
            os.system('pause')
            continue
        else:
            while(sl == 0):
                if(op ==1):
                    print('')
                    print('\t\t||||| DATAGRAMA |||||')
                    print('')
                    lecturasimple()
                    print('')
                    time.sleep(1)
                    DA()
                    time.sleep(1)
                    SA()
                    time.sleep(1)
                    Protocol()
                    time.sleep(1)
                    ip()
                    time.sleep(1)
                    tcp()
                    """print('')
                    tcp()
                    print('')"""
                    os.system('pause')
                    break
                elif(op == 2):
                    print('')
                    print('||||| Obteniendo datos Wifi |||||')
                    time.sleep(2)
                    wifi()
                    os.system('pause')
                    break
                elif(op == 3):
                    print('')
                    print('------------------------------')
                    print('Gracias por usar este programa')
                    print('------------------------------')
                    print('')
                    os.system('pause')
                    sl=1
                    break
                else:
                    print('No tenemos una opcion con ese numero seleccionado')
                    os.system('pause')
                    break
                    break
            ##aplicamos las opciones del menu 


main()
