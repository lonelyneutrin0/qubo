import matplotlib.pyplot as plt 
import numpy as np 
from simulated_annealing import ob 
from adaptive_annealing import transform
from adaptive_annealing import adaptive_anneal
import itertools 
import random
import math

order = 4
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
    transformed.append(transform(np.asarray(i), matrix=matrix, min_val=np.min(np.diagonal(matrix))))

# plt.plot(x,normal, label = "f(x)")
# plt.plot(x, transformed, label = "STUN f(x)")
anneal = adaptive_anneal(10000, matrix)
print(np.min(np.diagonal(matrix))==ob(anneal[0],matrix))
plt.plot(np.linspace(1, len(anneal[1]), len(anneal[1])), np.full(len(anneal[1]), np.min(np.diagonal(matrix))), label="Function Minimum")
plt.plot(np.linspace(1, len(anneal[1]), len(anneal[1])), np.full(len(anneal[1]), 1-(math.exp(-(np.min(np.diagonal(matrix)))))), label="Transformed Minimum")
# plt.plot(np.linspace(1, len(anneal[1]), len(anneal[1])), anneal[1], label="Temperature")
plt.plot(np.linspace(1, len(anneal[2]), len(anneal[2])), anneal[2], label='Candidate Minimum')
plt.legend()
plt.show()