__author__ = 'XiaoMing'
from Tkinter import *
import os

class Particle(object):
	"""docstring for Particle"""
	def __init__(self,pid, x=0,y=0,tag=''):
		super(Particle, self).__init__()
		self.id = pid   # each particle should have a uniqe pid
		self.x = x
		self.y = y
		self.tag = tag
		

	'''Print: id tag x,y '''
	def __str__(self):
		string = ''
		string += '\t'+str(self.id)
		string += '\t'+str(self.tag)
		string += '\t'+str(self.x)+','+str(self.y)

		return string


	def Update(self):
		pass


class ParticleGroup(object):
	"""docstring for ParticleGroup"""
	def __init__(self):
		super(ParticleGroup, self).__init__()
		self.group = {}
	
	def __str__(self):
		string = ''
		for i in self.group:
			string += str(self.group[i])+'\n'
		return string

	def Resample(self):
		pass

	def NewParticle(self,pid,x=0,y=0,tag=''):
		p = Particle(pid,x,y,tag)
		self.group.update({pid:p})

	def FindByTag(self,tag):
		pass


def main():
	pg = ParticleGroup()
	for i in xrange(1,10):
		pg.NewParticle(i,i,i*i/2.0,'a')
	pass

	print str(pg)



if __name__ == "__main__":
	main()