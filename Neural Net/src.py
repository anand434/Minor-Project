# The program creates an neural network that simulates the exclusive OR
# function with two inputs and one output.

import numpy as np

def nonlin(x,deriv = False):
	if(deriv == True):
		return (x*(1-x))

	return 1/(1+np.exp(-x))

# input data set
X = np.array([[0,0,1],
			[0,1,1],
			[1,0,1],
			[1,1,1]])

# output data set
y = np.array([[0] , [1] , [1] , [0]])

np.random.seed(1)

# Synapses
Synapses0 = 2*np.random.random((3,4)) - 1
Synapses1 = 2*np.random.random((4,1)) - 1

# Training
for j in range(60000):
	l0 = X
	l1 = nonlin(np.dot(l0 , Synapses0))
	l2 = nonlin(np.dot(l1 , Synapses1))

	l2_error = y - l2

	if(j % 10000) == 0:
		# Getting mean value of the absolute error
		print("Error : " + str(np.mean(np.abs(l2_error))))

	l2_delta = l2_error * nonlin(l2 , deriv = True)

	l1_error = l2_delta.dot(Synapses1.T)

	l1_delta = l1_error * nonlin(l1 , deriv = True)

	Synapses1 += l1.T.dot(l2_delta)
	Synapses0 += l0.T.dot(l1_delta)

print("\nOutput after Trainnig : ")
print(l2)