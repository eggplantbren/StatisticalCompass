import numpy as np

class Question:
	"""
	An object of this class is a question. Questions have text and a
	direction. The text is the question itself, and the direction specifies
	where an "agree" answer drags the user.
	"""

	def __init__(self, text, direction):
		"""
		text = question text
		direction = direction (gets normalised)
		"""
		self.text = text
		self.direction = direction/np.linalg.norm(direction)

