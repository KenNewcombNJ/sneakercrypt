from autobahn.twisted.websocket import WebSocketClientProtocol

class clientProtocol(WebSocketClientProtocol):

	def onConnect(self):
		print("Connected to Server: {}".format(response.peer))

	def onOpen(self):
		self.sendMessage(u"Hello, world!".encode('utf8'))
		messageSender()

	def onMessage(self, payload, isBinary):
		if isBinary:
			print("Binary message received: {0} bytes".format(len(payload)))
		else:
			print("Text message received: {0}".format(payload.decode('utf8')))

	def onClose(self, wasClean, code, reason):
		print("Connection closed.")

	def messageSender():
		while True:
			message = input("Message:")
			self.sendMessage(message.encode('utf8'))