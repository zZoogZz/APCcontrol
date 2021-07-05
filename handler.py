addresslimit = 98
string = ["",""]

def addresseshandler(ads = string[1]):
	addresses = []
	adsnorm = ads
	try: #Thru Commands
		ads = ads.split("-")
		ads[0] = int(ads[0])
		ads[1] = int(ads[1])
		if len(ads) == 2 and ads[0] < ads[1]:
			if ads[0] < addresslimit and ads[1] < addresslimit:
				for val in range(ads[0],ads[1]+1): addresses.append(val)
		else:
			print("WARNING: {} Thru {} based addresses not allowed! Check they are under {} and the values are the right way around".format(ads[0],ads[1],addresslimit))
			addresses = [0]
	except:
		try: #Normal Commands
			if addresslimit in ads:
				print("WARNING: An address in \"{}\" was above the addresslimit of {}. Please review.".format(ads,addresslimit))
				addresses = [0]
			else:
				ads = adsnorm.split(",")
				for address in ads:
					addresses.append(int(address))
		except type:
			print("WARNING: Address: \"{}\" was not recognised/allowed. Please review.".format(ads))
			addresses = [0]
	return addresses


def ch(string):
	#permitted values
	colours = ["red","yellow","green"]
	commands = ["on","blink"]
	allcommands = ["off","sleep"]
	#

	if string == "\n": return("pass")
	if string[0:] == "#": return("pass")
	string = string.strip()

	try:
		string = string.split("@")
	except: 
		string[0] = string

	fullcommand = string[0].split(".")
	colour = fullcommand[0]
	command = fullcommand[1]

	try: addresses = addresseshandler(string[1])
	except: pass
	
	'''
	print("Current Instruction Printout")
	print(string)
	print(fullcommand)
	print(colour)
	print(command)
	print(addresses)
	print("End of printout")
	'''

	if colour in colours: #Test that colours are allowed
		coloursafe = True
		if command in commands: #Test that standard colour's command is allowed
			commandsafe = True
		else:
			commandsafe = False
			print("Error with colour instruction type for \"{}\". For the instruction \"{}\"".format(command,string))
	elif colour == "all": #Test that if the colour isn't allowed it is an all command
		coloursafe = True
		if command in allcommands: #Test that the allcommand command is allowed.
			commandsafe = True
		else:
			commandsafe = False
			print("Error with all instruction type for \"{}\". For the instruction \"{}\"".format(command,string))	
	else:
		coloursafe = False
		print("Error with \"{}\". For the instruction \"{}\"".format(colour,string))

	if coloursafe == True and commandsafe == True: 
		#Command Builder
		if command == "sleep":
			exc = "time.sleep(1)"
		else:
			exc = "functions.{colr}.{func}({addresses},outport)".format(colr=colour, func=command, addresses=str(addresses))
		print("EXC: {}".format(exc))
		return(exc)
	elif coloursafe == False or commandsafe == False:
		print("\"{}\" - Command Skipped".format(string))
		return("pass")
	else:
		print("Major Error with command handler")
		return("pass")
