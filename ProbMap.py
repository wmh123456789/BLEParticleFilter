# probability map over singnal points

class ProbMap(object):
	"""docstring for ProbMap"""
	def __init__(self, arg):
		super(ProbMap, self).__init__()
		self.arg = arg
		self.SPList = {}
		self.KeyList = {} # the key of the source, MacAddr or Major-Minor


	def LoadSingnalPoint(self,SP):
		self.SPList.udpate({SP.name:SP})
		pass

	# Update the Keylist by SPlist
	def MacFilter(self,MacList):
		for name in self.SPList:
			SP = self.SPList[name]
			for key in SP: # key is macaddr in android
				if key in self.KeyList:
					pass
				else:
					pass

		pass


