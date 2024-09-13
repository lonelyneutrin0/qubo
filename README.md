# qubo
Quadratic Unconstrained Binary Optimization Algorithms
This project explores many ways of optimizing a subset of quadric forms known as QUBO problems. Each method has its own merits and shortcomings. 
A QUBO problem is of the form $$f(\mathbf{v}) : (0,1)^n \to \mathbb R = \mathbf{v^T}\mathbf{A}_{nxn}\mathbf{v}$$
## Simulated Annealing 
This method emulates the physical process of annealing. The solution space is searched by a rate determined by a temperature parameter. This steadily decreases as time passes. New candidates are chosen using the Metropolis-Hastings acceptance rule. This serves as a way to escape local minima. Over time, the number of unfavorable transitions decreases and the algorithm returns the minimum value of the given QUBO problem. 
### Specific Implementation Parameters
Annealing Schedule: `Logarithmic` \n
Number of Iterations: `1000000`
### Issues 
Because of its heavy reliance on randomness, the time taken to find optima can be excessive for larger solution spaces. The next method aims to resolve this issue by reducing the magnitude of local minima.
### Benchmark
Number of Trials: `25`\n
Average Time: `9.48s`
## Simulated Annealing with Stochastic Tunneling 
Stochastic Tunneling, or STUN is an adaptation of Monte Carlo methods. It tackles the issue of long computation times by transforming the objective function in such a way that local minima are flattened and the global minimum is amplified. The transformation for an objective function f(x) is given by $$T(x) = 1-e^{-(f(x)-f(x_0))}$$ where $f(x_0)$ is the lowest function value found so far. It is possible to continuously transform the objective function or do so only when stuck at a local minimum.
