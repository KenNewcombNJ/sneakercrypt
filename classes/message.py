class Message:

	def __init__(self, message):
		self.message = message
		self.isEncrypted = False
		self.isPadded = False

	def toBinary(self):
		"Converts a string message to a binary string format"
		letter_array = [ord(c) for c in self.message]
		self.message =  "".join([bin(letter)[2:] for letter in letter_array])
	
	def pad(self):
		"Ensures that a binary message is 1600 bits long to obfuscate the true message length"
		while(len(self.message) < 1600):
			self.message += "0"
		self.isPadded = True

	def encrypt(self,key):
		cryptobits = list(zip(key,self.message))
		cypher = []
		for pair in cryptobits:
			pair = ord(pair[0]) ^ ord(pair[1])
			cypher.append(pair)
		self.message =  "".join([str(bit) for bit in cypher])
		self.isEncrypted = True
