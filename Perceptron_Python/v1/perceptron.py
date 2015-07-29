import math
from numpy import random, array
from random import choice
import matplotlib.pyplot as plt

"""
This is single unit perceptron that learns simple boolean functions
"""

class Perceptron():
    
    """
    this is the thereshold to activate the unit 
    """
    def activation(self,x):
        if x >= 0:
            return 1
        else:
            return 0

    def linear_combination(self, X):
        total = 0
        for i in xrange(len(self.weights)):
            total += self.weights[i] * X[i]
        return total
    
    def unit_output(self, X):
        return self.activation(self.linear_combination(X))

    def train(self, training_data, epochs):
        
        self.learning_rate = 0.2
        self.errors = []

        # initializing weights
        self.weights = random.rand(len(training_data[1][0]))
        
        for i in xrange(epochs):
            X, y = choice(training_data)
            # > calculate output with current weight
            output = self.unit_output(X)
            # > calculate error rate (t - o)
            error_rate = y - output
            self.errors.append(error_rate)
            print 'the X: ', X
            print 'output: ',output
            print 'correct target: ', y
            # > apply learning rule which will update weights
            self.weights += self.learning_rate * error_rate * X

    def predict(self,X):
        y = self.unit_output(X)
        return y
                

training_data = [
                (array([0,0,1]), 0),
                (array([0,1,1]), 0),
                (array([1,0,1]), 0),
                (array([1,1,1]), 1),
                ]

p = Perceptron()

p.train(training_data, 100)
print p.predict([1,1,1])
plt.plot(p.errors)
plt.ylabel('errors')
plt.xlabel('epochs')
plt.show()

