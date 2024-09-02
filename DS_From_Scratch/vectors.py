from typing import List
 #this is a vector type alias
Vector = List[float]

height_weight_age = [70, #inches
                     170,#pounds
                     40] #years

grades = [95, #exam1
          80, #exam2
          75, #exam3
          62] #exam4

grades2 = [95, #exam1
           80, #exam2
           75, #exam3
           62] #exam4

 # a sum function for vectors
def vector_addition(a:Vector, b:Vector)-> Vector:
    '''A vector addition function . 
    Note that vectors can only be added if they are of
    the same length.
    '''
    if len(a) == len(b):
        return    [v_i + w_i for v_i, w_i in zip(a,b)]
    else:
        assert len(a) == len(b), 'Vectors must be of the same length'

def vector_subtraction(a:Vector, b:Vector)-> Vector:
    '''
    A vector subtraction function.
    Note that vectors must be of the same length.
    '''        
    if len(a) == len(b):
        return [v_i - w_i for v_i, w_i in zip(a,b)]
    else:
        assert len(a) == len(b), 'Vectors must be of the same length'

def vector_sum(vectors:List[Vector])-> Vector:
    '''
    Sums all corresponding elements of every vector passed 
    and makes it into a new vector
    '''        
    #Check that vectors are not empty
    assert vectors, 'No vector provided!'

    #Check that all the vectors are the same size
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors)
    
    #the i-th element of the result is the sum of every vector[i]
    return[sum(vector[i] for vector in vectors) for i in range(num_elements)]


def scalar_multiply(a:Vector,  b:float)-> Vector:
    '''
    Multiplies the passed vector(a) by a passed scalar(b)
    '''
    assert a, 'Vector must exist'
    return[ v_i * b for v_i in a]

def vector_mean(vectors:List[Vector])-> Vector:
    '''Computes the element-wise average'''
    n = len(vectors)
    return scalar_multiply(vector_sum(vectors),1/n)

def dot(a:Vector , b:Vector)-> float:
    '''
    Computes v_1 * w_1 +....+ v_n * w_n
    '''
    assert len(a) == len(b), 'Vectors must be of the same length'

    return sum(v_i* w_i for v_i, w_i in zip(a,b))


def sum_of_squares(a:Vector)-> float:
    '''
    Returns v_1*v_1 + ... + v_n * v_n.
    Basically, it returns the sum of the
    squares of each component of (a)
    '''
    return dot(a,a)

import math

def magnitude(v:Vector)-> float:
    '''
    Returns the magnitude or length of v
    '''
    return math.sqrt(sum_of_squares(v))

def distance_between_2_vectors(a:Vector, b:Vector)-> float:
    '''
    Returns the distance between two vectors (a & b)
    '''
    return magnitude(vector_subtraction(a,b))

    
    