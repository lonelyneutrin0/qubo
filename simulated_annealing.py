import numpy as np
from dataclasses import dataclass
from numpy import ndarray
from numpy.typing import ArrayLike
@dataclass
class solution: 
    x_min: ndarray 
    xs: ndarray
    energies: ArrayLike 
    accepts: ArrayLike
    rejects: ArrayLike
    """ 
    A container class for outputting the optimal solution to the given QUBO problem
    :param x_min: The bit vector corresponding to the minimum of the QUBO
    :param xs: The various bit vectors cycled through throughout the annealing process
    :param energies: An energy series for data analysis
    :param accepts: The cumalative number of accepts at each iteration
    :param rejects: The cumalative number of rejects at each iteration 
    """
@dataclass
class Annealer:
     ml: int 
     iterations: int
     T_0: float 
     T_f: float 
     X:ndarray=None

     """" 
     A container class storing the hyperparameters of the optimization algorithm 

     :param ml: The Markov Chain length for each random walk 
     :param iterations: The number of iterations for the annealing process 
     :param T_0: The starting temperature 
     :param T_f: The final temperature 
     :param X: The initial bit array. Defaults to None
     """

     def anneal(self, Q:ndarray)->solution: 
          """ 
          The main annealing function 
          :param Q: The QUBO matrix to optimize 
          :returns: A solution object containing run information 
          :raises ValueError: if the QUBO is not a square matrix or the initial bit vector is of inappropriate dimensionality 
          """
          
          # Check the given matrix
          if(len(Q.shape) != 2 or Q.shape[0] != Q.shape[1]): raise ValueError("Ensure that the QUBO is of proper dimensionality.")
          
          # Check the bit vector
          if(self.X is not None and self.X.shape[0] != Q.shape[0]): raise ValueError("Make sure the initial bit vector is of appropriate dimensionality")
          
          # If the initial bit vector is None, generate a random initial solution 
          self.X = np.random.randint(low=0, high=2, size=(Q.shape[0]), dtype=bool) if self.X is None else self.X
          
          # Initialize the ndarrays for data analytics, temperature and the random numbers to be used 
          random_numbers = np.random.uniform(size=(self.iterations, self.ml))
          
          # Energies, bit vectors, accepts and rejects are kept track of after every random walk 
          energies = np.zeros((self.iterations))
          bit_vectors = np.zeros((self.iterations, self.X.shape[0]))
          accepts = np.zeros((self.iterations))
          rejects = np.zeros((self.iterations))
          temperatures = np.linspace(start=self.T_0, stop=self.T_f, num=self.iterations)
          iter_energy = (self.X).T @ Q @ self.X 
          
          # Initiate the annealing
          for step in range(self.iterations): 
               
               # Log the current bit vector and energy value 
               energies[step] = iter_energy
               bit_vectors[step] = self.X 
               iter_temp = temperatures[step]
               
               for ml_step in range(self.ml):
                # Perturb a random bit of the bit vector 
                ran_i = np.random.randint(low=0, high=self.X.shape[0])
                temp_X = np.copy(self.X)
                temp_X[ran_i] = not temp_X[ran_i]
                
                # Compute the energy of the new bit vector
                temp_energy = temp_X.T @ Q @ temp_X
                
                # Analyze new states by the Metropolis condition
                if( (temp_energy-iter_energy) < 0 or np.exp(-(temp_energy-iter_energy)/temperatures[step]) > random_numbers[step, ml_step]):
                    self.X = temp_X
                    iter_energy = temp_energy
                    accepts[step] = 1
                
                else: 
                    rejects[step] = 1
        
          # Compile the results 
          sol = { 
              'x_min': self.X, 
              'xs': bit_vectors,
              'energies': energies, 
              'accepts': np.cumsum(accepts),
              'rejects': np.cumsum(rejects)
          }
          return solution(**sol)


