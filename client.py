import sys
import socket
from typing import final

#create tcp/ip socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#conectar al usuario definido
server_address = ('10.252.61.132', 1000)
message = b'SIP REGISTER'

try:

    # Send data
    print('sending {!r}'.format(message))
    sent = sock.sendto(message, server_address)

    # Receive response
    print('waiting to receive')
    data, server = sock.recvfrom(4096)
    print('received {!r}'.format(data))

finally:
    print('closing socket')
    sock.close()

