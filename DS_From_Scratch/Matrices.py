from typing import List, Tuple, Callable
from pprint import pprint

#Type alias for Matrices

Matrix = List[List[float]]

#type alias for Vector
Vector = List[float]

A:Matrix = [[1,2,3], #A has 2 rows and 3 columns
            [4,5,6]]

B:Matrix = [[1,2],  #B has 3 rows and 2 columns
            [3,4],
            [5,6]]

def shape(A:Matrix)-> Tuple[int,int]:
    '''
    Returns (# of rows of A, # of columns of A)
    '''
    num_row = len(A)
    num_columns = len(A[0]) if A else 0 #number of elements in first row
    return num_row , num_columns


def get_row(A:Matrix, i:int)-> Vector:
    '''
    Returns the i-th row of A (as a Vector)
    '''
    return A[i]

def get_column(A:Matrix, j:int)-> Vector:
    '''
    Returns the j-th column of A (as a Vector)
    '''
    return [A_i[j] for A_i in A]

def make_matrix(
        num_rows: int,
        num_cols: int,
        entry_fn: Callable[[int,int] , float])-> Matrix:
    '''
    Returns a num_rows x num_cols matrix
    whose (i,j)-th entry is entry_fn(i,j)
    '''
    return[[entry_fn(i,j)      #given i, create a list
            for j in range(num_cols)]# [entry_fn(i,0),...]
            for i in range(num_rows)]# create one list for each i
    

def identity_matrix(n: int)-> Matrix:
    '''Returns the n by n identity matrix'''
    return make_matrix(n,n, lambda i ,j : 1 if i == j else 0)

