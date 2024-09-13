# Libraries
import numpy as np 
import random
import math
import matplotlib.pyplot as plt
# Functions
def ob(vec, matrix): 
    if(matrix.shape[0] != vec.size): return
    return np.dot(vec, np.dot(matrix, vec))

def prob(old, new, temp): 
    try: 
        math.exp(-(new-old)/(temp))
    except OverflowError: 
        return 1
    return math.exp(-(new-old)/(temp))
def transform(vec, matrix, min): 
    return 1-(math.exp(-10*(np.dot(vec, np.dot(matrix, vec))-min)))

def stochastic_tunnel_optimize(iterations, objective_matrix): 
    # Parameters
    _ = np.vectorize(lambda x: -100*math.log(x) + math.log(iterations)*100)
    temps = 100*(-np.log(np.linspace(1, iterations-1, iterations-1)) + math.log(iterations))
    min = 0
    
    # Matrices/Vectors
    vec_i = np.full((objective_matrix.shape[0]),0, dtype=bool)
    vec_i[random.randint(0, vec_i.size-1)] = 1
    
    # Iteration
    for i in temps:
        vec_t = vec_i.copy() 
        
        # Toggling a random bit
        random_index = random.randint(0, vec_i.size-1)
        vec_t[random_index] = not vec_t[random_index]
        
        # Avoiding the trivial case
        if(np.sum(vec_t) == 0): 
            vec_t[random.randint(0, vec_t.size-1)] = 1
        
        # Probability Testing
        if(prob(transform(vec_i, objective_matrix, min), transform(vec_t, objective_matrix, min), i) >= random.random()):
            vec_i = vec_t.copy()
            min = ob(vec_i, objective_matrix)
    return vec_i
