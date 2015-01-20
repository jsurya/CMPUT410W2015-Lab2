import socket
import sys
import thread
import select

host = ''		# Accept any connection
port = 8888
size = 1024
server = None
threads = []

def clientThread(conn, addr):
	while 1:
		data = conn.recv(size)
		if data: 
			reply = 'Hello ' + str(data.strip()) + ' at ' + str(addr[0]) + '\n'
			conn.sendall(reply.encode("UTF-8"))
	conn.close()

try:
    # Create an AF_INET, STREAM socket (TCP)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit()
 
print 'Socket Created'

try:
	server.bind((host, port))
except socket.error as msg:
	# Could not bind to port
	if server:
		server.close()
	print 'Bind failed. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
	sys.exit()
else:
	print 'Socket bind is complete'

server.listen(5)
print 'Now listening on port ' + str(port)

while 1:
	conn, addr = server.accept()
	threads.append(thread.start_new_thread(clientThread, (conn, addr)))
		
# close all threads
server.close()
for c in threads:
	c.join()

