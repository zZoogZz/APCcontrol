import mido
import time

outport = mido.open_output()

#Customise:
ledchase = True

#Messages
print("")
print("APCMiniColourControl")
print("William Titchener © 2018 All Rights Reserved")
print("")
print("   Title: WWC Music Concert")
print("   To exit press ^+C")
input("   Press Enter to begin")

#Colour Presets
def ledoff(channel):
	for i in channel:
		outport.send(mido.Message('note_on', note=i, channel=0, velocity=0))
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


ledyellow([56,48])
ledred([40,32])
ledgreen([24,16,8,0])
ledgreen([57,49,41,33])
ledyellow([25,17,9,1])
ledred([58,50,42,34])
ledyellow([26,18,10,2])
ledredblink([59,51,43,35,27,19,11,3])
ledgreen([60,52,44])
ledgreen([36,28,20,12])
ledoff([4])
ledredblink([61,53,45,37])
ledgreenblink([29,21,13,5])
ledyellow([62,54,46,38,30,22,14,6])
ledoff([63,55,47,39,31,23,15,7])

print("")
print("System ON")
print("DO NOT CLOSE THIS WINDOW")

#Led chase
while ledchase == True:
	for i in [82,83,84,85,86,87,88,89]:
		time.sleep(0.3)
		ledgreen([i])
		time.sleep(0.3)
		ledoff([i])
