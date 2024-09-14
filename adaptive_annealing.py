import numpy as np 
import random 
import math
from functions import ob, prob, transform

def adaptive_anneal(iterations, matrix):
    # Parameters
    
    temps = 10*(-np.log(np.linspace(1, iterations-1, iterations-1)) + math.log(iterations))
    # The initial bit
    initial_bit = np.zeros(matrix.shape[0], dtype=bool)
    initial_bit[random.randint(0, matrix.shape[0] -1)] = 1
    min_val = 0
    # Analytics
    funcs = []
    mins = []
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
        new_ob = ob(new_bit, matrix)
        funcs.append(new_ob)
        if(prob(old_energy, new_energy, i) >= random.random()): 
            if(i == temps[0] or new_ob < min_val):
                mins.append(new_ob)
                print(mins)
                # print(min_val)
            initial_bit = new_bit
        min_val = np.min(mins)
    return initial_bit, temps, funcs, mins

