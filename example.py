from stochastic_tunneling import Annealer as st_annealer
from simulated_annealing import Annealer as sa_annealer
import numpy as np
import matplotlib.pyplot as plt
st = st_annealer(iterations=1000, ml=100, T_0=10, T_f=1.0)
sa = sa_annealer(iterations=1000, ml=100, T_0=10, T_f=1.0)

Q = -np.random.uniform(low=0, high=10, size=(3,3))
st_sol = st.anneal(Q=Q)
sa_sol = sa.anneal(Q=Q)
st_x_min = st_sol.x_min
sa_x_min = sa_sol.x_min

print(f'Simulated Annealing Minimum: {sa_x_min.T @ Q @ sa_x_min}')
print(f'Stochasic Tuneneling Minimum: {st_x_min.T @ Q @ st_x_min}')

plt.plot(np.arange(1000), st_sol.accepts, label='STSA')
plt.plot(np.arange(1000), sa_sol.accepts, label='SA') 
plt.xlabel("Iteration No.")
plt.ylabel("Cumalative Acceptance No.")
plt.legend()
plt.savefig('acceptances.png', dpi=800, bbox_inches='tight')
plt.close()

plt.plot(np.arange(1000), st_sol.energies, label='STSA')
plt.plot(np.arange(1000), sa_sol.energies, label='SA')
plt.ylabel("Energy")
plt.legend()
plt.savefig('energies.png', dpi=800, bbox_inches='tight')
plt.close() 

plt.plot(np.arange(1000), st_sol.rejects, label='STSA')
plt.plot(np.arange(1000), sa_sol.rejects, label='SA')
plt.ylabel("Cumalative Rejection No.")
plt.legend()
plt.savefig('rejections.png', dpi=800, bbox_inches='tight')
