import numpy as np

class Question:
	"""
	An object of this class is a question. Questions have text and a
	vector associated with them. The norm of the vector should be of order 1.
	"""

	def __init__(self, text, vec):
		"""
		text = question text
		vec = direction and magnitude of the movement implied by strong
				agreement with the statement
		"""
		self.text = text
		self.vec = vec
		norm = np.linalg.norm(vec)
		if norm > 2:
			print("# Warning: created a strongly influential question.")
		elif norm < 0.5:
			print("# Warning: created a weakly influential question.")

