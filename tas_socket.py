import socket
import asyncio, socket
import sys

#define socket with default values
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
	# Bind the socket to the port
    #format to recieve
    #para cada msg 1ero codigo de msj
    server_address = ('0.0.0.0', 1000)
    print('starting up on {} port {}'.format(*server_address))
    s.bind(server_address)
        
    while True:
        print('\nwaiting to receive message')
        data, address = s.recvfrom(4096) #S-CSCF
        if data:
            data = (data.decode()).split(" ")
            #S-CSCF sends SIP Register
            if(data[0] == "SIP" and data[1] == "REGISTER"):
                #envío UDR al HSS
                hss_address = ('', '') # van la IP y el port del hss
                udr_msg = "UDR ..." #PENDIENTE EL RESTO DE LOS PARÁMETROS
                udr_msg = udr_msg.encode()
                sent = s.sendto(udr_msg, hss_address)
                print('sent {} bytes back to {}'.format(
                    udr_msg, hss_address))
            
            #HSS SENDS UDA
            elif(data[0] == "UDA"):
                #envío un 200 OK al S-CSCF inicial(?
                sip_msg = "SIP 200 OK ..." #PENDIENTE EL RESTO DE LOS PARÁMETROS
                sip_msg = sip_msg.encode()
                sent = s.sendto(sip_msg, address)
                print('sent {} bytes back to {}'.format(
                    sip_msg, address))

            #luego pasan cosas ?? y sendeo un SIP suscribe a S-CSCF
            sip_msg = "SIP SUSCRIBE ..." #PENDIENTE EL RESTO DE LOS PARÁMETROS
            sip_msg = sip_msg.encode()
            sent = s.sendto(sip_msg, address)
            print('sent {} bytes back to {}'.format(
                sip_msg, address))

            #S-CSCF sends SIP 200 OK
            if(data[0] == "SIP" and data[1] == "NOTIFY"):
                #envío S-CSCF un 200ok notify
                sip_msg = "200 OK NOTIFY ..." #PENDIENTE EL RESTO DE LOS PARÁMETROS
                sip_msg = sip_msg.encode()
                sent = s.sendto(sip_msg, address)
                print('sent {} bytes back to {}'.format(
                    sip_msg, address))
            

