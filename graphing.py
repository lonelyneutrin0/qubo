import matplotlib.pyplot as plt 
import numpy as np 
from simulated_annealing import ob 
from stochastic_tunneling import transform
import itertools 
import random

order = 10
def generate_bit_vectors(n):
    return list(itertools.product([0, 1], repeat=n))
bit_vectors = generate_bit_vectors(order)
bit_vectors.pop(0)

x = np.linspace(1, len(bit_vectors), len(bit_vectors))
matrix = np.triu(np.random.random((order, order)))
normal = []
transformed = []
for i in bit_vectors: 
    normal.append(ob(np.asarray(i), matrix=matrix))
    transformed.append(transform(np.asarray(i), matrix=matrix, min=np.min(np.diagonal(matrix))))
plt.plot(x,normal, label = "f(x)")
plt.plot(x, transformed, label = "STUN f(x)")
plt.legend()
plt.show()