import numpy as np
import math 
import random 

def ob(vec, matrix): 
    if(matrix.shape[0] != vec.size): return
    return np.dot(vec, np.dot(matrix, vec))

def prob(old, new, temp): 
    try: 
        math.exp(-(new-old)/(temp))
        # print(math.exp(-(new-old)/(temp)))
    except OverflowError: 
        return 1
    return math.exp(-(new-old)/(temp))

def transform(vec, matrix, min_val): 
    return 1-(math.exp(-(np.dot(vec, np.dot(matrix, vec))-min_val)))