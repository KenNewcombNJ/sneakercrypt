""" crypto.py: An implementation of one-time-pad cryptography."""
import sys

def getMessage():
	message = input("Message : ")
	return message

def encrypt(pad):
	"""Encrypts the message with the given pad."""
	# Get message
	print("A Sneakercrypt message can be 200 characters long.")
	message = getMessage()
	
	# Convert message to byte array
	message_bytes = bytearray(message, 'utf-8')
	
	# Make sure message is <= 200 characters
	if len(message_bytes) > 200:
		print("Message is longer than 200 characters. Sneakercrypt will abort.")
		exit()
	
	# Pad message to 200 characters:
	while len(message_bytes) < 200:
		message_bytes.append(0)

	pad_bytes = bytearray(pad)
	
	cypherbits = []
	for byte in range(0, len(message_bytes)):
		# xor returns an int, which is what a bytearray.append(int) expects
		cypherchar = message_bytes[byte] ^ pad_bytes[byte]
		cypherbits.append(cypherchar)
	
	print("Encrypted Cyphertext:")
	for bit in cypherbits:
		sys.stdout.write(str(bit) + '$')

	sys.stdout.write("\n")
	sys.stdout.flush()
	

def decrypt(pad):
	"""Decrypts given message with given pad."""
	# Construct bytearray from message
	message = getMessage().split('$')[:-1]
	message_bytes = bytearray()
	for word in message:
		message_bytes.append(int(word))

	pad_bytes     = bytearray(pad)

	plaintext = bytearray()
	for byte in range(0, len(message_bytes)):
		plainchar = message_bytes[byte] ^ pad_bytes[byte]
		plaintext.append(plainchar)
	print("Decrypted Plaintext:")
	print(plaintext.decode('utf-8'))