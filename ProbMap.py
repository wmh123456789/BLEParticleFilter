# probability map over singnal points
from SingnalPoint import *

class ProbMap(object):
	"""docstring for ProbMap"""
	def __init__(self):
		super(ProbMap, self).__init__()
		self.SPDict = {}
		self.KeyDict = {}  # Orin data, the key of the source, MacAddr or Major-Minor
		self.ProbDict = {} 		
		
		self.RSSIHist = {}

	# def InitRSSIHist(self):
	# 	for key in self.KeyDict:
	# 		self.RSSIHist.update({key:[]})

	def CalcRSSIHist(self):
		for SPName in self.SPDict:
			SP = self.SPDict[SPName]
			for key in SP.StatDict:
				if key in self.RSSIHist:
					self.RSSIHist[key] += SP.StatDict[key]['hist']
				else:
					self.RSSIHist.update({key:SP.StatDict[key]['hist']})


	def LoadSingnalPoint(self,SP):
		self.SPDict.update({SP.name:SP})
		pass

	# Update the KeyDict by SPDict
	# KeyDict : {key:{SPName:StatDict[key]}}
	def GenKeyDict(self,KeyList = ['']):
		for SPName in self.SPDict:
			SP = self.SPDict[SPName]
			# key is macaddr in android
			for key in SP.StatDict: 
				if key in KeyList or '' in KeyList:
					if key in self.KeyDict:
						self.KeyDict[key].update({SPName:SP.StatDict[key]})
						pass
					else:
						self.KeyDict.update({key:{SPName:SP.StatDict[key]}})
						pass

	# Calc. the probability distribution of each key, over SPs
	def CalcProbDict(self):
		for key in KeyDict:
			pass



def main():
	RootDir = r'E:\= Workspaces\Git\BLEParticleFilter\Test\From HongBo\20141201NineP\8M'
	# FileName =  'A_8_20141201T172926.txt'
	PMap = ProbMap()
	for FileName in os.listdir(RootDir):
		if '.txt' in FileName:
			SP = SingnalPoint()
			SP.LoadSampleDict(os.path.join(RootDir,FileName))
			SP.LocName2XY()
			SP.CalcStatDict()
			# print SP

			PMap.LoadSingnalPoint(SP)

	PMap.GenKeyDict()


	key = '78:A5:04:41:5A:26'
	# print PMap.KeyDict.keys()
	# print PMap.KeyDict['78:A5:04:41:5A:26']['A']['RSSI']
	PMap.CalcRSSIHist()
	print PMap.RSSIHist[key]/float(np.sum(PMap.RSSIHist[key]))



if __name__ == '__main__':
	main()