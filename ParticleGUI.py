__author__ = 'XiaoMing'
from Tkinter import *
import tkFileDialog
from Particle import *
from PIL import Image, ImageTk
from ProbMap import *
import AllParaminTest as A

class DisplayFrame(object):
	"""docstring for DisplayFrame"""
	def __init__(self,width,height,Margin = 0,title=''):
		super(DisplayFrame, self).__init__()
		# self.top = Toplevel()
		self.top = Tk()
		self.top.geometry(str(width)+'x'+str(height)+'+'+str(Margin)+'+'+str(Margin))
		self.top.title(title)
		self.width = width
		self.height = height
		self.initCanvas()
		self.ParticleSize = 5


	def initCanvas(self):
		self.C = Canvas(self.top,width=self.width,height=self.height)
		self.C.pack(expand = 1)

	def initParticleGroup(self,PG,color='blue',size = 5):
		for i in PG.group:
			# print str(PG.group[i])
			rec = self.C.create_rectangle(
					PG.group[i].x,
                    PG.group[i].y,
					PG.group[i].x+size,
					PG.group[i].y+size, 
					fill=color, tags=PG.group[i].tag)
			text = self.C.create_text(
					PG.group[i].x+size,
                    PG.group[i].y+size,
                    fill = color,
                    anchor = NW,
                    text = PG.group[i].id
				)



def main0():
	pg = ParticleGroup()
	for i in xrange(0,10):
		pg.NewParticle(i,i*10,i*i*10,'a')
	pass


	win = DisplayFrame(A.WinW,A.WinH,'Particles')
	win.initParticleGroup(pg,'red')

	win.top.mainloop()
	pass


def InitProbMap(RootDir):
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
	PMap.CalcGlobalRSSIHist()
	print PMap.KeyDict.keys()
	print PMap.SPDict.keys()
	PMap.CalcProbDict()
	return PMap



# Calc the final location with the prob on all SP 
def CalcResultLoc(ResultDict,LocDict):
	Loc = np.array((0.0,0.0))
	TotalWeight = 0.0
	for SPName in ResultDict:
		Loc += np.array(LocDict[SPName]) * ResultDict[SPName] 
		TotalWeight += ResultDict[SPName] 

	print Loc,TotalWeight
	return Loc/TotalWeight

# Calc the final location with the best N SP
def CalcResultLoc_bestN(ResultDict,LocDict,N=1):
	if N > 0 and N <= len(ResultDict) :
		# Pick up best N
		BestResult = sorted(ResultDict.items(), key=lambda d: d[1], reverse=True)[0:N]
		print BestResult
		return CalcResultLoc({item[0]:item[1] for item in BestResult },LocDict)
	else:
		return CalcResultLoc(ResultDict,LocDict)
	pass

def LocationByRV_test (SPName,PMap):
	RssiVector = {}
	for key in PMap.SPDict[SPName].StatDict:
		mean = int(PMap.SPDict[SPName].StatDict[key]['mean'])
		RssiVector.update({key:mean})
	# print RssiVector
	ResultDict = PMap.CalcJointProb(RssiVector)
	return ResultDict




def main():
	ZoomFactor = A.ZoomFactor
	LocDict = A.AnchorDict
	RootDir = A.RootDir
	PM = InitProbMap(RootDir)
	
	# Show Result on the map
	pg_Point = ParticleGroup()
	ShowPointList = A.ShowPointList
	for name in ShowPointList:
		ResultDict = LocationByRV_test(name,PM)
		print sorted(ResultDict.items(), key=lambda d: d[1], reverse=True)
		Loc = CalcResultLoc_bestN (ResultDict,LocDict,A.BestN) * ZoomFactor
		# Loc = CalcResultLoc(ResultDict,LocDict) * ZoomFactor
		print 'LocResult:',Loc
		pg_Point.NewParticle(name+'_',Loc[0],Loc[1])

	# Draw Anchor Points
	pg_Anchor = ParticleGroup()
	for SPName in LocDict:
		pg_Anchor.NewParticle(SPName,LocDict[SPName][0]*ZoomFactor,LocDict[SPName][1]*ZoomFactor)

	win = DisplayFrame(A.WinW,A.WinH,title='LocationShow')
	win.initParticleGroup(pg_Anchor,'red',size=8)

	# Draw Result
	win.initParticleGroup(pg_Point,'blue',size=12)
	win.top.mainloop()

if __name__ == "__main__":
	main()