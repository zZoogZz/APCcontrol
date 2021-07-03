import mido
import time

def ledyellow(channel):
	for i in channel:
		outport.send(mido.Message('note_on', note=i, channel=0, velocity=5))
def ledyellowblink(channel):
	for i in channel:
		outport.send(mido.Message('note_on', note=i, channel=0, velocity=6))