import numpy as np 
import random
import math
import matplotlib.pyplot as plt
def ob(vec, matrix): 
    if(matrix.shape[0] != vec.size): return
    # print(np.dot(vec, np.dot(matrix, vec.T)))
    return np.dot(vec, np.dot(matrix, vec.T))

start_temp = 1000
iterations = 100000
temps = np.linspace(start_temp, 1, iterations)

def prob(old, new, temp): 
    return math.exp((old-new)/temp)

# objective_matrix = np.random.random((10,10))
objective_matrix = random.random()*np.random.randint( -3, 4, (10,10))
initial_vector = np.empty((objective_matrix.shape[0]))
initial_vector[0] = 1
final_vector = initial_vector
values = []
for i in temps:
    intermediate_vector = final_vector.copy() 
    # Turning a random bit on and a random bit off
    intermediate_vector[random.randint(0, initial_vector.shape[0]-1)] = 1
    intermediate_vector[random.randint(0, initial_vector.shape[0]-1)] = 0
    # print(ob(intermediate_vector, objective_matrix))
    values.append(ob(intermediate_vector, objective_matrix))
    if prob(ob(intermediate_vector, objective_matrix), ob(final_vector, objective_matrix), i) < random.random(): 
        final_vector = intermediate_vector

print(final_vector)
print(objective_matrix)
print(ob(final_vector, objective_matrix))
x = np.linspace(1, iterations, iterations)
plt.plot(x, values)
plt.show()