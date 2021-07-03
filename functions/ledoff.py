def ledoff(channel):
	for i in channel:
		outport.send(mido.Message('note_on', note=i, channel=0, velocity=0))