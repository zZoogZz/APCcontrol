import mido

def on(channel,outport):
	for i in channel:
		outport.send(mido.Message('note_on', note=int(i), channel=0, velocity=5))
def blink(channel,outport):
	for i in channel:
		outport.send(mido.Message('note_on', note=int(i), channel=0, velocity=6))