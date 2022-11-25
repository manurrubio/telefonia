import socket
import asyncio, socket
import sys
import datetime



scscf_address = None

#define socket with default values
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    time = datetime.datetime.now()
	# Bind the socket to the port
    #format to recieve
    #para cada msg 1ero codigo de msj
    server_address = ('0.0.0.0', 1000)
    print('starting up on {} port {}'.format(*server_address))
    s.bind(server_address)
    s.setblocking(0)
        
    while True:
        print('\nwaiting to receive message')
        try:
            data, address = s.recvfrom(4096) #address changes depending on the msg
            input("Press enter to continue")
        except socket.error as e: 
            print("not recieved")
            now = datetime.datetime.now()
            if((now - time).total_seconds() > 30 and scscf_address is not None):
                sip_msg = "SIP SUSCRIBE ..." #PENDIENTE EL RESTO DE LOS PARÁMETROS
                sip_msg = sip_msg.encode()
                sent = s.sendto(sip_msg, scscf_address)
                print('sent {} bytes back to {}'.format(
                    sip_msg, scscf_address))
                time = now

        if data:
            data = (data.decode()).split(" ")
            #S-CSCF sends SIP Register
            if(data[0] == "SIP" and data[1] == "REGISTER"):
                #envío UDR al HSS
                scscf_address = address # van la IP y el port del hss
                hss_address = ('10.252.61.132', 1002) # van la IP y el port del hss
                udr_msg = "UDR ..." #PENDIENTE EL RESTO DE LOS PARÁMETROS
                udr_msg = udr_msg.encode()
                sent = s.sendto(udr_msg, hss_address)
                print('sent {} bytes back to {}'.format(
                    udr_msg, hss_address))
                input("Press enter to continue")
            
            #HSS SENDS UDA
            elif(data[0] == "UDA" and scscf_address is not None):
                #envío un 200 OK al S-CSCF inicial(?
                sip_msg = "SIP 200 OK ..." #PENDIENTE EL RESTO DE LOS PARÁMETROS
                sip_msg = sip_msg.encode()
                sent = s.sendto(sip_msg, scscf_address)
                print('sent {} bytes back to {}'.format(
                    sip_msg, scscf_address))
                input("Press enter to continue")  

            #S-CSCF sends SIP 200 OK
            if(data[0] == "SIP" and data[1] == "NOTIFY" and address is not None):
                #envío S-CSCF un 200ok notify
                sip_msg = "200 OK NOTIFY ..." #PENDIENTE EL RESTO DE LOS PARÁMETROS
                sip_msg = sip_msg.encode()
                sent = s.sendto(sip_msg, address)
                print('sent {} bytes back to {}'.format(
                    sip_msg, address))
                input("Press enter to continue")