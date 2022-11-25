import socket
import asyncio, socket
import sys

hss_users = {
  "fabri": true,
  "tute": false
  }
  
hss_location = {
  "fabri": "uruguay",
  "tute": "china"
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
            data = (data.decode()).split(" ")
            # I-CSCF asks for user info
            if(data[0] == "UAR"):
                uaa_msg = None
                if hss_users.get(data[1], false):
                    uaa_msg = "AUTH 400 NOK"
                else:
                    uaa_msg = "AUTH 200 OK"
                uaa_msg = "UAA 200 OK"
                uaa_msg = uaa_msg.encode()
                sent = s.sendto(uaa_msg, address)
                print('sent {} bytes back to {}'.format(
                    uaa_msg, address))
                input("Press enter to continue")
            elif(data[0] == "UDR"):
                #TAS sends UDR
                uda_msg = None
                if hss_users.get(data[1], false):
                    uda_msg = "UDA 400 NOK"
                else:
                    uda_msg = "UDA 200 OK"
                uda_msg = uda_msg.encode()
                sent = s.sendto(uda_msg, address)
                print('sent {} bytes back to {}'.format(
                    uda_msg, address))
                input("Press enter to continue")
            elif(data[0] == "MAR"):
                #PCSC-F sends MAR
                maa_msg = None
                if hss_users.get(data[1], false):
                    maa_msg = "MAA 400 NOK"
                else:
                    maa_msg = "MAA 200 OK"
                maa_msg = maa_msg.encode()
                sent = s.sendto(maa_msg, address)
                print('sent {} bytes back to {}'.format(
                    maa_msg, address))
                input("Press enter to continue")
            elif(data[0] == "SAR"):
                #PCSC-F sends SAR
                saa_msg = None
                if hss_users.get(data[1], false):
                    saa_msg = "SAA 400 NOK"
                else:
                    saa_msg = "SAA 200 OK"
                saa_msg = saa_msg.encode()
                sent = s.sendto(maa_msg, address)
                print('sent {} bytes back to {}'.format(
                    saa_msg, address))
                input("Press enter to continue")
            elif(data[0] == "AUTH"):
                auth_msg = None
                if hss_users.get(data[1], false):
                    auth_msg = "AUTH 400 NOK"
                else:
                    auth_msg = "AUTH 200 OK"
                auth_msg = auth_msg.encode()
                sent = s.sendto(auth_msg, address)
                print('sent {} bytes back to {}'.format(
                    auth_msg, address))
                input("Press enter to continue")
            elif(data[0] == "UPDATE_LOCATION"):
                location_msg = None
                if hss_users.get(data[1], "") == "":
                    location_msg = "UPDATE_LOCATION 400 NOK"
                else:
                    hss_users[data[1]] = data[2]
                    location_msg = "AUTH 200 OK"
                location_msg = location_msg.encode()
                sent = s.sendto(location_msg, address)
                print('sent {} bytes back to {}'.format(
                    location_msg, address))
                input("Press enter to continue")
