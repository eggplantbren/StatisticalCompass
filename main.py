import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from transform import transform

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
	print('\nQuestion {k}/{n}:\n'.format(k=i+1, n=questions.shape[0]))
	print(questions.iloc[i, 0] + '\n')

	# Get the user's response
	response = None	# Placeholder value
	while response is None or response < -2. or response > 2.:
		response = float(input(input_text))

	# Increment the user's position
	pos += response*questions.iloc[i, 1:].values

# Apply some scaling to the position based on how far it was possible
# to move in each dimension
pos = transform(pos, questions)[0]

print('Your position in 3D is ' + str(pos) + '.')

# Plot two of the three coordinates
plt.rc("font", size=20, family="serif", serif="Computer Sans")
plt.rc("text", usetex=True)

plt.figure(figsize=(8, 8))
plt.plot(pos[0], pos[1], 'ro', markersize=10)
plt.axis([-5., 5., -5., 5.])
plt.gca().set_xticks(np.linspace(-5., 5., 11))
plt.gca().set_yticks(np.linspace(-5., 5., 11))
plt.gca().set_xticklabels([])
plt.gca().set_yticklabels([])
plt.grid(True)
plt.axhline(0., color='k', linewidth=2)
plt.axvline(0., color='k', linewidth=2)
plt.xlabel('Frequentist --------- Bayesian')
plt.ylabel('Philosophical --------- Pragmatic')
plt.show()

