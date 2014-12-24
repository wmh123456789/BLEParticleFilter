from fdnn.tools.datasets import ClassificationEigenDataSet
from scipy import array, argmax, dot
from fdnn.brain.optimize import NeuralNetworkFullBatchOptimizer
from fdnn.brain.network import NexdFeedForwardNetwork
from fdnn.utilities import workspace, listdir
from os.path import splitext, isfile


def majorPlusMinor(major, minor):
	return major * 65536 + minor


def debugPrint(vector):
	for i, e in enumerate(vector):
		print("%2d : %.8e" % (i, e))


def ExtractUUIDListFromFile(filepath, WL=[]):
	f = open(filepath, "r")
	UUID = list(WL)
	for line in f:
		if line == "" or line.startswith("//"):
			continue
		e = line.split("\t")
		if len(e) >= 3:
			major = int(e[1])
			minor = int(e[2])
			uid = str(majorPlusMinor(major, minor))
			if uid not in UUID:
				UUID.append(uid)
	f.close()
	return UUID

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


def BuildDatasetFromIOSBluetoothFile(filepath, classNumber, WL, FL):
	f = open(filepath, "r")
	k = 0
	vector = [0] * len(WL)
	matrix = []
	for line in f:
		if line == "" or line.startswith("//"):
			continue
		e = line.split("\t")
		if line.startswith("#"):
			if sum(vector) > 0.0001:
				matrix.append(vector)
			vector = [0] * len(WL)
		elif len(e) >= 4:
			major = int(e[1])
			minor = int(e[2])
			uid = str(majorPlusMinor(major, minor))
			if uid in WL:
				pos = WL.index(uid)
				val = int(e[3])
				if val != 0:
					rss = (float(val) * 0.01 + 1.0) * 5.0 / 3.0
				else:
					rss = 0.0
				vector[pos] = rss
	f.close()
	dataset = ClassificationEigenDataSet(len(WL), len(FL), feature_labels=WL, 
		class_labels=FL, unique=False)
	for vector in matrix:
		dataset.addSample(array(vector), classNumber, check=False)
	dataset.finalize()
	return dataset


if __name__ == "__main__":

	if not isfile("DangDaiNew_F1.fnn.npz"):

		output_classes = []
		input_features = []
		top = "F1"
		
		def namecmp(x, y):
			assert isinstance(x, str)
			assert isinstance(y, str)
			vx = int(splitext(x.split("-")[1])[0])
			vy = int(splitext(y.split("-")[1])[0])
			if vx < vy:
				return -1
			elif vx > vy:
				return 1
			else:
				return 0

		atop = listdir(top)
		atop.sort(cmp=namecmp)

		for aFile in atop:
			filepath = top + "/" + aFile
			fxy = splitext(aFile)[0]
			output_classes.append(fxy)
			input_features = ExtractUUIDListFromFile(filepath, input_features)

		print output_classes

		dataset = ClassificationEigenDataSet(len(input_features), len(output_classes), 
			class_labels=output_classes, feature_labels=input_features, unique=False)
		for aFile in listdir(top):
			filepath = top + "/" + aFile
			fxy = splitext(aFile)[0]
			cn = output_classes.index(fxy)
			d = BuildDatasetFromIOSBluetoothFile(filepath, cn, input_features, output_classes)
			dataset.append(d)
		dataset.finalize()
		dataset.saveToFile("DangDaiNew_F1.data.npz")

		network = NexdFeedForwardNetwork.randomInitializeForDataset(dataset, 3, 0.0001)
		optres, ehists = NeuralNetworkFullBatchOptimizer.train(
			network, dataset, ftol=1e-5, tol=1e-6, maxiter=600, return_hist=True)
		network.writeToFile("DangDaiNew_F1.fnn.npz")
		network.loadCModel()
		network.writeToBinary("DangDaiNew_F1.model.txt")

	else:

		network = NexdFeedForwardNetwork.readFromFile("DangDaiNew_F1.fnn.npz")
		output_classes = network.output_classes
		input_features = network.input_features


	print network


	
	# coordfile = "DangDaiNew_F1.model.coord"
	# coords = readCoords(coordfile)

	# filepath = "xidanF2quan.txt"
	# tests_set = BuildDatasetFromIOSBluetoothFile(filepath, 0, input_features, output_classes)
	# X = tests_set.getField("input")

	# hist = []

	# for i in xrange(X.shape[0] - 2):
	# 	xx = X[i:i+3, :]
	# 	res = network.activate(xx).sum(axis=0)
	# 	res = res / res.sum()

	# 	x = dot(res, coords[:, 0])
	# 	y = dot(res, coords[:, 1])
	# 	hist.append((x, y))

	# hist = array(hist)

	# from matplotlib import pyplot as plt

	# plotmap=plt.imread("XiDanF2.model.png");
	# p=plt.imshow(plotmap);
	# l_user, = plt.plot(0, 0, 'gs');
 
	# for i in range(len(hist)):
	# 	l_user.set_xdata(hist[i][0]);
	# 	l_user.set_ydata(hist[i][1]);
	# 	plt.draw();
	# 	plt.autoscale(False)
	# 	plt.pause(0.2);

	

	# for v in res:
	# 	print(v[:10])
	# 	x = dot(v, coords[:, 0])
	# 	y = dot(v, coords[:, 1])
	# 	print(x, y)

	# paths = []








