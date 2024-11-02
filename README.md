# qubo
Quadratic Unconstrained Binary Optimization Algorithms
This project explores many ways of optimizing a subset of quadric forms known as QUBO problems. Each method has its own merits and shortcomings. 
A QUBO problem is of the form $$f(\mathbf{v}) : (0,1)^n \to \mathbb R = \mathbf{v^T}\mathbf{A}_{nxn}\mathbf{v}$$

Source-
I learnt about simulated annealing and its implementation from this repo which was used as reference
https://github.com/jwjeffr/pytorch_annealing

## Simulated Annealing 
This method emulates the physical process of annealing. The solution space is searched by a rate determined by a temperature parameter. This steadily decreases as time passes. New candidates are chosen using the Metropolis-Hastings acceptance rule. This serves as a way to escape local minima. Over time, the number of unfavorable transitions decreases and the algorithm returns the minimum value of the given QUBO problem. 
### Specific Implementation Parameters
Annealing Schedule: `Linear` <br/>
Probability Condition: `Metropolis`
### Issues 
Because of its heavy reliance on randomness, the time taken to find optima can be excessive for larger solution spaces. The next method aims to resolve this issue by reducing the magnitude of local minima.

## Simulated Annealing with Stochastic Tunneling 
Stochastic Tunneling, or STUN is an adaptation of Monte Carlo methods. It tackles the issue of long computation times by transforming the objective function in such a way that local minima are flattened and the global minimum is amplified. The transformation for an objective function f(x) is given by $$T(x) = 1-e^{-s(f(x)-f(x_0))}$$ where $f(x_0)$ is the lowest function value found so far. The parameter `s` controls how much the function is warped. It is advised to tune this to a high value (~10) when $f(x_0)$ is close to the global minimum and keep it low otherwise.  In this implementation, the objective function will be dynamically transformed once a new candidate minimum is discovered. The parameter `s` will also gradually be increased as better candidates are found.


