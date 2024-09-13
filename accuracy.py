from stochastic_tunneling import stochastic_tunnel_optimize, ob
from simulated_annealing import simulate_anneal_optimize
import numpy as np 
order = 10
i = 0
errs = 0 
# Used to determine the required number of iterations for a given order matrix
while i < 100: 
    test_matrix = np.triu(np.random.random((order, order)))
    if ob(stochastic_tunnel_optimize(4000, test_matrix), test_matrix) != np.min(np.diagonal(test_matrix)): 
        errs += 1
    i+=1 
print(1-errs/i)