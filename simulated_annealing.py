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
    return math.exp(-(new-old)/(temp))

# Parameters
iterations = 100000
_ = np.vectorize(lambda x: -100*math.log(x) + math.log(iterations)*100)
temps = _(np.linspace(1, iterations-1, iterations-1))
objective_matrix = np.triu(np.random.random((2,2)), k=0)
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
    if(prob(ob(vec_i, objective_matrix), ob(vec_t, objective_matrix), i) >= random.random()):
        vec_i = vec_t.copy()
