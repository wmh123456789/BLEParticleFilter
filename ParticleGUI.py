__author__ = 'XiaoMing'
from Tkinter import *
import tkFileDialog
from Particle import *
from PIL import Image, ImageTk
from ProbMap import *


class DisplayFrame(object):
	"""docstring for DisplayFrame"""
	def __init__(self,width,height,title=''):
		super(DisplayFrame, self).__init__()
		# self.top = Toplevel()
		self.top = Tk()
		self.top.geometry(str(width)+'x'+str(height))
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
			print str(PG.group[i])
			rec = self.C.create_rectangle(
					PG.group[i].x,
                    PG.group[i].y,
					PG.group[i].x+size,
					PG.group[i].y+size, 
					fill=color, tags=PG.group[i].tag)



def main0():
	pg = ParticleGroup()
	for i in xrange(0,10):
		pg.NewParticle(i,i*10,i*i*10,'a')
	pass


	win = DisplayFrame(800,600,'Particles')
	win.initParticleGroup(pg,'red')

	win.top.mainloop()
	pass


def InitProbMap():
	RootDir = r'E:\= Workspaces\Git\BLEParticleFilter\Test\From HongBo\20141201NineP\8M'

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
	PMap.CalcProbDict()

	RssiVector = {}
	SPName = 'A'
	for key in PMap.SPDict[SPName].StatDict:
		mean = int(PMap.SPDict[SPName].StatDict[key]['mean'])
		RssiVector.update({key:mean})
	# print RssiVector
	ResultDict = PMap.CalcJointProb(RssiVector)
	return ResultDict




def main():
	ZoomFactor = 150
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
	pg_Anchor = ParticleGroup()
	for SPName in LocDict:
		pg_Anchor.NewParticle(SPName,20+LocDict[SPName][0]*ZoomFactor,20+LocDict[SPName][1]*ZoomFactor)


	win = DisplayFrame(400,400,'Particles')
	win.initParticleGroup(pg_Anchor,'red',size=8)

	win.top.mainloop()

	ResultDict = InitProbMap()
	print ResultDict



if __name__ == "__main__":
	main()