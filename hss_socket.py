import socket
import asyncio, socket
import sys

hss_users = {
  "RODRIGO": True,
  "TUTE": False,
  #"+59898124957": True
  }
  
hss_location = {
  "RODRIGO": "uruguay",
  "TUTE": "china"
  }

#define socket with default values
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
	# Bind the socket to the port
    #format to recieve
    #para cada msg 1ero codigo de msj
    server_address = ('0.0.0.0', 1002)
    print('starting up on {} port {}'.format(*server_address))
    s.bind(server_address)
        
    while True:
        print('\nwaiting to receive message')
        data, address = s.recvfrom(4096) #
        if data:
            data = ((data.decode()).upper()).split(" ")
            print(data)
            # I-CSCF asks for user info
            if(data[0] == "UAR"):
                uaa_msg = None
                if hss_users.get(data[1].split(":")[1], False):
                    uaa_msg = "AUTH 400 NOK"
                else:
                    uaa_msg = "AUTH 200 OK"
                uaa_msg = "UAA 200 OK"
                uaa_msg = uaa_msg.encode()
                input(f"Press enter to send {uaa_msg}")
                sent = s.sendto(uaa_msg, address)
                print('sent {} bytes back to {}'.format(
                    uaa_msg, address))
            elif(data[0] == "UDR"):
                #TAS sends UDR
                uda_msg = None
                if hss_users.get(data[1], False):
                    uda_msg = "UDA 400 NOK"
                else:
                    uda_msg = "UDA 200 OK"
                uda_msg = uda_msg.encode()
                input(f"Press enter to send {uda_msg}")
                sent = s.sendto(uda_msg, address)
                print('sent {} bytes back to {}'.format(
                    uda_msg, address))
            elif(data[0] == "MAR"):
                #PCSC-F sends MAR
                maa_msg = None
                maa_msg = "MAA 401 NOK"
                hss_users[data[1]] = True
                print(data[1])
                #if hss_users.get(data[1], False):
                #    maa_msg = "MAA 401 NOK"
                #    hss_users[data[1]] = True
                #    print(data[1])
                #else:
                #    maa_msg = "MAA 200 OK"
                maa_msg = maa_msg.encode()
                input(f"Press enter to send {maa_msg}")
                sent = s.sendto(maa_msg, address)
                print('sent {} bytes back to {}'.format(
                    maa_msg, address))
            elif(data[0] == "SAR"):
                #PCSC-F sends SAR
                saa_msg = None
                if hss_users.get(data[1], False):
                    saa_msg = "SAA 400 NOK"
                else:
                    saa_msg = "SAA 200 OK"
                saa_msg = saa_msg.encode()
                sent = s.sendto(maa_msg, address)
                input(f"Press enter to send {saa_msg}")
                print('sent {} bytes back to {}'.format(
                    saa_msg, address))
            elif(data[0] == "SIP" and data[1] == "REGISTER"):
                auth_msg = None
                if hss_users.get((data[2]).split(":")[1], False):
                    auth_msg = "AUTH 400 NOK"
                else:
                    auth_msg = "AUTH 200 OK"
                auth_msg = auth_msg.encode()
                input(f"Press enter to send {auth_msg}")
                sent = s.sendto(auth_msg, address)
                print('sent {} bytes back to {}'.format(
                    auth_msg, address))
            elif(data[0] == "UPDATE_LOCATION"):
                location_msg = None
                if not hss_users.get(data[1], False) :
                    location_msg = "UPDATE_LOCATION 400 NOK"
                else:
                    #hss_users[data[1]] = data[2]
                    location_msg = "APN:movistar.uy"
                location_msg = location_msg.encode()
                input(f"Press enter to send {location_msg}")
                sent = s.sendto(location_msg, address)
                print('sent {} bytes back to {}'.format(
                    location_msg, address))
