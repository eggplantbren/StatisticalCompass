import numpy as np
import pandas as pd

def transform(pos, questions):
	"""
	Takes the user's position and scales it, with some consideration to
	the *available* distance in each direction. The method is ad-hoc and may
	remain so.
	"""
	# Mean and sd of question vectors
	mu = np.mean(questions.iloc[:,1:].values, axis=0)
	sd = np.std(questions.iloc[:,1:].values, axis=0)

	pos = ((pos - mu)/sd)/np.sqrt(questions.shape[0])
	pos = np.sign(pos)*np.sqrt(np.abs(pos))	# Take square root for moderation

	return [pos, mu, sd]


if __name__ == '__main__':
	"""
	Load the questions and print the mean and sd of the question vectors
	"""
	questions = pd.read_csv('questions.csv')
	[pos, mu, sd] = transform(np.zeros(3), questions)
	print(mu)
	print(sd)

