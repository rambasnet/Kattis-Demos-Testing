__author__ = "Ram Basnet"
__date__ = "2023/1/1"
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Ram Basnet"

"""
Hello World Class
"""

class HelloWorld(object):
	"""
	Hello World program using OOP
	"""
	def __init__(self) -> None:
		"""
		Constructor
		"""
		self._message = 'Hello World!'

	def print_message(self) -> None:
		"""
		Prints the message
		:return: None
		"""
		print(self.message)

	def get_message(self) -> str:
		"""
		Returns the message
		:return: message
		"""
		return self._message

	@property
	def message(self):
		"""
		Property getmethod
		"""
		return self._message

