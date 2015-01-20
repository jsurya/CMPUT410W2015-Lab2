import socket
import sys
 
try:
    # Create an AF_INET, STREAM socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit()
 
print 'Socket Created'
host = 'www.google.com'
port = 80

try:
	remote_ip = socket.gethostbyname(host)
except socket.gaierror:
	# Could not resolve IP
	print 'Hostname could not be resolved... Exiting'
	sys.exit
else:
	print 'Ip address of ' + host + ' is ' + remote_ip

# Connect to remote server
s.connect((remote_ip , port))
print 'Socket Connected to ' + host + ' on ip ' + remote_ip

# Send some data to remote server
message = "GET / HTTP/1.1\r\n\r\n"
 
try :
    # Send string
    s.sendall(message.encode("UTF8"))
except socket.error:
    # Send failed
    print 'Send failed'
    sys.exit()
 
print 'Message send successfully'