# All param in the test
from ParseRawData import *

# == ProbMap.py ==
# -- CalcJointProb --
SPwieght_pow_index = 1



# == SingnalPoint.py ==
# -- SingnalPoint.LoadSampleDict --
MacDict = {
			# '01:17:C5:39:78:41':'sa', 
			# '01:17:C5:38:BE:39':'sb', 
			# '01:17:C5:1A:74:DB':'sd',
			# '01:17:C5:33:28:18':'sc', 

			'D0:39:72:E8:06:94':'wh', 
			'D0:39:72:E8:05:69':'wg', 
			'B4:99:4C:8A:D1:EF':'we', 
			'B4:99:4C:8A:B2:D9':'wd', 
			'B4:99:4C:8A:C1:5E':'wa', 
			'B4:99:4C:8A:C1:5A':'wb', 
			'B4:99:4C:8A:C7:D4':'wc', 
			'B4:99:4C:8A:AE:9F':'wf', 

			# '78:A5:04:41:68:A3':'bg', 
			# '78:A5:04:41:5D:F9':'bb', 
			# '78:A5:04:41:3A:32':'bf', 
			# '78:A5:04:41:3A:23':'bd', 
			# '78:A5:04:41:5A:26':'bc', 
			# '78:A5:04:41:37:B5':'ba', 
			# '78:A5:04:41:2A:C1':'be', 
			# '78:A5:04:41:17:41':'bh',

			'31:84:A8:BD:76:67':'dd', 
			'1E:09:97:2C:45:33':'da', 
			'34:17:47:B3:BE:F2':'db', 
			'3B:91:83:A3:05:03':'dc'
			}
DeviceFilter = MacDict.keys()


# == ParticleGUI.py ==
# -- main --
WinH = 400
WinW = 400
RootDir = r'E:\= Workspaces\Git\BLEParticleFilter\Test\From HongBo\20141202NineP\April'
ZoomFactor = 150
# # By HongBo
AnchorDict = { 
				# 'A' :(0.0,0.0),
# 				'AB':(1.0,0.0),
# 				'B' :(2.0,0.0),
# 				'BC':(2.0,1.0),
# 				'C' :(2.0,2.0),
# 				'CD':(1.0,2.0),
# 				'D' :(0.0,2.0),
# 				'AD':(0.0,1.0),
# 				'O' :(1.0,1.0) 

				# 'E' :(0.0,0.0),
				# 'EF':(1.0,0.0),
				# 'F' :(2.0,0.0),
				# 'FG':(2.0,1.0),
				# 'G' :(2.0,2.0),
				# 'GH':(1.0,2.0),
				# 'H' :(0.0,2.0),
				# 'EH':(0.0,1.0),
				# 'O' :(1.0,1.0) 
			}
# ShowPointList = ['A','B','C','D','AB','BC','CD','AD','O']

# # By Yuanliang
AnchorDict = {  
#				'A' :(0.0,0.0),
# 				'AB':(1.0,0.0),
# 				'B' :(2.0,0.0),
# 				'BD':(2.0,1.0),
# 				'C' :(0.0,2.0),
# 				'CD':(1.0,2.0),
# 				'D' :(2.0,2.0),
# 				'AC':(0.0,1.0),
# 				'O' :(1.0,1.0) 

				'E' :(0.0,0.0),
				'EF':(1.0,0.0),
				'F' :(2.0,0.0),
				'FH':(2.0,1.0),
				'G' :(0.0,2.0),
				'GH':(1.0,2.0),
				'H' :(2.0,2.0),
				'EG':(0.0,1.0),
				'O' :(1.0,1.0) 
			}

BestN = 3

# == SingnalPoint.py ==
# -- SingnalPoint.LocName2XY --
# RootDir = r'E:\= Workspaces\Git\BLEParticleFilter\Test\FromChenXin\data'
# FilePath = 'E:\= Workspaces\Git\BLEParticleFilter\Test\FromChenXin\MTC.model.coord'
# AnchorDict = LoadSPCoord(FilePath)
ShowPointList = AnchorDict.keys()



