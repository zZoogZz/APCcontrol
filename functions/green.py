import mido
import time

def ledgreen(channel):
	for i in channel:
		outport.send(mido.Message('note_on', note=i, channel=0, velocity=1))
def ledgreenblink(channel):
	for i in channel:
		outport.send(mido.Message('note_on', note=i, channel=0, velocity=2))