from stochastic_tunneling import stochastic_tunnel_optimize, ob
from simulated_annealing import simulate_anneal_optimize
from adaptive_annealing import adaptive_anneal
from stochastic_tunneling import transform
import matplotlib.pyplot as plt
import numpy as np 
import itertools
order = 5
i = 0
errs = 0 
def generate_bit_vectors(n):
    return list(itertools.product([0, 1], repeat=n))
# Used to determine the required number of iterations for a given order matrix
while i < 100: 
    test_matrix = np.triu(np.random.random((order, order)))
    test_val = ob(adaptive_anneal(15000, test_matrix), test_matrix)
    if test_val != np.min(np.diagonal(test_matrix)): 
        errs += 1
    i+=1 
print((100-errs)/i)
# test_matrix = np.triu(np.random.random((order, order)))
# test_val = ob(stochastic_tunnel_optimize(10000, test_matrix), test_matrix)

# if test_val != np.min(np.diagonal(test_matrix)): 
#     print(test_val)
#     print(np.min(np.diagonal(test_matrix)))
#     bit_vectors = generate_bit_vectors(order)
#     bit_vectors.pop(0)

#     x = np.linspace(1, len(bit_vectors), len(bit_vectors))
#     normal = []
#     transformed = []
#     for i in bit_vectors: 
#         normal.append(ob(np.asarray(i), matrix=test_matrix))
#         transformed.append(transform(np.asarray(i), matrix=test_matrix, min=0))
    
#     plt.plot(x,normal, label = "f(x)")
#     plt.plot(x, transformed, label = "STUN f(x)")
#     plt.legend()
#     plt.show()