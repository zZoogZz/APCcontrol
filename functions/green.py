import mido

def on(channel,outport):
	for i in channel:
		outport.send(mido.Message('note_on', note=i, channel=0, velocity=1))
def blink(channel,outport):
	for i in channel:
		outport.send(mido.Message('note_on', note=i, channel=0, velocity=2))