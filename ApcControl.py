import mido
import time
import functions.all
import functions.red
import functions.yellow
import functions.green
import handler

outport = mido.open_output()

#Customise:
ledchase = True

#Messages
print("")
print("APCMiniColourControl")
print("William Titchener © 2021 All Rights Reserved")
print("")
print("   To exit press ^+C")
input("   Press Enter to begin")

#Files
startup = "startup.txt"
initalize = "initalize.txt"
runloop = "runloop.txt"

enable_startup = True
enable_initalize = True
enable_runloop = True

#Colour Presets
'''
def ledgreen(channel):
	for i in channel:
		outport.send(mido.Message('note_on', note=i, channel=0, velocity=1))
def ledred(channel):
	for i in channel:
		outport.send(mido.Message('note_on', note=i, channel=0, velocity=3))
def ledyellow(channel):
	for i in channel:
		outport.send(mido.Message('note_on', note=i, channel=0, velocity=5))
def ledgreenblink(channel):
	for i in channel:
		outport.send(mido.Message('note_on', note=i, channel=0, velocity=2))
def ledredblink(channel):
	for i in channel:
		outport.send(mido.Message('note_on', note=i, channel=0, velocity=4))
def ledyellowblink(channel):
	for i in channel:
		outport.send(mido.Message('note_on', note=i, channel=0, velocity=6))
'''
#Panel Defining
'''
ledgreen([56,48,40,32,24])
ledyellow([16,8,0])
ledred([57,49,41,33,25,17,9,1])
ledred([58,50,42,34,26,18,10,2])
ledred([59,51,43,35,27,19,11,3])
ledgreen([60,52,44,36,28])
ledyellow([20,12,4])
ledgreen([61,53,45,37,29,21,13,5])
ledgreen([62,54,46,38,30,22,14,6])
ledredblink([63,55,47,39,31,23,15,7])

ledred([64,65,66,67,68,69,70,71])
ledgreen([82,83,84,85,86,87,88,89])
'''
def filehandler(file):
	with open('animations/{}'.format(file), 'r') as animation:
		for line in animation: exec(handler.ch(line))

def loopedfilehandler(file):
	with open('animations/{}'.format(file), 'r') as animation:
		while True:
			for line in animation: exec(handler.ch(line))

if enable_startup == True: filehandler(startup)
if enable_initalize == True: filehandler(initalize)
if enable_runloop == True: loopedfilehandler(runloop)



#print(handler.ch("red.on@56,48"))

functions.yellow.on([56,48],outport)
functions.red.on([40,32],outport)
functions.green.on([24,16,8,0],outport)
functions.green.on([57,49,41,33],outport)
functions.yellow.on([25,17,9,1],outport)
functions.red.on([58,50,42,34],outport)
functions.yellow.on([26,18,10,2],outport)
functions.red.blink([59,51,43,35,27,19,11,3],outport)
functions.green.on([60,52,44],outport)
functions.green.on([36,28,20,12],outport)
functions.all.off([4],outport)
functions.red.blink([61,53,45,37],outport)
functions.green.blink([29,21,13,5],outport)
functions.yellow.on([62,54,46,38,30,22,14,6],outport)
functions.all.off([63,55,47,39,31,23,15,7],outport)

print("")
print("System ON")
print("DO NOT CLOSE THIS WINDOW")

#Led chase
while ledchase == True:
	for i in [82,83,84,85,86,87,88,89]:
		time.sleep(0.3)
		functions.green.on([i],outport)
		time.sleep(0.3)
		functions.all.off([i],outport)
