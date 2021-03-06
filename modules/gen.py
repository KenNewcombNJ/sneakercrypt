""" gen.py: Generate a one-time-pad. """
import random
import os
import sys

def userPrompt():
	"""Prompts the user for a bit of input regarding pad generation."""
	print("How much entropy would you like to generate?")
	print("   10 kilobytes =    25 messages (\"The Quick Update\")")
	print("  100 kilobytes =   250 messages (\"The Conversation\")")
	print(" 1000 kilobytes =  2500 messages (\"Some Discussions\")")
	print("10000 kilobytes = 25000 messages (\"Social Butterfly\")")
	try:
		num_kb = int(input("Pad Size (kB):  "))
	except ValueError:
		print("Pad size must be an integer! Sneakercrypt will abort.")
		exit()
	if num_kb > 50:
		time = (num_kb/2.0)/60.0
		answer = input("Generating {0} kilobytes will require approximately {1:.1f} minutes. Continue? (Y/n) ".format(num_kb, time))
		if answer.lower() == "n":
			print("Sneakercrypt has terminated.")
			exit()
	name = input("Please enter a name associated with this key: ")
	return [name, num_kb]
	
def getPad(kb):
	"""Actually generates the pad."""
	pad = bytearray()
	print("Generating pad.")
	for byte in range(0, 1000*kb):
		rand = int.from_bytes(os.urandom(1), 'little')
		pad.append(rand)
	return pad

def savePad(name, pad):
	"""Saves pad to disk."""
	with open('./outpads/{0}'.format(name), 'wb') as f:
		f.write(pad)

def genPad():
	"""Generates a one-time pad."""
	# Prompt the user for input
	user_input = userPrompt()
	name   = user_input[0]
	num_kb = user_input[1]
	
	# Generate a pad of length num_kb
	pad = getPad(num_kb)
	
	# Save the pad to disk.
	savePad(name, pad)
	print("The the outpad for {0} has been successfully generated.".format(name))
	print("{0} can use this pad to decrypt your messages (./inpads)".format(name))
	print("Obtain {0}'s outpad and place it in your inpad folder, and you're good to go.".format(name))
