from simulated_annealing import Annealer
import numpy as np
import matplotlib.pyplot as plt
x = Annealer(iterations=1000, ml=100, T_0=10, T_f=1.0)

Q = -np.random.uniform(low=0, high=10, size=(3,3))
sol = x.anneal(Q=Q)
x_min = sol.x_min
print(x_min.T @ Q @ x_min, x_min)
plt.plot(np.arange(1000), sol.accepts) 
plt.xlabel("Iteration No.")
plt.ylabel("Cumalative Acceptance No.")
plt.savefig('acceptances.png', dpi=800, bbox_inches='tight')
plt.close()
plt.plot(np.arange(1000), sol.energies)
plt.ylabel("Energy")
plt.savefig('energies.png', dpi=800, bbox_inches='tight')
plt.close() 
plt.plot(np.arange(1000), sol.rejects)
plt.ylabel("Cumalative Rejection No.")
plt.savefig('rejections.png', dpi=800, bbox_inches='tight')