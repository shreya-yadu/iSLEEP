import socket
import sys
import numpy as np
import time

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('192.168.0.105', 5154)

publish = bytearray([0, 2, 0, 0, 255, 4, 5, 5, 2 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

i=1
# Example: msg = bytearray([1, 2, 46, 2, 7, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 2, 3, 4])
# c = {'type': mtype.SUBSCRIBE, 'src': 7, 'group': 46, 'class': ftype.SLEEP, 'topic': 2, 'data': bytearray(b'\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x01\x02\x03\x04')}
try:
    # Send data
    while(i<100):
    	print >>sys.stderr, 'publishing "%s"' % str(publish)
    	sent = sock.sendto(publish, server_address)
    	time.sleep(5)
    	i=i+1

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
