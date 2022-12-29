class Temperature(object):
	"""
	Represents a temperature
	"""
	def __init__(self, temp):
		"""
		initializes a temperature
		:param temp: temperature
		"""
		self.temp = temp
		self.unit = 'F' # default unit is Fahrenheit

	def setTemp(self, temp):
		"""
		sets the temperature
		:param temp: temperature
		"""
		self.temp = temp

	def getTemp(self):
		"""
		returns the temperature
		:return: temperature
		"""
		return self.temp

	def setUnit(self, unit):
		self.unit = unit

	def getUnit(self):
		return self.unit

	def isNegative(self):
		return self.temp < 0

	def __str__(self):
		return f'{self.temp} {self.unit}'

	def __repr__(self):
		return f'{self.temp} {self.unit}'

	def __lt__(self, other):
		return self.temp < other.temp
	
	def __gt__(self, other):
		return self.temp > other.temp

	def __eq__(self, other):
		return self.temp == other.temp

	def __le__(self, other):
		return self.temp <= other.temp

	def __ge__(self, other):
		return self.temp >= other.temp



