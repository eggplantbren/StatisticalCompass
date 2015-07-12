import numpy as np
import pandas as pd

def transform(pos, questions):
	"""
	Takes the user's position and scales it, with some consideration to
	the *available* distance in each direction. The method is ad-hoc and may
	remain so.
	"""
#	# Old method
#	# Mean and sd of question vectors
#	mu = np.mean(questions.iloc[:,1:].values, axis=0)
#	sd = np.std(questions.iloc[:,1:].values, axis=0)

#	pos = ((pos - mu)/sd)/np.sqrt(questions.shape[0])
#	pos = np.sign(pos)*np.sqrt(np.abs(pos))	# Take square root for moderation
#	return [pos, mu, sd]

	# New method
	most_extreme = 2.*np.sum(np.abs(questions.iloc[:,1:].values), axis=0)
	pos = (pos + most_extreme)/(2.*most_extreme)	# \in [0, 1]
	pos = pos**2				# Nonlinear transformation using a power
	pos = 10.*pos - 5.			# Transform to [-5, 5]

	return [pos, most_extreme]


if __name__ == '__main__':
	"""
	Load the questions and print the mean and sd of the question vectors
	"""
	questions = pd.read_csv('questions.csv')
	[pos, most_extreme] = transform(np.zeros(3), questions)
	print(most_extreme)

