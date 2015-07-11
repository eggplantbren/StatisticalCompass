import numpy as np
import pandas as pd

# Load the questions
questions = pd.read_csv('questions.csv')

# Initialise the position of the user at the origin
pos = np.zeros(3)

input_text = 'Enter response from -2 (strongly disagree) to +2 (strongly agree): '

# Using a C-style loop over questions without apology
for i in range(0, questions.shape[0]):

	# Check the question satisfies a basic sanity check
	norm = np.linalg.norm(questions.iloc[i, 1:])
	if norm > 2.:
		print('# WARNING: Very influential question.')
	elif norm < 0.5:
		print('# WARNING: Very uninfluential question.')

	# Print the question
	print('\nQuestion {k}:\n'.format(k=i+1))
	print(questions.iloc[i, 0] + '\n')

	# Get the user's response
	response = None	# Placeholder value
	while response < -2. or response > 2.:
		response = input(input_text)

	# Increment the user's position
	pos += response*questions.iloc[i, 1:].values

