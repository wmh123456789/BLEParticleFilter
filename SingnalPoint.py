import os
from ParseRawData import *
import math
import numpy as np
import scipy as sc
import scipy.special as special
import scipy.io as io 
import matplotlib.pyplot as plt
import AllParaminTest as A

class SingnalPoint(object):
	"""docstring for SingnalPoint"""
	def __init__(self):
		super(SingnalPoint, self).__init__()
		self.y = 0
		self.x = 0
		self.name = ''
		self.SampleDict = {}
		self.StatDict = {}
		self.RSSIMax = -30
		self.RSSIMin = -90
		self.RSSIBins = list(xrange(self.RSSIMin,self.RSSIMax+1))

	def __str__(self):
		string = ''
		if self.SampleDict == {}:
			return 'Empty SingnalPoint'
		else:
			string += '{} (x={},y={}):\n'.format(self.name,self.x,self.y)
			for key in self.SampleDict.keys():
				string += '{}({})-> {:>3} samples, avg:{:.1f}, wbl:{:.1f}\n'.format(
					key,self.SampleDict[key]['Tag'],
					len(self.SampleDict[key]['RSSI']),
					self.StatDict[key]['mean'],
					self.StatDict[key]['wblTheta']+self.StatDict[key]['wblLambda'])
			
			return string

	def LoadSampleDict(self,FilePath,DeviceFilter = A.DeviceFilter):
		self.SampleDict = Rawdata2Dict(FilePath,DeviceFilter)
		RootDir,FileName = os.path.split(FilePath)
		self.name = FileName.split('_')[0]
		self.FitRSSIToTheRange()
		pass

	# Fit all rssi value to the range (RSSIMin,RSSIMax)
	def FitRSSIToTheRange(self):
		for key in self.SampleDict:
			for i,rssi in enumerate(self.SampleDict[key]['RSSI']):
				if int(rssi) >= self.RSSIMax:
					self.SampleDict[key]['RSSI'][i] = self.RSSIMax-1
				elif rssi <= self.RSSIMin:
					self.SampleDict[key]['RSSI'][i] = self.RSSIMin+1

	# Calc Statics data of sample data
	# Output :  {ID:{'RSSI':xx, 'mean':xx, ...},...}
	def CalcStatDict(self):
		if self.SampleDict == {}:
			print 'SampleDict is Empty, please load some data first~'
		else:
			for key in self.SampleDict:
				aRSSI = np.asarray(self.SampleDict[key]['RSSI'],dtype=np.int)
				self.StatDict.update({key:{
					'N' : len(self.SampleDict[key]['RSSI']),
					'RSSI': aRSSI,
					'hist': np.histogram(aRSSI,self.RSSIBins)[0],
					'mean': np.mean(aRSSI),
					'mid' : np.median(aRSSI),
					'std' : np.std(aRSSI),
					'wblTheta' : self.FitWbl(aRSSI)['theta'],
					'wblK': self.FitWbl(aRSSI)['k'],
					'wblLambda' : self.FitWbl(aRSSI)['lambda']
					}
				})

	# for the input numpy array X, fit it to weibull distribution
	# Output: {'theta':xx ,'lambda':xx, 'k':xx}
	def FitWbl(self,X):
		delta = np.std(X)
		k = delta/np.log(2)
		if delta < 2:
			lmbd = 2*(k+0.15)
		elif delta <= 3.5:
			lmbd = delta*(k+0.15)
		else: # delta > 3.5
			lmbd = 3.5*(k+0.15)

		theta = np.mean(X) - lmbd*special.gamma(1+1/k)
		return {'theta':theta ,'lambda':lmbd, 'k':k}



	# for the input numpy array X, fit it to norm distribution
	# Output:{'miu':xx,'sigma':xx}
	def FitNorm(self,X):
		return {'miu':np.mean(X),'sigma':np.std(X)}


	def LocName2XY(self):
		# Name : [x,y], x,y are relative coordinates
		# LocDict = { 'A' :(0,0),
		# 			'AB':(1,0),
		# 			'B' :(2,0),
		# 			'BC':(2,1),
		# 			'C' :(2,2),
		# 			'CD':(1,2),
		# 			'D' :(0,2),
		# 			'AD':(0,1),
		# 			'O' :(1,1) 
		# 			}
		LocDict = A.AnchorDict
		self.x, self.y = LocDict[self.name]


def main():
	RootDir = r'E:\= Workspaces\Git\BLEParticleFilter\Test\From HongBo\20141201NineP\8M'
	# FileName =  'A_8_20141201T172926.txt'
	for FileName in os.listdir(RootDir):
		if '.txt' in FileName:
			SP = SingnalPoint()
			SP.LoadSampleDict(os.path.join(RootDir,FileName))
			SP.LocName2XY()
			SP.CalcStatDict()
			print SP

	

if __name__ == '__main__':
	main()