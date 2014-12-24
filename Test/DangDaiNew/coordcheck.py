from PIL import Image, ImageDraw, ImageFont
from numpy import array


def plotBeaconNodes(imageFile, coordFile, saveFile):
	im = Image.open(imageFile)
	font = ImageFont.truetype("../FreeMono.ttf", 30)

	f = open(coordFile, "r")
	xy = []
	for line in f:
		e = line.split()
		if len(e) != 3:
			continue
		x = float(e[1]) - 15.0
		y = float(e[2]) - 15.0
		xy.append((x, y))
	f.close()

	draw = ImageDraw.Draw(im)
	for i, p in enumerate(xy):
		draw.text(p, "%d" % (i+1), font=font, fill=(255, 0, 0, 255))

	im.save(saveFile)
	

if __name__ == "__main__":

	imageFile = "DangDaiNew_F1.model.png"
	coordFile = "DangDaiNew_F1.model.coord"
	saveFile = "DangDaiNew_F1.beacons.png"

	plotBeaconNodes(imageFile, coordFile, saveFile)