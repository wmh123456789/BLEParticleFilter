# probability map over singnal points
from SingnalPoint import *

class ProbMap(object):
	"""docstring for ProbMap"""
	def __init__(self):
		super(ProbMap, self).__init__()
		self.SPDict = {}
		self.KeyDict = {}  # Orin data, the key of the source, MacAddr or Major-Minor
		self.ProbDict = {} 			
		self.GlobalRSSIHist = {}
		self.RSSIMax  = 0
		self.RIISMin  = 0
		self.RSSIBins = []


	def CalcGlobalRSSIHist(self):
		for SPName in self.SPDict:
			SP = self.SPDict[SPName]
			for key in SP.StatDict:
				if key in self.GlobalRSSIHist:
					self.GlobalRSSIHist[key] += SP.StatDict[key]['hist']
				else:
					self.GlobalRSSIHist.update({key:SP.StatDict[key]['hist']})


	def LoadSingnalPoint(self,SP):
		self.SPDict.update({SP.name:SP})
		self.RSSIMax  = SP.RSSIMax 
		self.RIISMin  = SP.RIISMin 
		self.RSSIBins = SP.RSSIBins
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
		for key in self.KeyDict:
			sp_dict = {}
			for SPName in self.SPDict:
				SP = self.SPDict[SPName]
				Bins = SP.RSSIBins
				hist_sp = SP.StatDict[key]['hist']
				
				if len(hist_sp) == len (self.GlobalRSSIHist[key]):
					pdf = hist_sp/(self.GlobalRSSIHist[key]+0.00001)
					rssi_dict = {}
					for i,rssi in enumerate(Bins[0:-1]):
						rssi_dict.update({rssi:pdf[i]})
					sp_dict.update({SPName:rssi_dict})
				else:
					print 'Hist length is not match ~',len (self.GlobalRSSIHist[key])
			self.ProbDict.update({key:sp_dict})
		# print len(self.ProbDict)

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


	# key = '78:A5:04:41:5A:26'
	# print PMap.KeyDict.keys()
	# print PMap.KeyDict['78:A5:04:41:5A:26']['A']['RSSI']
	PMap.CalcGlobalRSSIHist()
	# print PMap.GlobalRSSIHist[key]/float(np.sum(PMap.GlobalRSSIHist[key]))
	PMap.CalcProbDict()

	# for key in PMap.GlobalRSSIHist:
	# 	print key, PMap.GlobalRSSIHist[key]


	rssi = -71
	# for key in PMap.ProbDict:
	# 	print '==========',key
	# 	p = []
	# 	for SPName in PMap.ProbDict[key]:
	# 		print '---------',SPName
	# 		# print len(PMap.ProbDict[key][SPName])
	# 		if rssi in PMap.ProbDict[key][SPName]:
	# 			p.append(PMap.ProbDict[key][SPName][rssi]) 
	# 			print PMap.ProbDict[key][SPName][rssi]
	# 	print sum(p)
			
	for key in PMap.ProbDict:
		print '==========',key
		SPName = 'A'
		if rssi in PMap.ProbDict[key][SPName]:
			print PMap.GlobalRSSIHist[key]
			print PMap.SPDict[SPName].StatDict[key]['hist']


if __name__ == '__main__':
	main()