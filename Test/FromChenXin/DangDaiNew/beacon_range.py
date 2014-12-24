from fdnn.tools.datasets import ClassificationEigenDataSet
from PIL import Image, ImageDraw, ImageFont
from numpy import array, ndarray
from os import makedirs
from os.path import isdir


color_red = (255, 0, 0, 255)
color_black = (0, 0, 0, 255)



def readCoords(coordfile):
	f = open(coordfile, "r")
	coord = []
	for line in f:
		e = line.split()
		if len(e) == 3:
			x = float(e[1])
			y = float(e[2])
			coord.append((x, y))
	f.close()
	return array(coord)



def drawBeaconRanges(dataset, imgpath, coord, beaconClass, outdir="./"):
	assert isinstance(dataset, ClassificationEigenDataSet)
	assert isinstance(imgpath, str)
	assert isinstance(coord, ndarray)
	assert isinstance(beaconClass, int)
	assert isinstance(outdir, str)

	if outdir.endswith("/"):
		outdir = outdir[:-1]

	if not isdir(outdir):
		makedirs(outdir)

	stat = [0.0] * dataset.nClasses
	nstat = [0] * dataset.nClasses

	for sample in dataset:
		rssi = sample["input"][beaconClass]
		cl = sample["class"]
		stat[cl] += rssi
		if rssi > 0.0:
			nstat[cl] += 1

	im = Image.open(imgpath)
	draw = ImageDraw.Draw(im)
	font = ImageFont.truetype("../FreeMono.ttf", 20)
	R = 30.0

	for i, v in enumerate(stat):
		if v == 0:
			continue

		cx = coord[i][0]
		cy = coord[i][1]

		r = R * float(v) / 24.0
		xy = [cx - r, cy - r, cx + r, cy + r]
		draw.ellipse(xy, fill=color_red, outline=None)

		if r >= 12.0:
			text = "%.0f/%d" % (v, nstat[i])
			sn = len(text)
			tlp = (cx - 6. * sn, cy - 10.0)
			draw.text(tlp, text, font=font, fill=color_black)

	im.save(outdir + "/Beacon_%d.png" % (beaconClass))


if __name__ == "__main__":

	coordfile = "XiDanF2.model.coord"
	coord = readCoords(coordfile)

	dataset = ClassificationEigenDataSet.loadFromFile("XiDanF2.data.npz")
	imgpath = "XiDanF2.model.png"
	outdir = "XiDanF2_Beacons"

	for bclass in xrange(dataset.indim):
		drawBeaconRanges(dataset, imgpath, coord, bclass, outdir)

