import mido
import time
import functions.all
import functions.red
import functions.yellow
import functions.green
import handler

#Configurable:
startup = "startup.txt"
initalize = "initalize.txt"
runloop = "runloop.txt"

enable_startup = True
enable_initalize = True
enable_runloop = False

#Functions:
def portopener():
	'''
	Asks the user if they are ready to connect to a port
	Prompts the user if it is unable to connect and waits before attempting to reconnect. 
	'''
	connectioncreated = False
	while connectioncreated == False:
		input("Press enter to connect to port.")
		try:
			outport = mido.open_output()
			connectioncreated = True
		except:
			print("ERROR: Unable to connect to port!")
	return outport

def filehandler(file):
	'''
	Opens the called file, passes each line to the instuction handler.
	Executes the instruction returned from the handler.
	'''
	with open('animations/{}'.format(file), 'r') as animation:
		for line in animation: exec(handler.ch(line))

def loopedfilehandler(file):
	'''
	Opens the called file, passes each line to the instuction handler.
	Executes the instruction returned from the handler.
	Repeats.
	'''
	with open('animations/{}'.format(file), 'r') as animation:
		while True:
			for line in animation: exec(handler.ch(line))

#Execution:
outport = portopener()
if enable_startup == True: filehandler(startup)
if enable_initalize == True: filehandler(initalize)
if enable_runloop == True: loopedfilehandler(runloop)


