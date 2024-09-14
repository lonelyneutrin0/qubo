import numpy as np 
import random 
import math
from functions import ob, prob, transform

def adaptive_anneal(iterations, matrix):
    # Parameters
    min_val = 0
    temps = 100*(-np.log(np.linspace(1, iterations-1, iterations-1)) + math.log(iterations))
    # The initial bit
    initial_bit = np.zeros(matrix.shape[0], dtype=bool)
    initial_bit[random.randint(0, matrix.shape[0] -1)] = 1
    
    # Analytics
    funcs = []
    for i in temps: 
        # Creating a new candidate 
        random_index = random.randint(0, matrix.shape[0] -1)
        new_bit = initial_bit.copy()
        new_bit[random_index] = not new_bit[random_index]
        
        # Avoiding the trivial case 
        if(np.sum(new_bit) == 0): 
            random_index = random.randint(0, matrix.shape[0] -1)
            new_bit[random_index] = not new_bit[random_index]
        
        # Testing the probabilities of the new versus old case 
        old_energy = transform(initial_bit, matrix, min_val)
        new_energy = transform(new_bit, matrix, min_val)
        
        funcs.append()
        if(prob(old_energy, new_energy, i) >= random.random()): 
            if(ob(new_bit, matrix) < min_val):
                min_val = ob(new_bit, matrix)
            initial_bit = new_bit
    return initial_bit, temps, 

# test = np.triu(np.random.random((4,4)))
# print(test, adaptive_anneal(100000, test))
