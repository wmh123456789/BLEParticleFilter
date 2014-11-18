__author__ = 'XiaoMing'
from Tkinter import *
import tkFileDialog
from Particle import *
from PIL import Image, ImageTk


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
		self.ParticleSize = 3


	def initCanvas(self):
		self.C = Canvas(self.top,width=self.width,height=self.height)
		self.C.pack(expand = 1)

	def initParticleGroup(self,PG):
		for i in PG.group:
			print str(PG.group[i])
			rec = self.C.create_rectangle(
					PG.group[i].x,
                    PG.group[i].y,
					PG.group[i].x+self.ParticleSize,
					PG.group[i].y+self.ParticleSize, 
					fill='blue', tags=PG.group[i].tag)






def main():
	pg = ParticleGroup()
	for i in xrange(0,10):
		pg.NewParticle(i,i*10,i*i*10,'a')
	pass


	win = DisplayFrame(800,600,'Particles')
	win.initParticleGroup(pg)

	win.top.mainloop()
	pass


if __name__ == "__main__":
	main()