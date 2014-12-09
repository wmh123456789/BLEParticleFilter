# Parse Raw file
# coding = utf-8
import os
from bs4 import BeautifulSoup

def SoupFile(FilePath):
	FileLines = open(FilePath,'r').readlines()
	FileText = ' '.join(FileLines)
	return BeautifulSoup(FileText)

'''
Replace space and '_' by '\t'
'''
def FormartConversion_android(FilePath):
	FileLines = [line.replace('_','\t').replace(' ','\t') 
					for line in open(FilePath,'r').readlines()]
	FileText = ''.join(FileLines)
	fp = open(FilePath,'w')
	fp.write(FileText)
	fp.close()

'''
Read a Rawdata file and save the UUID,MAJOR,MINOR,RSSI into a dict
{MAJOR-MINOR:{'RSSI':[RSSI0,RSSI1,...],'MAJOR':XXXX,'MINOR':YYYY,'UUID':????}}
ID a beacon with MacAddr.
Only save the info of the beacon in MacFileter
Only for Android records
'''
def Rawdata2Dict_ios(FilePath,Fileter = ['']):
	SampleDict = {}
	for line in open(FilePath).readlines():
		if '#' in line:  # sample package ID
			pass
		elif '//' in line or len(line)<3: # Comments or blank line(only \n)
			pass 
		else:			# Data body
			words = line.split()
			if len(words)>3:
				UUID = words[0]
				MAJOR = words[1]
				MINOR = words[2]
				RSSI = words[3]
				ID = MAJOR+'-'+MINOR
				if ID in SampleDict: # if the major-minor already in dict
					SampleDict[ID]['RSSI'].append(RSSI)
				else: 				# if a new major-minor is found
					SampleDict.update({ID:{'RSSI':[RSSI],'MAJOR':MAJOR,'MINOR':MINOR,'UUID':UUID}})
	return SampleDict

'''
Read a Rawdata file and save the Mac,RSSI into a dict
{MacAddr:[RSSI0,RSSI1,...]}
ID a beacon with MacAddr.
Only save the info of the beacon in MacFileter
Only for Android records
'''
def Rawdata2Dict_android(FilePath,MacFileter = ['']):
	# All lines into Samplelist
	# SampleList = [] 
	# Dict structure for Samplelist, mac addr. as a key 
	SampleDict = {}
	FormartConversion_android(FilePath)
	for line in open(FilePath,'r').readlines():
		if '//' in line or 'Timestamp' in line or len(line)<6: # Comments or blank line
			pass
		else:
			words = line.split()
			if len(words)>6:
				Date = words[0]
				Time = words[1]
				MacAddr = words[2]
				UUID = words[3]
				RSSI = words[6]
				if MacAddr in MacFileter or '' in MacFileter:
					if MacAddr in SampleDict:  # if the mac already in dict
						SampleDict[MacAddr]['RSSI'].append(RSSI)
						pass
					else:
						SampleDict.update({MacAddr:{'RSSI':[RSSI]}}) # if a new mac is found
					pass
	return SampleDict


'''
Auto switch android/ios Rawdata2Dict
'''
def Rawdata2Dict(FilePath,DeviceFilter = ['']):
	line = open(FilePath).readline()
	if 'ios' in line.lower():
		print 'Detected as an IOS record~'
		return Rawdata2Dict_ios(FilePath,DeviceFilter)
	elif 'android' in line.lower():
		print 'Detected as an Android record~'
		return Rawdata2Dict_android(FilePath,DeviceFilter)
	else:
		print 'Error: Cannot find the OS tag (ios/android) in the first line.'
		return {}


def GenMatlabFile(FilePath,MacFileter = ['']):
	# SampleDict = Rawdata2Dict_ios(FilePath,MacFileter)
	# SampleDict = Rawdata2Dict_android(FilePath,MacFileter)
	SampleDict = Rawdata2Dict(FilePath,MacFileter)
	RootDir,FileName = os.path.split(FilePath)
	# print SampleDict.keys()
	# Android: MacAddr is key, IOS: Major-Minpr is key
	for key in SampleDict:
		# New file name : oldname_mac.txt
		# NewFile = os.path.splitext(FileName)[0]+'_'+key.replace(':','_')+'.csv'
		NewFile = os.path.splitext(FileName)[0]+'_'+Mac2Tag(key)+'.csv'
		print NewFile
		fp = open(os.path.join(RootDir,NewFile),'w')
		for RSSI in SampleDict[key]['RSSI']:
			if not RSSI in ['0','127']:
				fp.write(RSSI+'\n')
		fp.close()

def Mac2Tag(MacAddr):
	MacDict = { 'D0:39:72:E8:06:94':'wh', 
				'D0:39:72:E8:05:69':'wg', 
				'B4:99:4C:8A:D1:EF':'we', 
				'1E:09:97:2C:45:33':'da', 
				'34:17:47:B3:BE:F2':'db', 
				'3B:91:83:A3:05:03':'dc', 
				'B4:99:4C:8A:B2:D9':'wd', 
				'01:17:C5:38:BE:39':'sb', 
				'B4:99:4C:8A:C1:5E':'wa', 
				'01:17:C5:39:78:41':'sa', 
				'B4:99:4C:8A:AE:9F':'wf', 
				'78:A5:04:41:68:A3':'bg', 
				'78:A5:04:41:5D:F9':'bb', 
				'B4:99:4C:8A:C7:D4':'wc', 
				'78:A5:04:41:3A:32':'bf', 
				'78:A5:04:41:3A:23':'bd', 
				'B4:99:4C:8A:C1:5A':'wb', 
				'78:A5:04:41:5A:26':'bc', 
				'78:A5:04:41:37:B5':'ba', 
				'31:84:A8:BD:76:67':'dd', 
				'78:A5:04:41:2A:C1':'be', 
				'01:17:C5:33:28:18':'sc', 
				'78:A5:04:41:17:41':'bh',
				'01:17:C5:1A:74:DB':'sd' }

	if MacAddr in MacDict.keys():
		return MacDict[MacAddr]
	else:
		print 'Unkown Mac:', MacAddr
		return 'UnkownMac'
	pass



# RootDir = 'E:\= Workspaces\Git\BLEParticleFilter\Test'
# FileName = 'iphone-4.txt'
# RawFile = os.path.join(RootDir,FileName)
# MacFileter = ['01:17:C5:38:BE:39']

# GenMatlabFile(RawFile)


RootDir = r'E:\= Workspaces\Git\BLEParticleFilter\Test\From HongBo\20141208FixDis\Black'
for FileName in os.listdir(RootDir):
	if '.txt' in FileName:
		RawFile = os.path.join(RootDir,FileName)
		GenMatlabFile(RawFile)



# FormartConversion_android(RawFile)

# soup = SoupFile(RawFile)

