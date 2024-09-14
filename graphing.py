import matplotlib.pyplot as plt 
import numpy as np 
from functions import ob, transform, prob
from adaptive_annealing import adaptive_anneal
from simulated_annealing import simulate_anneal_optimize
import itertools 
import random
import math

order = 3
def generate_bit_vectors(n):
    return list(itertools.product([0, 1], repeat=n))
bit_vectors = generate_bit_vectors(order)
bit_vectors.pop(0)

x = np.linspace(1, len(bit_vectors), len(bit_vectors))
matrix = np.triu(np.random.random((order, order)))
normal = []

transformations = []
anneal = adaptive_anneal(10000, matrix)
anneal[3].insert(0, 0)
for i in bit_vectors: 
    normal.append(ob(np.asarray(i), matrix=matrix))

for j in anneal[3]:
    new_arr =[] 
    for i in bit_vectors:
        new_arr.append(transform(i, matrix, j))
    transformations.append(new_arr)
plt.plot(x,normal, label = "f(x)")
j=0

for i in transformations:
    plt.plot(x, i, label=anneal[3][j])
    plt.pause(1)
    j+=1
print("Done")
print(np.min(np.diagonal(matrix))==ob(anneal[0],matrix))
print(np.sum(np.where(np.all(bit_vectors == anneal[0], axis=1)))+1)
# plt.plot(np.linspace(1, len(anneal[1]), len(anneal[1])), np.full(len(anneal[1]), np.min(np.diagonal(matrix))), label="Function Minimum")
# plt.plot(np.linspace(1, len(anneal[1]), len(anneal[1])), anneal[1], label="Temperature")
# plt.plot(np.linspace(1, len(anneal[2]), len(anneal[2])), anneal[2], label='Candidate Minimum')
plt.legend()
plt.show()