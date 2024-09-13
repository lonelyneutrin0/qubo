# qubo
Quadratic Unconstrained Binary Optimization Algorithms
This project explores many ways of optimizing a subset of quadric forms known as QUBO problems. Each method has its own merits and shortcomings. 
A QUBO problem is of the form $$f(\mathbf{v}) : (0,1)^n \to \mathbb R = \mathbf{v^T}\mathbf{A}_{nxn}\mathbf{v}$$
## Simulated Annealing 
This method emulates the physical process of annealing. The solution space is searched by a rate determined by a temperature parameter. This steadily decreases as time passes. New candidates are chosen using the Metropolis-Hastings acceptance rule. This serves as a way to escape local minima. Over time, the number of unfavorable transitions decreases and the algorithm returns the minimum value of the given QUBO problem. 
### Specific Implementation Parameters
Annealing Schedule: `Logarithmic` 
Number of Iterations: `1000000`
