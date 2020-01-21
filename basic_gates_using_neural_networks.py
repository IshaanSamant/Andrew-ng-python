import numpy as np 

def sigmoid(x):
	return 1 / (1+ np.exp(-x))

inputs = np.array([[0,0,1], #The first two digits are the actual input to the neuron whereas the third input is a constant 1
				   [0,1,1],
				   [1,0,1],
				   [1,1,1]])

weights = np.array([20,20,-30]) #AND gate
print("AND gate")
outputs = sigmoid(np.dot(inputs, weights))
print(outputs)

weights = np.array([20,20,-10]) #OR gate
print("OR gate")
outputs = sigmoid(np.dot(inputs, weights))
print(outputs)

weights = np.array([-20,-20,10]) #XNOR gate
print("XNOR gate")
outputs = sigmoid(np.dot(inputs, weights))
print(outputs)

inputs = np.array([[0,1],[1,1]])
print("NOT gate")
weights = np.array([-20,10]) #NOT gate
outputs = sigmoid(np.dot(inputs, weights))
print(outputs)