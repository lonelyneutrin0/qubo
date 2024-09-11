import numpy as np 
import random
import math
import matplotlib.pyplot as plt
def ob(vec, matrix): 
    if(matrix.shape[0] != vec.size): return
    return np.dot(vec.T, np.dot(matrix, vec))

start_temp = 1000 
iterations = 1000000
temps = np.linspace(start_temp, 1, iterations)

def prob(old, new, temp): 
    return math.exp((old-new)/temp)

objective_matrix = np.random.random((10, 10))
initial_vector = np.empty((1, objective_matrix.shape[0]))

final_vector = initial_vector
print(final_vector)