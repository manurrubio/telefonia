import socket
import asyncio, socket
import sys

#define socket with default values
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
	# Bind the socket to the port
    #format to recieve
    #para cada msg 1ero codigo de msj
    server_address = ('0.0.0.0', 1001)
    print('starting up on {} port {}'.format(*server_address))
    s.bind(server_address)
        
    while True:
        print('\nwaiting to receive message')
        data, address = s.recvfrom(4096) #
        if data:
            data = (data.decode()).split(" ")
            #PGW sends CCR Register
            if(data[0] == "CCR"):
                #PASAN COSAS Y LE MANDO UN CCA
                cca_msg = "CAA ..." #PENDIENTE EL RESTO DE LOS PARÁMETROS
                cca_msg = cca_msg.encode()
                sent = s.sendto(cca_msg, address)
                print('sent {} bytes back to {}'.format(
                    cca_msg, address))
            elif(data[0] == "AAR"):
                #PCSC-F sends AAR
                aar_msg = "AAR ..."
                aar_msg = aar_msg.encode()
                sent = s.sendto(aar_msg, address)
                print('sent {} bytes back to {}'.format(
                    aar_msg, address))