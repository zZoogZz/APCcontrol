import mido
import time


def ledred(channel):
	for i in channel:
		outport.send(mido.Message('note_on', note=i, channel=0, velocity=3))
def ledredblink(channel):
	for i in channel:
		outport.send(mido.Message('note_on', note=i, channel=0, velocity=4))