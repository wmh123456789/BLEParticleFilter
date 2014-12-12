import os
from ParseRawData import *
class SingnalPoint(object):
	"""docstring for SingnalPoint"""
	def __init__(self):
		super(SingnalPoint, self).__init__()
		self.y = 0
		self.x = 0
		self.name = ''
		self.SampleDict = {}

	def __str__(self):
		string = ''
		if self.SampleDict == {}:
			return 'Empty SingnalPoint'
		else:
			string += '{} (x={},y={}):\n'.format(self.name,self.x,self.y)
			for key in self.SampleDict.keys():
				string += '{} -> {}\n'.format(key,len(self.SampleDict[key]['RSSI']))
			
			return string

	def LoadSampleDict(self,FilePath):
		self.SampleDict = Rawdata2Dict(FilePath)
		RootDir,FileName = os.path.split(FilePath)
		self.name = FileName.split('_')[0]
		pass

	def LocName2XY(self):
		# Name : [x,y], x,y are relative coordinates
		LocDict = { 'A' :(0,0),
					'AB':(1,0),
					'B' :(2,0),
					'BC':(2,1),
					'C' :(2,2),
					'CD':(1,2),
					'D' :(0,2),
					'AD':(0,1),
					'O' :(1,1) 
					}
		self.x, self.y = LocDict[self.name]


def main():
	RootDir = r'E:\= Workspaces\Git\BLEParticleFilter\Test\From HongBo\20141201NineP\8M'
	FileName =  'A_8_20141201T172926.txt'
	SP = SingnalPoint()
	SP.LoadSampleDict(os.path.join(RootDir,FileName))
	SP.LocName2XY()
	print SP
	

if __name__ == '__main__':
	main()