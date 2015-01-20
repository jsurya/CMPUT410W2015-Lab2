import socket
import sys
import threading
import select

class Server:
	def __init__(self):
		self.host = ''		# Accept any connection
		self.port = 8888
		self.size = 1024
		self.server = None
		self.threads = []

	def open_socket(self):
		try:
		    # Create an AF_INET, STREAM socket (TCP)
		    self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		except socket.error, msg:
		    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
		    sys.exit()
		 
		print 'Socket Created'

		try:
			self.server.bind((self.host, self.port))
		except socket.error as msg:
			# Could not bind to port
			if self.server:
				self.server.close()
			print 'Bind failed. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
			sys.exit()
		else:
			print 'Socket bind is complete'

		self.server.listen(5)
		print 'Now listening on port ' + str(self.port)

	def run(self):
		self.open_socket()
		input =[self.server, sys.stdin]
		while 1:
			inputReady, outputReady, exceptReady = select.select(input, [], [])

			for s in inputReady:
				if s == self.server:
					# Handle server socket
					c = Client(self.server.accept())
					c.start()
					self.threads.append(c)
				elif s == sys.stdin:
					# Handle standard input
					stdin = sys,stdinreadline()
					break
		# close all threads
		self.server.close()
		for c in self.threads:
			c.join()

class Client (threading.Thread):
	def __init__(self, (client, addr)):
		threading.Thread.__init__(self)
		self.client = client
		self.addr = addr
		self.size = 1024

	def run(self):
		while 1:
			data = self.client.recv(self.size)
			if data: 
				reply = 'Hello ' + str(data)
				self.client.sendall(reply.encode("UTF-8"))
				self.client.close()
			else:
				self.client.close()
				break

if __name__ == "__main__":
	s = Server()
	s.run()
