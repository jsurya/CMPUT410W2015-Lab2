import socket
import sys
 
try:
    # Create an AF_INET, STREAM socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit()
 
print 'Socket Created'
host = ''		# Accept any connection
port = 8888

try:
	s.bind((host, port))
except socket.error as msg:
	# Could not bind to port
	print 'Bind failed. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
	sys.exit()
else:
	print 'Socket bind is complete'

s.listen(5)
print 'Now listening on port ' + str(port)


conn, addr = s.accept() #	Blocking listen
print 'Connection with ' + addr[0] + ':' + str(addr[1])

data = conn.recv(1024)
reply = 'Hello ' + str(data)
conn.sendall(reply.encode("UTF-8"))
conn.close()

s.close()
