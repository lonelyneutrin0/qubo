import numpy as np 
import random 
import math
# Adapting Stochastic Simulated Annealing


def ob(vec, matrix): 
    if(matrix.shape[0] != vec.size): return
    return np.dot(vec, np.dot(matrix, vec))
def transform(vec, matrix, min_val): 
    return 1-(math.exp(-(np.dot(vec, np.dot(matrix, vec))-min_val)))
def adaptive_temperature_exponential(initial_temp, iteration, success_rate):
    """Exponential decay with an adaptive factor based on success rate."""
    decay_rate = 0.95  # Base decay rate
    adjustment_factor = 1 + success_rate  # Adaptive scaling factor (more successful moves -> slower decay)
    return initial_temp * (decay_rate ** (iteration / adjustment_factor))
def adaptive_anneal(iterations, objective):
    
    # Parameters
    current_solution = np.zeros(objective.shape[0], dtype=bool)
    current_temperature = 100
    min_val = 0
    
    successes = 100

    # Data for testing 
    funcs = []
    temps = [current_temperature]
    for i in range(iterations):
    
        success_rate = successes/100
        # Toggle a random bit
        random_bit = random.randint(0, current_solution.size-1)
        new_solution = current_solution.copy()
        new_solution[random_bit]  = not new_solution[random_bit]
        energy_diff = transform(new_solution, objective, min_val) - transform(current_solution, objective, min_val)
        if(np.sum(new_solution) == 0): 
            new_solution[random.randint(0, new_solution.size-1)] = 1
        # Temperature Adjustment
        current_temperature = adaptive_temperature_exponential(current_temperature, i, success_rate)
        
        funcs.append(transform(new_solution, objective, min_val))
        if(current_temperature == 0):
            acceptance_prob = 0
        else: 
            try:
                acceptance_prob = math.exp(-energy_diff / (current_temperature+0.001))   
            except OverflowError: 
                acceptance_prob = 1
          
        temps.append(current_temperature)
        if random.random() < acceptance_prob:
            current_solution = new_solution
            min_val = ob(current_solution, objective)
            successes+=1
        if(i % 100 == 0): 
            print(success_rate)
            successes=0
        # if(current_temperature == 0):
        #     print("Terminated")
        #     break   
    return current_solution, temps, funcs

