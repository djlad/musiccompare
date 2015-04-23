song = open("Jay Sean - Down.mp3","rb")

for i in range(100):
	byte = song.read(1)
	print byte