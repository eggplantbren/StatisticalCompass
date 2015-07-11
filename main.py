import numpy as np
import pandas as pd

# Load the questions
questions = pd.read_csv('questions.csv')

# Initialise the position of the user at the origin
pos = np.zeros(3)

input_text = 'Enter response from -2 (strongly disagree) to +2 (strongly agree): '

# Using a C-style loop without apology
for i in range(0, questions.shape[0]):
	print('\nQuestion {k}:\n'.format(k=i+1))
	print(questions.iloc[i, 0] + '\n')
	response = input(input_text)

