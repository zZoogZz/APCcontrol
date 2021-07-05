def ch(string):
	#permitted values
	colours = ["red","yellow","green"]
	commands = ["on","blink"]
	allcommands = ["off","sleep"]
	#
	if string == "\n": return("pass")
	if string[0:] == "#": return("pass")
	if string == "['all.sleep\n']": return ("time.sleep(1)")
	try:
		string = string[:-1]
		string = string.split("@")
		fullcommand = string[0].split(".")
		colour = fullcommand[0]
		command = fullcommand[1]
		addresses = string[1]
	except:
		pass



	if colour in colours: #Test that colours are allowed
		coloursafe = True
		if command in commands: #Test that standard colour's command is allowed
			commandsafe = True
		else:
			commandsafe = False
			print("Error with \"{}\". For the instruction \"{}\"".format(command,string))
	elif colour == "all": #Test that if the colour isn't allowed it is an all command
		coloursafe = True
		if command in allcommands: #Test that the allcommand command is allowed.
			commandsafe = True
		else:
			commandsafe = False
			print("Error with \"{}\". For the instruction \"{}\"".format(command,string))	
	else:
		coloursafe = False
		print("Error with \"{}\". For the instruction \"{}\"".format(colour,string))

	if coloursafe == True and commandsafe == True: 
		#Command Builder
		if command == "sleep":
			exc = "time.sleep(1)"
		else:
			exc = "functions.{colr}.{func}([{addresses}],outport)".format(colr=colour, func=command, addresses=addresses)
		return(exc)
	elif coloursafe == False or commandsafe == False:
		print("\"{}\" - Command Skipped".format(string))
		return("pass")
	else:
		print("Major Error with command handler")
		return("pass")
