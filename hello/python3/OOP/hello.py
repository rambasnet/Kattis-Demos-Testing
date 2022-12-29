__author__ = "Ram Basnet"
__date__ = "2022/1/1"
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Ram Basnet"

"""
Hello World Class
"""

class HelloWorld:
	"""
	Hello World Program using OOP
	"""
	def __init__(self):
		"""
		Constructor
		"""
		self.message = 'Hello World!'

	def printMessage(self) -> None:
		"""
		Prints the message
		:return: None
		"""
		print(self.message)

	def getMessage(self) -> str:
		"""
		Returns the message
		:return: message
		"""
		return self.message

