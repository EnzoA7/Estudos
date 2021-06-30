import numpy as np
from random import random


class MLP(object):
    """A Multilayer Perceptron class.
    """
    
    
    def __init__(self, num_inputs=3, hidden_layers=[3, 3], num_outputs=2):
        """Constructor for the MLP. Takes the number of inputs,
           a variable number of hidden layers, and number of outputs
           
        Args:
            num_inputs (int): Number of inputs
            hidden_layers (list): A list of ints for the hidden layers
            num_outputs (int): Number of outputs
        """
        
        
        self.num_inputs = num_inputs
        self.hidden_layers = hidden_layers
        self.num_outputs = num_outputs
        
        # create a generic representation of the layers
        layers = [self.num_inputs] + self.hidden_layers + [self.num_outputs]
        
        # initiate random weights
        weights = []
        for i in range(len(layers) - 1):
            w = np.random.rand(layers[i], layers[i+1])
            weights.append(w)
        self.weights = weights
            
        activations = []
        for i in range(len(layers)):
             a = np.zeros(layers[i])
             activations.append(a)
        self.activations = activations
            
        derivatives = []
        for i in range(len(layers) - 1):
             d = np.zeros((layers[i], layers[i + 1]))
             derivatives.append(d)
        self.derivatives = derivatives           
            
         
    def forward_propagate(self, inputs):
        """Computes forward propagation of the network based on input signals.
        
        Args:
            inputs (ndarray): Input signals
        Returns:
            activations (ndarray): Output values
        """
        
        
        # the input layer activation is just the input itself
        activations = inputs
        self.activations[0] = activations
        
        # iterate through the network layers
        for i, w in enumerate(self.weights):
            # calculate matrix multiplication between previous activation and weight matrix
            net_inputs = np.dot(activations, w)
            
            # calculate the activations
            activations = self._sigmoid(net_inputs)
            
            self.activations[i + 1] = activations
            
        return activations


    def back_propagate(self, error, verbose=False):
        
        for i in reversed(range(len(self.derivatives))):
            activations = self.activations[i+1]
            delta = error * self._sigmoid_derivative(activations) # ndarray([0.1, 0.2]) --> ndarray([[0.1, 0.2]])
            delta_reshaped = delta.reshape(delta.shape[0], -1).T
            current_activations = self.activations[i] # ndarray([0.1, 0.2]) --> ndarray([[0.1], [0.2]])
            current_activations_reshaped = current_activations.reshape(current_activations.shape[0], -1)
            self.derivatives[i] = np.dot(current_activations_reshaped, delta_reshaped)
            error = np.dot(delta, self.weights[i].T)
        
            if verbose:
                print("Derivatives for W{}: {}".format(i, self.derivatives[i]))
        
        return error

    def gradient_descent(self, learning_rate):
        for i in range(len(self.weights)):
            weights = self.weights[i]
            derivatives = self.derivatives[i]
            weights += learning_rate * derivatives
            
    def train(self, inputs, targets, epochs, learning_rate):
        for i in range(epochs):
            sum_error = 0
            
            for input, target in zip(inputs, targets):
               
                # perform forward propagete
                output = self.forward_propagate(input)
    
                # calculate error
                error = target - output
    
                # back propagation
                self.back_propagate(error)
    
                # apply gradient
                self.gradient_descent(learning_rate)    

                sum_error += self._mse(target, output)
            
            
            # report error
            print("Error: {} at epoch {}".format(sum_error / len(inputs), i))

    print("Training complete!")
    print("=====")

    def _mse(self, target, output):
        return np.average((target - output) ** 2)

    def _sigmoid(self, x):
        """Sigmoid activation function
        Args:
            x (flaot): Value to be processed
        Returns:
            y(float): Output
        """
        
        return 1.0 / (1 + np.exp(-x))
    
    def _sigmoid_derivative(self, x):
        return x * (1.0 - x)    
    
if __name__ == "__main__":
   
    # create some inputs
    inputs = np.array([[random()/2 for _ in range(2)] for _ in range(1000)])
    targets = np.array([[i[0] + i[1]] for i in inputs])
     
    # create an MLP
    mlp = MLP(2, [5], 1)
          
    # train our mlp
    mlp.train(inputs, targets, 50, 0.1) 
    
    # create dummy data
    input = np.array([0.3, 0.1])
    target = np.array([0.4])
    
    output = mlp.forward_propagate(input)
    
    print()
    print()
    print('Our network believes that {} + {} is equal to {}'.format(input[0], input[1], output))