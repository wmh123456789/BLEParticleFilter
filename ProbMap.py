# probability map over singnal points

class ProbMap(object):
	"""docstring for ProbMap"""
	def __init__(self, arg):
		super(ProbMap, self).__init__()
		self.arg = arg
		self.SPList = {}


	def LoadSingnalPoint(self,SP):
		self.SPList.udpate({SP.name:SP})
		pass

	def MacFilter(self,MacList):
		for name in self.SPList:
			SP = self.SPList[name]
			
		pass


