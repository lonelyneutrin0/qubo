from stochastic_tunneling import stochastic_tunnel_optimize, ob
from simulated_annealing import simulate_anneal_optimize
from stochastic_tunneling import adaptive_anneal
from stochastic_tunneling import transform
import matplotlib.pyplot as plt
import numpy as np 
import itertools
order = 10
i = 0
errs = 0 
def generate_bit_vectors(n):
    return list(itertools.product([0, 1], repeat=n))
# Used to determine the required number of iterations for a given order matrix
while i < 100: 
    test_matrix = np.triu(np.random.random((order, order)))
    test_val = ob(adaptive_anneal(100000, test_matrix)[0], test_matrix)
    if test_val != np.min(np.diagonal(test_matrix)): 
        errs += 1
    i+=1 
print((100-errs)/i)

