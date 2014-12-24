from fdnn.utilities import listdir
from os.path import splitext


def detect(filepath):
	f = open(filepath, "r")
	stat = {}
	for line in f:
		if line.startswith("//") or line.startswith("#"):
			continue
		e = line.split("\t")
		if len(e) < 4:
			continue
		minor = e[2]
		rssi = int(e[3])
		if rssi == 0:
			continue
		stat[minor] = stat.get(minor, 0.0) + (float(rssi) * 0.01 + 1.0)
	f.close()
	return stat


def numdetect(filepath):
	f = open(filepath, "r")
	stat = {}
	k = 0
	for line in f:
		if line.startswith("//"):
			continue
		if line.startswith("#"):
			if k >= 3:
				k = 3
			stat[k] = stat.get(k, 0) + 1
			k = 0
		else:
			e = line.split("\t")
			if len(e) < 4:
				continue
			rssi = int(e[3])
			if rssi == 0:
				continue
			else:
				k += 1
	f.close()
	return stat


n = 0

for aFile in listdir("F1"):
	filepath = "F1/" + aFile
	s = splitext(aFile)[0]
	beacon = s.split("-")[1]
	stat = numdetect(filepath)

	k0 = stat.get(0, 0)
	k1 = stat.get(1, 0)
	k2 = stat.get(2, 0)
	k3 = stat.get(3, 0)

	if k3 < 2 * (k1 + k2):
		print str(beacon) + " : " + str(numdetect(filepath))
		n += 1

print n
	
