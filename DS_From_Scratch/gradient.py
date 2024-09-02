from typing import Callable 
from DS_From_Scratch.vectors import Vector
from DS_From_Scratch.Matrices import Matrix
import numpy as np

'''If f is a function of one variable, it's derivative 
at a point x measures how f(x) changes when we make a very
small change to x. THe derivative is defined as the limit
of the difference quotients:'''

def difference_quotient(f: Callable[[float],float],
                        x:float,
                        h:float)-> float:
    '''Calculates the difference quotient of a function'''
    return (f(x + h) - f(x)) / h

'''as h approaches zero'''


'''The derivative is the slope of the tangent line at
(x,f(x)), while the difference quotient is the slope of the 
not-quite-tangent line that runs through(x + h, f(x + h)). As h gets
smaller and smaller, the not-quite-tangent line gets closer and closer 
to the tangent line'''


'''For many functions, it's easy to exactly calculate derivatives. 
FOr example, the square function'''

def square(x:float)->float:
    '''Reurns the square of x '''
    return x ** 2

'''Has the derivative'''
def derivative(x:float)->float:
    '''Calculates the derivativr of x^2'''
    return 2 * x

'''We can estimate derivatives by evaluating the difference quotient
for a very small h:'''

xs = range(-10,11)
actuals = [derivative(x) for x in xs]
estimates = [difference_quotient ( square , x , h = 0.001) for x in xs]

'''Plot to show they are basically the same'''
'''Un-Comment the code for the plot when a demo is required'''
'''
import matplotlib.pyplot as plt
plt.title('Actual derivatives vs Estimates')
plt.plot(xs, actuals, 'rx', label='Actual')
plt.plot(xs, estimates, 'b+', label='Estimates')
plt.legend(loc=9)
plt.show()'''


'''When f is a function of many variables, it has multiple partial derivatives,
each indicating how f changes when we make  small changes in just one of 
the input variables.'''

'''We calculate its Ith partial derivative by treating it as a function
of just its ith variable, holding the other variables fixed: '''

def partial_difference_quotient(
        f:Callable[[Vector], float],
        v:Vector,
        i:int,
        h:float
            ):
    return

def to_one_hot(labels:Vector, dimension:int = 46)->Matrix:
    '''One hot encodes a label note that @labels should be a numerical Vector'''
    result = np.zeros((len(labels),dimension))
    for i, label in enumerate(labels):
        result[i,label] = 1
    return result



"""Un-related plotting of the gradient Ascent of the function -x^2 + 4x"""
def example_func(x):
	return -(x ** 2) + (4 * x)

def gradient_ascent(starting_point, learning_rate, max_iterations, f:Callable[[float],float]):
	x = starting_point
	iterations = 0
	gradients = []
	while iterations < max_iterations:
		gradients.append(x)
		gradient = difference_quotient(f, x, 0.001)
		x = x + learning_rate * gradient
		if gradient < 1e-6:
			break
		iterations += 1
	return (x, gradients)

answer, gradient_values = gradient_ascent(0, 0.1, 1000, example_func)

#Uncomment the code to plot the graph.

import matplotlib.pyplot as plt
plt.title('Gradient Ascent of the function -x^2 + 4x ')
plt.plot(range(len(gradient_values)), gradient_values, 'rx', label='gradients')
plt.show()



