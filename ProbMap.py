# probability map over singnal points
from SingnalPoint import *
import AllParaminTest as A

class ProbMap(object):
	"""docstring for ProbMap"""
	def __init__(self):
		super(ProbMap, self).__init__()
		self.SPDict = {}
		self.KeyDict = {}  # Orin data, the key of the source, MacAddr or Major-Minor
		self.ProbDict = {} 			
		self.GlobalRSSIHist = {}
		self.RSSIMax  = 0
		self.RSSIMin  = 0
		self.RSSIBins = []


	def CalcGlobalRSSIHist(self):
		for SPName in self.SPDict:
			SP = self.SPDict[SPName]
			for key in SP.StatDict:
				if key in self.GlobalRSSIHist:
					self.GlobalRSSIHist[key] += np.array(SP.StatDict[key]['hist'])
				else:
					v = np.array(SP.StatDict[key]['hist'])
					self.GlobalRSSIHist.update({key:v})



	def LoadSingnalPoint(self,SP):
		self.SPDict.update({SP.name:SP})
		self.RSSIMax  = SP.RSSIMax 
		self.RSSIMin  = SP.RSSIMin 
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
	# ProbDict[key](x) = P(SPName|RSSI=x)
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

	# Calc. the joint probility of the RSSI-vector in this prob map
	def CalcJointProb(self,RssiVector):
		ResultDict = {}
		for key in RssiVector:
			for SPName in self.ProbDict[key]:
				v = self.ProbDict[key][SPName][RssiVector[key]]
				if SPName in ResultDict:
					ResultDict[SPName] += v*v
				else:
					ResultDict.update({SPName:v})
		for SPName in ResultDict:
			ResultDict[SPName] = ResultDict[SPName]**A.SPwieght_pow_index
		return ResultDict


def main():
	RootDir = r'E:\= Workspaces\Git\BLEParticleFilter\Test\From HongBo\20141201NineP\5M'
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


	# rssi = -70
	# for key in PMap.ProbDict:
	# 	print '==========',key
	# 	p = []
	# 	for SPName in PMap.ProbDict[key]:
	# 		print '---------',SPName
	# 		# print len(PMap.ProbDict[key][SPName])
	# 		if rssi in PMap.ProbDict[key][SPName]:
	# 			p.append(PMap.ProbDict[key][SPName][rssi]) 
	# 			print PMap.ProbDict[key][SPName][rssi]
		# print sum(p)
	
	# print '\n\n=============  For Debug  =================='
	# for key in PMap.ProbDict:
	# 	print '==========',key
	# 	SPName = 'A'
	# 	if rssi in PMap.ProbDict[key][SPName]:
	# 		print PMap.GlobalRSSIHist[key]
	# 		print PMap.SPDict[SPName].StatDict[key]['hist']


	RssiVector = {}
	SPName = 'A'
	for key in PMap.SPDict[SPName].StatDict:
		mean = int(PMap.SPDict[SPName].StatDict[key]['mean'])
		RssiVector.update({key:mean})
	print RssiVector
	ResultDict = PMap.CalcJointProb(RssiVector)
	print ResultDict



if __name__ == '__main__':
	main()