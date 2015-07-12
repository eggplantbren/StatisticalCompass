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
	# pos is in [-most_extreme, most_extreme]
	result = pos/most_extreme		# \in [-1, 1]
	#result = result**3				# Nonlinear transformation if desired (must be odd)
	result = 5.*result				# Transform to [-5, 5]

	return [result, most_extreme]


if __name__ == '__main__':
	"""
	Load the questions and print the mean and sd of the question vectors
	"""
	questions = pd.read_csv('questions.csv')
	[pos, most_extreme] = transform(np.array([14.2, -3.1, -1.4]), questions)
	print(pos)

